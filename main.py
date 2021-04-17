# ----------------------------------------------------------------------------------------------------------------------------------------
#
#                                                ______  _                     ______ _                       
#                                               (_____ \| |           _       / _____) |                      
#                                                _____) ) |__   ___ _| |_ ___( (____ | |__  _____ ____  _   _ 
#                                               |  ____/|  _ \ / _ (_   _) _ \\____ \|  _ \(____ |  _ \| | | |
#                                               | |     | | | | |_| || || |_| |____) ) | | / ___ | |_| | |_| |
#                                               |_|     |_| |_|\___/  \__)___(______/|_| |_\_____|  __/ \__  |
#                                                                                                |_|   (____/
# 
#
#   Projet NSI 1ère
#   Lycée Sophie Germain
#   Milo GARDIES & Alexis GALOPIN, classe de 1G6
#   
#   PhotoShapy est un éditeur d'images écrit entièrement en Python
#   Modules utilisées : 
#         - PIL (édition d'images)
#         - Tkinter (interface graphique)
#         - Os (interactions avec le système d'exploitation)
#         - Time ()
#         - Webbrowser (recherches sur le web)
#
#
#                                                           🔄 En cours de développement 🔄
# ----------------------------------------------------------------------------------------------------------------------------------------

 # afpt = à faire plus tard
# l. = ligne

###########  importation des modules  ###########
import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import os
import time
import webbrowser as web
# ----------------------------------------------------------------------------------------------------------------------------------------


######################################################    CREATION DES FONCTIONS    #####################################################
def open_img():
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

def delete_img():
    global im
    global default_noimg
    if 'im' in globals():
        default_noimg = tk.Label(frame4, width=60,height=20,bg='grey',text="Pas d'image",font=('Consolas',10),fg='white')
        default_noimg.pack(pady=10,padx=10,side=tk.TOP)
        
        default_lbl.configure(image='',bg='#053f5e')  # on rajoute l'image au label default_lbl
    else:
        print("pas d'image")


# def rotate():
#     """fonction qui vérifie qu'une image est affichée et si oui qui la tourne de 45° à gauche puis la réaffiche"""
#     global photoim,im
#     if 'im' in globals():       # on vérifie si la variable existe dans les variables globales (en gros si on a une image ouverte dans la fenêtre)
#         im = im.rotate(45,expand=True)
#         photoim = ImageTk.PhotoImage(im)
#         lbl.configure(image = photoim)
#         lbl.image = photoim
#     else:
#         print('Aucune image')


def escape(event):
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

def prise_en_main():
    """attribution : option "Prise En Main" du sous menu "Outils" (l.afpt)
    description : --à venir--"""
    alerte = messagebox.askyesno(title="Ouverture", message="Ouvrir en ligne ?")
    if alerte == True:              # alerte = True si l'utilisateur clique sur Yes
        web.open_new_tab('https://axxiar.github.io/PhotoShapy/')
    else:                           # alerte = False si l'utilisateur clique sur No
        pem_master = tk.Tk()
        pem_master.title('Prise en main')
        pem_master.geometry(f'{master.winfo_width()-30}x{master.winfo_height()-30}')
        pem_master.geometry("+40+60")
        pem_master.config(bg='#022c43')
        master.destroy()
        pem_master.mainloop()


def code_source():
    """attribution : option "Code Source" du sous menu "Aide" (ligne 180)
    description : ouvre à l'aide du module webbrowser le lien vers ce dépot github"""
    
    web.open_new_tab('https://github.com/AXXIAR/PhotoShapy')
    

def docu():
    #- renvoyer sur le site (docu à créer)
    """bloub"""
    alerte = messagebox.askyesno(title="Ouverture", message="Ouvrir en ligne ?")
    if alerte == True:              # alerte = True si l'utilisateur clique sur Yes
        web.open_new_tab('https://axxiar.github.io/PhotoShapy/')
    else:                           # alerte = False si l'utilisateur clique sur No
        docu_master = tk.Tk()
        docu_master.title('Prise en main')
        docu_master.geometry(f'{master.winfo_width()-30}x{master.winfo_height()-30}')
        docu_master.geometry("+40+60")
        docu_master.config(bg='#022c43')
        master.destroy()
        docu_master.mainloop()


