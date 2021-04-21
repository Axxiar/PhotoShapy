from tkinter import messagebox
import tkinter as tk
import webbrowser as web

def dest(*args):
    for widget in args:
        widget.destroy()

def f_getting_started(masterx,mastery):
    """attribution : option "Prise En Main" du sous menu "Outils" (l.afpt)
    description : --à venir--"""
    alerte = messagebox.askyesno(title="Ouverture", message="Ouvrir en ligne ?")
    if alerte == True:              # alerte = True si l'utilisateur clique sur Yes
        web.open_new_tab('https://axxiar.github.io/PhotoShapy/')
    else:                           # alerte = False si l'utilisateur clique sur No
        pem_master = tk.Tk()
        pem_master.title('Prise en main')
        pem_master.geometry(f'{masterx-30}x{mastery-30}')
        pem_master.geometry("+40+60")
        pem_master.config(bg='#022c43')
        pem_master.mainloop()


def source_code():
    """attribution : option "Code Source" du sous menu "Aide" (ligne 180)
    description : ouvre à l'aide du module webbrowser le lien vers ce dépot github"""
    
    web.open_new_tab('https://github.com/AXXIAR/PhotoShapy')
    

def f_doc(masterx,mastery):
    #- renvoyer sur le site (docu à créer)
    """bloub"""
    alerte = messagebox.askyesno(title="Ouverture", message="Ouvrir en ligne ?")
    if alerte == True:              # alerte = True si l'utilisateur clique sur Yes
        web.open_new_tab('https://axxiar.github.io/PhotoShapy/')
    else:                           # alerte = False si l'utilisateur clique sur No
        docu_master = tk.Tk()
        docu_master.title('Prise en main')
        docu_master.geometry(f'{masterx-30}x{mastery-30}')
        docu_master.geometry("+40+60")
        docu_master.config(bg='#022c43')
        docu_master.mainloop()


def f_credit(masterx,mastery):
    credit_master = tk.Tk()
    credit_master.title('Prise en main')
    credit_master.geometry(f'{masterx-30}x{mastery-30}')
    credit_master.geometry("+40+60")
    credit_master.config(bg='#022c43')
    credit_master.mainloop()
