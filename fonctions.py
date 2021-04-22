import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import os
import time
import webbrowser as web
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS GLOBALES       #########################################

def dest(*args):
    for widget in args:
        widget.destroy()
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS MODIFIANT L'INTERFACE       #########################################

def f_close(event):
    """attribution : option "Quitter" du sous menu "Fichiers" (l.afpt)
    description : affiche un message de confirmation pour quitter (OK/CANCEL). 
        Ferme le widget sur lequel l'utilisateur est si OK (une fenêtre étant considérée comme un widget cela la fermera),
        Annule si CANCEL"""
    
    # on stocke dans alerte une messagebox de type okcancel (présente un bouton OK et un bouton Cancel)
    #   title sera le titre de la fenêtre messagebox 
    #   message sera le texte qu'elle affiche
    alerte = messagebox.askokcancel(title="Attention", message="Es-tu sûr de vouloir quitter ?\n\n*Le travail non sauvegardé sera irrecupérable*")
    if alerte == True:              # alerte = True si l'utilisateur clique sur OK
        messagebox.showinfo(title='Au revoir',message="Merci de nous avoir utilisé :)") # on affiche une autre boîte avec du texte seulement pour dire au revoir
        time.sleep(1)                           # on met le programme en pause pendant 1 seconde
        event.widget.destroy()                  # on détruit le widget où à été appelée la fonction
    else:                           # alerte = False si l'utilisateur clique sur CANCEL
        pass                                    # on ne fait rien (la boîte est fermée par défaut) ... retour à l'application

def f_modify(default_lbl,default_noimg,import_button,modify_button,delete_button,frame4,frame5):
    global back,draw,filters,crop,rotate,adjust

    dest(import_button,modify_button,delete_button)
    
    back = tk.Button(frame5, text = "<",font=('Consolas',20,'bold'),bg="#ffd700",fg="#115173",command=lambda:f_back_menu(default_lbl,default_noimg,frame4,frame5))

    draw = tk.Button(frame5, text = "Dessiner",font=('Consolas'),bg="#115173",fg="#ffd700")
    crop = tk.Button(frame5, text = "Rogner",font=('Consolas'),bg="#115173",fg="#ffd700")
    rotate = tk.Button(frame5, text = "Pivoter",font=('Consolas'),bg="#115173",fg="#ffd700")
    filters = tk.Button(frame5, text = "Filtres",font=('Consolas'),bg="#115173",fg="#ffd700")
    adjust = tk.Button(frame5, text = "Ajuster (RGB)",font=('Consolas'),bg="#115173",fg="#ffd700")

    back.pack(side=tk.BOTTOM,pady=10,ipadx=30)
    draw.pack(ipadx=60,ipady=5,pady=10)
    crop.pack(ipadx=65,ipady=5,pady=10)
    rotate.pack(ipadx=60,ipady=5,pady=10)
    filters.pack(ipadx=60,ipady=5,pady=10)
    adjust.pack(ipadx=33,ipady=5,pady=10)

def f_back_menu(default_lbl,default_noimg,frame4,frame5):
    global import_button, modify_button, delete_button
    global back,draw,filters,crop,rotate,adjust
    try:
        dest(back,draw,filters,crop,rotate,adjust)
    except:
        print('pas encore')
        
    import_button = tk.Button(frame5, text = "Importer une photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_open_img(default_lbl,default_noimg))
    modify_button = tk.Button(frame5, text = "Modifier la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_modify(default_lbl,default_noimg,import_button,modify_button,delete_button,frame4,frame5))
    delete_button = tk.Button(frame5, text = "Effacer la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_delete_img(default_lbl,frame4))
    import_button.pack(padx=155,ipady=10,ipadx=10,pady=30)
    modify_button.pack(ipady=10,ipadx=16,pady=30)
    delete_button.pack(ipady=10,ipadx=20,pady=25)
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS MODIFIANT L'IMAGE       #########################################

def f_open_img(default_lbl,default_noimg):
    """attribution : bouton "Importer" (l.afpt)
    description : permet d'ouvrir et de sélectionner depuis l'explorateur de fichiers une image 
    puis de la charger dans la fenêtre"""
    global im                          # permet à la variable im d'être aussi utilisée en dehors de cette fonction 
    
    # askopenfilename est une fonction de filedialog (module tkinter) qui permet de choisir un fichier depuis l'exporateur de fichier puis de récup son chemin d'accès 
    # 
    # ici on stocke le chemin d'accès dans la variable filename
    #   
    #   title sera le nom de la fenêtre de l'explorateur de fichier
    #   initialdir = os.getcwd() permet d'indiquer que l'explorateur de fichier doit s'ouvrir au chemin d'accès où se trouve l'utilisateur
    #   filetypes définit les extensions que l'utilisateur peut choisir
    
    filename = filedialog.askopenfilename(title="Ouvrir un fichier",initialdir= os.getcwd(),filetype=((".png","*.png"), (".jpg","*.jpg"), (".jfif","*.jfif"), ("Tous les fichiers","*")))
    try:                                                        # try fait comprendre à python qu'on essaye quelque chose
        im = Image.open(filename)           # ici on charge la photo sélectionnée et on la stocke dans im 
                                            #(le fichier choisit peut ne pas être dans un format accepté par Pillow) d'où le try:
        
        if im.height >= 20:                     # pas besoins de commenter ca sera modifié
            print('too big')                    # |
            im = im.resize((im.width,150))      # |
        if im.width >= 60:                      # |
            print('too large\n')                  # |
            im = im.resize((200,im.height))     # |
        photoim = ImageTk.PhotoImage(im)             # on charge l'image en élément ImageTk qu'on stocke dans im 
        
        default_noimg.destroy()

        default_lbl.configure(image=photoim,bg='grey')  # on rajoute l'image au label default_lbl 
        default_lbl.image = photoim                     #   (celui qui n'aura pas de modifications pour afficher à l'utilisateur son image de départ) 
        
    except:                                   # mot-clé de python, relié à try : si le code dans try rencontre une erreur alors 
                                              #     (sans doute à cause d'un mauvais format dans notre cas)
        print('erreur')                       #  on print 'erreur'


def f_delete_img(default_lbl,frame4):
    global im, default_noimg
    if 'im' in globals():
        default_noimg = tk.Label(frame4, width=60,height=20,bg='grey',text="Pas d'image",font=('Consolas',10),fg='white')
        default_noimg.pack(pady=10,padx=10,side=tk.TOP)
        
        default_lbl.configure(image='',bg='#053f5e')  # on rajoute l'image au label default_lbl
        del im
    else:
        print("pas d'image")
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS MENU AIDE       #########################################

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
# ----------------------------------------------------------------------------------------------------------------------------------------