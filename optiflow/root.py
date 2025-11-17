import tkinter as tk
from optiflow import database  # engine et session globaux
from optiflow.common.base.basemodel import Base  # pour créer les tables
from optiflow.modules.client.frame.client import ClientPage
from optiflow.modules.client.frame.ListeClient import ListeClient
from optiflow.modules.client.frame.Parametrage import ParametrageBase
from optiflow.modules.expedition.frame.palette import PalettePage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OptiFlow")
        self.geometry("800x600")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Pages à afficher
        for F in (HomePage, ClientPage, ParametrageBase, ListeClient, PalettePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Bienvenue dans l'application !", font=("Arial", 16))
        label.pack(pady=20)

        btn_client = tk.Button(self, text="Aller à la page Client",
                               command=lambda: controller.show_frame("ClientPage"))
        btn_client.pack()
        
        btn_palette = tk.Button(self, text='Aller à la page TSC', command=lambda: controller.show_frame("PalettePage"))
        btn_palette.pack()
        
        btn_quitter = tk.Button(self, text="Quitter", command=self.controller.quit)
        btn_quitter.pack(pady=5)
