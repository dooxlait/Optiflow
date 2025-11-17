import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from optiflow import database
from optiflow.modules.client.models.client import Client

class ParametrageBase(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text='Gestion de la base de données')
        label.pack(pady=20, padx=10)

        self.file_label = tk.Label(self, text="Aucun fichier sélectionné")
        self.file_label.pack(pady=5)

        btn_select_file = tk.Button(self, text="Choisir un fichier", command=self.select_file)
        btn_select_file.pack(pady=5)

        btn_import = tk.Button(self, text="Importer dans la base", command=self.ecrire_base_donnees)
        btn_import.pack(pady=5)
        
        btn_suppression_base = tk.Button(self, text='Supprimer la base de données', command=self.supprimer_base_donnees)
        btn_suppression_base.pack(pady=5)
        
        tk.Button(self, text="Retour", command=lambda: controller.show_frame("ClientPage")).pack()

        self.filepath = None

    def select_file(self):
        filepath = filedialog.askopenfilename(
            title="Sélectionner un fichier",
            filetypes=[("Fichiers Excel", "*.xlsx *.xls"), ("Tous les fichiers", "*.*")]
        )
        if filepath:
            self.filepath = filepath
            self.file_label.config(text=filepath)

    def ecrire_base_donnees(self):
        if not self.filepath:
            tk.messagebox.showwarning("Avertissement", "Aucun fichier sélectionné")
            return

        # Lecture du fichier Excel et convertion en string
        df = pd.read_excel(self.filepath, dtype={"Compte": str, "CP": str})

        # Boucle sur chaque ligne pour créer un Client
        df["CP"] = df["CP"].apply(lambda x: str(int(x)) if pd.notna(x) else "")
        df["Compte"] = df["Compte"].apply(lambda x: str(x).zfill(7))
        clients = [
            Client(
                nom=row.get("Nom Client", ""),
                code_postal=row.get("CP", ""),
                ville=row.get("Ville", ""),
                compte=str(row.get("Compte", ""))
            )
            for _, row in df.iterrows()
        ]
        database.session.bulk_save_objects(clients)
        database.session.commit()

        # Valider les changements dans la base
        database.session.commit()
        messagebox.showinfo("Succès", f"{len(df)} clients importés dans la base")
         
    def supprimer_base_donnees(self):
        # Supposons que Client est le modèle
        database.session.query(Client).delete()
        database.session.commit()
        messagebox.showinfo("Succès", f"La base de données a été supprimée")