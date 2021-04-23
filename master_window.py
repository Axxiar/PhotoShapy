

# afpt = à faire plus tard
# l. = ligne

###########  importation des modules  ###########
import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import os
import time
import webbrowser as web
from fonctions import *
# ----------------------------------------------------------------------------------------------------------------------------------------


######################################################    CREATION DES FONCTIONS    #####################################################

def initialization():
    pass

def modify():
    f_modify(default_lbl,default_noimg,import_button,modify_button,delete_button,frame4,frame5)


def open_img():
    f_open_img(default_lbl,default_noimg)

def delete_img():
    f_delete_img(default_noimg,default_lbl,frame4)


# def rotate():
#     """fonction qui vérifie qu'une image est affichée et si oui qui la tourne de 45° à gauche puis la réaffiche"""
#     global photoim,im
#     if 'im' in globals():       # on vérifie si la variable existe dans les variables globales (en gros si on a une image ouverte dans la fenêtre)
#         default_im= im.rotate(45,expand=True)
#         photodefault_im= ImageTk.PhotoImage(im)
#         lbl.configure(image = photoim)
#         lbl.image = photoim
#     else:
#         print('Aucune image')


def close(event):
    """attribution : option "Quitter" du sous menu "Fichiers" (l.afpt)
    description : affiche un message de confirmation pour quitter (OK/CANCEL). 
        Ferme le widget sur lequel l'utilisateur est si OK (une fenêtre étant considérée comme un widget cela la fermera),
        Annule si CANCEL"""
    f_close(event)

def getting_started():
    """"""
    masterx=master.winfo_width()
    mastery=master.winfo_height()
    f_getting_started(masterx,mastery)
    

def doc():
    #- renvoyer sur le site (docu à créer)
    """bloub"""
    masterx=master.winfo_width()
    mastery=master.winfo_height()
    f_doc(masterx,mastery)


def credit():
    """"""
    masterx=master.winfo_width()
    mastery=master.winfo_height()
    f_credit(masterx,mastery)
    

# ----------------------------------------------------------------------------------------------------------------------------------------


####################################      CREATION ET PARAMETRAGE DE LA FENETRE PRINCIPALE       #########################################

master = tk.Tk()                                           # stockage de la fenêtre principale dans la variable master

master.title("PhotoShapy")                                 # changement du titre de la fenêtre
master.config(bg='#022c43')                                # changement de l'arrière plan 
master.geometry("1850x900")                                # définition de sa taille par défaut à l'ouverture
master.geometry("+25+25")                                  # définition de sa position par défaut à l'ouverture (Décalage_Top ; Décalage_Left)

master.bind('<Escape>', close)                           # lorsque, sur la fenêtre, la touche Echap est préssée, on appelle la fonction destroy (l.afpt)
# ----------------------------------------------------------------------------------------------------------------------------------------


######################################      CREATION DES BOITES QUI STRUCTURE LA FENETRE     #############################################

#   argument 1 : la fenêtre ou boîte dans laquelle on place notre nouvelle boîte
#   argument 2 : définition de la couleure d'arrière-plan de la boîte
frame1 = tk.Frame(master,bg='#022c43')                     
frame2 = tk.Frame(frame1,bg='#053f5e')
frame3 = tk.Frame(frame1,bg='#053f5e')
frame4 = tk.Frame(frame2,bg='#053f5e')
frame5 = tk.Frame(frame2,bg='#053f5e')
separation1 = tk.Frame(frame1,bg='#ffd700')             # cette boîte et la suivante servent de séparations visuelles (les deux traits jaunes sur la fenêtre)
separation2 = tk.Frame(frame2,bg='#ffd700')
# ----------------------------------------------------------------------------------------------------------------------------------------


################################################    CREATION DES BOUTONS ET LABELS   #####################################################

