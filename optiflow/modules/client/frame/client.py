import tkinter as tk
from optiflow.modules.client.frame.Parametrage import ParametrageBase

class ClientPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Page Client", font=("Arial", 16))
        label.pack(pady=20, padx=10)
        
        # Bouton pour naviguer vers la gestion de la base de données
        btn_gestion_base = tk.Button(self, text="Accès Base de données", command=lambda: controller.show_frame("ParametrageBase"))
        btn_gestion_base.pack()
        
        # Bouton vers la liste des clients
        btn_liste_client = tk.Button(self, text="Liste des clients existants", command=lambda: controller.show_frame('ListeClient'))
        btn_liste_client.pack()

        # Bouton pour revenir à l'accueil 
        btn_back = tk.Button(self, text="Retour à l'accueil",
                             command=lambda: controller.show_frame("HomePage"))
        btn_back.pack()