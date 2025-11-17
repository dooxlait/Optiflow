import tkinter as tk
from optiflow.modules.client.services import *

class PalettePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configurer les colonnes pour qu'elles s'étendent
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        # En-têtes
        headers = ["Code", "Client", "Nombre de colis", "Nombre de palette"]
        for col, text in enumerate(headers):
            lbl = tk.Label(self, text=text, anchor="center")
            lbl.grid(row=0, column=col, sticky="ew", padx=5, pady=5)

        # Frame pour le tableur avec scrollbar
        self.table_frame = tk.Frame(self)
        self.table_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)  # Laisser la frame tableur s'étendre verticalement

        self.canvas = tk.Canvas(self.table_frame)
        self.scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.canvas.yview)
        self.inner_frame = tk.Frame(self.canvas)

        self.inner_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Liste pour stocker les lignes (dictionnaires de StringVar)
        self.rows = []

        # Bouton pour ajouter une ligne
        tk.Button(self, text="+", command=self.ajouter_ligne).grid(row=2, column=0, columnspan=4, pady=5)

        # Ajouter la première ligne
        self.ajouter_ligne()

    def ajouter_ligne(self):
        row_index = len(self.rows)
        row_data = {
            "code_var": tk.StringVar(),
            "client_var": tk.StringVar(),
            "colis_var": tk.StringVar(),
            "palette_var": tk.StringVar()
        }

        # Déclencher la mise à jour du client pour chaque modification du code
        row_data["code_var"].trace_add("write", lambda *args, r=row_data: self.code_modifie(r))

        # Créer les widgets pour cette ligne
        tk.Entry(self.inner_frame, textvariable=row_data["code_var"], justify="center").grid(row=row_index, column=0, sticky="ew", padx=5, pady=2)
        tk.Label(self.inner_frame, textvariable=row_data["client_var"], anchor="center").grid(row=row_index, column=1, sticky="ew", padx=5, pady=2)
        tk.Entry(self.inner_frame, textvariable=row_data["colis_var"], justify="center").grid(row=row_index, column=2, sticky="ew", padx=5, pady=2)
        tk.Entry(self.inner_frame, textvariable=row_data["palette_var"], justify="center").grid(row=row_index, column=3, sticky="ew", padx=5, pady=2)

        # Configurer les colonnes pour s'étendre horizontalement
        for col in range(4):
            self.inner_frame.grid_columnconfigure(col, weight=1)

        self.rows.append(row_data)

    def code_modifie(self, row_data):
        code = row_data["code_var"].get()
        if len(code) == 7:
            client = get_client_by_id(code)
            if client:
                row_data["client_var"].set(client.nom)
            else:
                row_data["client_var"].set("Inconnu")
        else:
            row_data["client_var"].set("")