def credit():
    credit_master = tk.Tk()
    credit_master.title('Prise en main')
    credit_master.geometry(f'{master.winfo_width()-30}x{master.winfo_height()-30}')
    credit_master.geometry("+40+60")
    credit_master.config(bg='#022c43')
    master.destroy()
    credit_master.mainloop()

# ----------------------------------------------------------------------------------------------------------------------------------------


####################################      CREATION ET PARAMETRAGE DE LA FENETRE PRINCIPALE       #########################################

master = tk.Tk()                                           # stockage de la fenêtre principale dans la variable master

master.title("PhotoShapy")                                 # changement du titre de la fenêtre
master.config(bg='#022c43')                                # changement de l'arrière plan 
master.geometry("1850x900")                                # définition de sa taille par défaut à l'ouverture
master.geometry("+25+25")                                  # définition de sa position par défaut à l'ouverture (Décalage_Top ; Décalage_Left)

master.bind('<Escape>', escape)                           # lorsque, sur la fenêtre, la touche Echap est préssée, on appelle la fonction destroy (l.afpt)
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
modify_button = tk.Button(frame5, text = "Modifier la photo",font=('Consolas'),bg="#115173",fg="#ffd700")
delete_button = tk.Button(frame5, text = "Effacer la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=delete_img)
lbl = tk.Label(frame3,width=130,height=43,bg='grey',text="Pas d'image",font=('Consolas'),fg='white')                    # lbl est un label qui contiendra l'image sur laquelle on verra les modifications
default_noimg = tk.Label(frame4, width=60,height=20,bg='grey',text="Pas d'image",font=('Consolas',10),fg='white')       # default_noimg est le label par défaut quand il n'y a pas d'image
default_lbl = tk.Label(frame4,bg='#053f5e')         # default_lbl est le label qui contiendra l'image par défaut sans ses changements
# ----------------------------------------------------------------------------------------------------------------------------------------


###################################################    AFFICHAGE DES ELEMENTS CREE    ####################################################

#   padx, pady met du padding extérieur sur l'axe x ou y
#   ipadx, ipady met du padding intérieur sur l'axe x ou y
#   expand étire le padding extérieur autant que possible
#   side définit le côté où sera placé l'élément
import_button.pack(padx=155,ipady=10,ipadx=10,pady=30)
modify_button.pack(ipady=10,ipadx=16,pady=30)
delete_button.pack(ipady=10,ipadx=20,pady=25)
lbl.pack(pady=10,padx=10,expand=tk.YES)
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
file_menu.add_command(label="Quitter",command=master.destroy,accelerator='Echap',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')


#sous-menu "Outils"
outils_menu = tk.Menu(menu, tearoff = 0)
outils_menu.add_command(label="Ajuster (RGB)",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
outils_menu.add_command(label="Rogner",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
outils_menu.add_command(label="Filtres",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
outils_menu.add_command(label="Dessiner",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
outils_menu.add_command(label="Pivoter",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
menu.add_cascade(label="Outils", menu=outils_menu)

#sous-menu "Aide"
aide_menu = tk.Menu(menu, tearoff = 0)
aide_menu.add_command(label="Prise en main",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=prise_en_main)
aide_menu.add_command(label="Documentation",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700', command=docu)
aide_menu.add_command(label="Code Source",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=code_source)
aide_menu.add_command(label="Crédits",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=credit)
menu.add_cascade(label="Aide", menu=aide_menu)

master.config(menu=menu)
# ----------------------------------------------------------------------------------------------------------------------------------------


######################################################    LANCEMENT DE LA FENETRE    #####################################################

master.mainloop()