import tkinter as tk
from tkinter import ttk
from optiflow.database import session
from optiflow.modules.client.models.client import Client


class ListeClient(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Colonnes
        colonnes = ("nom", "code_postal", "ville", "compte")
        self.table = ttk.Treeview(self, columns=colonnes, show="headings")

        # En-têtes
        for col in colonnes:
            self.table.heading(col, text=col.capitalize())
            self.table.column(col, width=150)

        self.table.pack(fill="both", expand=True)

        tk.Button(self, text="Actualiser", command=self.afficher_clients).pack()
        tk.Button(self, text="Retour", command=lambda: controller.show_frame("HomePage")).pack()

        self.afficher_clients()

    def afficher_clients(self):
        # Efface les anciennes lignes
        for item in self.table.get_children():
            self.table.delete(item)

        # Requête SQLAlchemy
        clients = session.query(Client).all()

        # Insertion dans le tableau
        for c in clients:
            self.table.insert("", "end", values=(c.nom, c.code_postal, c.ville, c.compte))