import_button = tk.Button(frame5, text = "Importer une photo",font=('Consolas'),bg="#115173",fg="#ffd700", command = open_img)
modify_button = tk.Button(frame5, text = "Modifier la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=modify)
delete_button = tk.Button(frame5, text = "Effacer la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=delete_img)

lbl_noimg = tk.Label(frame3,width=130,height=43,bg='grey',text="Pas d'image",font=('Consolas'),fg='white')              # lbl_noimg est le label central quand il n'y a pas d'image
lbl = tk.Label(frame3,bg='#053f5e',width=1,height=1)                 # lbl est un label qui contiendra l'image sur laquelle on verra les modifications
lbl2 = tk.Label(frame3,bg='#053f5e',width=1,height=1)                # ce label sert uniquement à 
default_noimg = tk.Label(frame4, width=60,height=20,bg='grey',text="Pas d'image",font=('Consolas',10),fg='white')       # default_noimg est le label en haut à gauche quand il n'y a pas d'image
default_lbl = tk.Label(frame4,bg='#053f5e')                          # default_lbl est le label qui contiendra l'image par défaut sans ses changements
# ----------------------------------------------------------------------------------------------------------------------------------------


###################################################    AFFICHAGE DES ELEMENTS CREE    ####################################################

#   padx, pady met du padding extérieur sur l'axe x ou y
#   ipadx, ipady met du padding intérieur sur l'axe x ou y
#   expand étire le padding extérieur autant que possible
#   side définit le côté où sera placé l'élément
import_button.pack(padx=155,ipady=10,ipadx=10,pady=30)
modify_button.pack(ipady=10,ipadx=16,pady=30)
delete_button.pack(ipady=10,ipadx=20,pady=25)
lbl.pack(side=tk.TOP)

lbl_noimg.pack(pady=10,padx=10,expand=tk.YES)
lbl2.pack(side=tk.BOTTOM)
default_lbl.pack(side=tk.TOP)
default_noimg.pack(pady=10,padx=10,side=tk.TOP)


frame1.pack(fill=tk.BOTH,expand=tk.YES)
frame2.pack(padx=20,ipadx=20,ipady=20,side=tk.LEFT)
frame3.pack(padx=20,ipady=10,ipadx=10,side=tk.RIGHT)
frame4.pack(pady=20,padx=10)
separation2.pack(ipadx=160,pady=20)
frame5.pack(ipady=15,pady=20,expand=tk.YES)

separation1.pack(ipady=380,expand=tk.YES)
# ----------------------------------------------------------------------------------------------------------------------------------------


######################################################      CREATION DU MENU      ########################################################

menu = tk.Menu(master)

# sous-menu
#   argument 1 insique dans quele fenêtre est placé le menu
#   argument 2 rend le menu indétachable
file_menu = tk.Menu(menu, tearoff = 0)

# sous-menu en format cascade "Fichiers" dans le menu file
menu.add_cascade(label="Fichiers", menu=file_menu)

file_menu.add_command(label="Importer",accelerator='Ctrl+I',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=open_img)
file_menu.add_command(label="Enregistrer",accelerator='Ctrl+S',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
file_menu.add_command(label="Enregistrer sous",accelerator='Ctrl+Alt+S',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
file_menu.add_separator(background='#053f5e')
file_menu.add_command(label="Quitter",accelerator='Echap',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=master.destroy)


#sous-menu "Outils"
tools_menu = tk.Menu(menu, tearoff = 0)
tools_menu.add_command(label="Ajuster (RGB)",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
tools_menu.add_command(label="Rogner",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
tools_menu.add_command(label="Filtres",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
tools_menu.add_command(label="Dessiner",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
tools_menu.add_command(label="Pivoter",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
menu.add_cascade(label="Outils", menu=tools_menu)

#sous-menu "Aide"
help_menu = tk.Menu(menu, tearoff = 0)
help_menu.add_command(label="Prise en main",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=getting_started)
help_menu.add_command(label="Documentation",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700', command=doc)
help_menu.add_command(label="Code Source",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=source_code)
help_menu.add_command(label="Crédits",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=credit)
menu.add_cascade(label="Aide", menu=help_menu)

master.config(menu=menu)
# ----------------------------------------------------------------------------------------------------------------------------------------


######################################################    LANCEMENT DE LA FENETRE    #####################################################

master.mainloop()
