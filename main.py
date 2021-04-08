# ----------------------------------------------------------------------------------------------------------------------------------------
#
#                                                     _____  _           _        _____ _                       
#                                                    |  __ \| |         | |      / ____| |                      
#                                                    | |__) | |__   ___ | |_ ___| (___ | |__   __ _ _ __  _   _ 
#                                                    |  ___/| '_ \ / _ \| __/ _ \\___ \| '_ \ / _` | '_ \| | | |
#                                                    | |    | | | | (_) | || (_) |___) | | | | (_| | |_) | |_| |
#                                                    |_|    |_| |_|\___/ \__\___/_____/|_| |_|\__,_| .__/ \__, |
#                                                                                                  | |     __/ |
#                                                                                                  |_|    |___/ 
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


# importation des modules
import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import os
import time
import webbrowser as web


# création des fonctions
def open_img():
    """open_img est une fonction qui permet d'ouvrir et de sélectionner depuis l'explorateur de fichiers une image 
    puis de la charger dans la fenêtre"""
    global im                                   # permet à la variable im d'être aussi utilisée en dehors de cette fonction 
    
    # askopenfilename est une fonction de filedialog (module tkinter) qui permet de choisir un fichier depuis l'exporateur de fichier puis de récup son chemin d'accès 
    # 
    # ici on stocke le chemin d'accès dans la variable filename
    #   
    #   title sera le nom de la fenêtre de l'explorateur de fichier
    #   initialdir = os.getcwd() permet d'indiquer que l'explorateur de fichier doit s'ouvrir au chemin d'accès où se trouve l'utilisateur
    #   filetypes définit les extensions que l'utilisateur peut choisir
    
    filename = filedialog.askopenfilename(title="Ouvrir un fichier",initialdir= os.getcwd(),filetype=((".png","*.png"), (".jpg","*.jpg"), (".jfif","*.jfif"), ("Tous les fichiers","*")))
    try:                                                        # try fait comprendre à python qu'on essaye quelquechose
        im = Image.open(filename)           # ici on charge la photo sélectionnée et on la stocke dans im 
                                            #(le fichier choisit peut ne pas être dans un format accepté par Pillow) d'où le try:
        
        if im.height >= 20:                     # pas besoins de commenter ca sera modifié
            print('too big')                    # |
            im = im.resize((im.width,150))      # |
        if im.width >= 60:                      # |
            print('too large')                  # |
            im = im.resize((200,im.height))     # |
        photoim = ImageTk.PhotoImage(im)             # on charge l'image en élément ImageTk qu'on stocke dans im 
        default_noimg.destroy()                      # voir l.171

        default_lbl.configure(image=photoim,bg='grey')  # on rajoute l'image au label default_lbl 
        default_lbl.image = photoim                     #   (celui qui n'aura pas de modifications pour afficher à l'utilisateur son image de départ) 
        
    except:                                   # mot-clé de python, relié à try : si le code dans try rencontre une erreur alors 
                                              #     (sans doute à cause d'un mauvais format dans notre cas)
        print('erreur')                       #  on print 'erreur'

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


def code_source():
    """attribution : option "Code Source" du sous menu "Aide" (ligne 180)
    description : ouvre à l'aide du module webbrowser le lien vers ce dépot github"""
    
    web.open_new_tab('https://github.com/AXXIAR/PhotoShapy')

def destroy(event):
    """attribution : option "Quitter" du sous menu "Fichiers" (l. 167)
    description : affiche un message de confirmation pour quitter (OK/CANCEL). 
        Ferme le widget sur lequel l'utilisateur est si OK (une fenêtre étant considérée comme un widget cela la fermera),
        Annule si CANCEL"""
    
    # on stocke dans alerte une messagebox de type okcancel (présente un bouton OK et un bouton Cancel)
    #   title sera le titre de la fenêtre messagebox 
    #   message sera le texte qu'elle affiche
    alerte = messagebox.askokcancel(title="Attention", message="Es-tu sûr de vouloir quitter ?\n\n*Le travail non sauvegarder sera irrecupérable*")
    if alerte == True:              # alerte = True si l'utilisateur clique sur OK
        messagebox.showinfo(title='Au revoir',message="Merci de nous avoir utilisé :)") # on affiche une autre boîte avec du texte seulement pour dire au revoir
        time.sleep(1)                           # on met le programme en pause pendant 1 seconde
        event.widget.destroy()                  # on détruit le widget où à été appelée la fonction
    else:                           # alerte = False si l'utilisateur clique sur CANCEL
        pass                                    # on ne fait rien (la boîte est fermée par défaut) ... retour à l'application

def prise_en_main():
    """attribution : option "Prise En Main" du sous menu "Outils" (l. 185)
    description : --à venir--"""
    pem = tk.Toplevel(fen)
    pem.title('Prise en main')
    

#-----------  à garder pour plus tard  --------------

# def openwindow():          
#     """fonction qui créer une autre fenêtre avec un texte 'Nouvelle fenêtre' 
#     et qui aura la possibilité d'être fermée 
#     si on appuie sur la touche Echap lorsqu'on est dessus"""
    
#     top = tk.Toplevel()                                         # on créer une nouvelle fenêtre
#     label_2 = tk.Label(top, text = 'Nouvelle fenêtre')          # on y rajoute le texte : "Nouvelle fenêtre"
#     label_2.pack()                                              # on affiche le texte ^
#     top.bind('<Escape>', destroy)                               # lorsque la touche Echap est préssée, on appelle la fonction destroy() *qui ferme la fenêtre sur laquelle on est*

#-----------------------------------------------------



# création et paramètrage de notre fenêtre principale
fen = tk.Tk()                                           # stockage de la fenêtre principale dans la variable fen

fen.title("PhotoShapy")                                 # changement du titre de la fenêtre
fen.config(bg='#022c43')                                # changement de l'arrière plan 
fen.geometry("1850x900")                                # définition de sa taille par défaut à l'ouverture

fen.bind('<Escape>', destroy)                           # lorsque, sur la fenêtre, la touche Echap est préssée, on appelle la fonction destroy (l.80)

# création des différentes boîtes qui structure l'intérieur de la fenêtre
#   argument 1 : la fenêtre ou boîte dans laquelle on place notre nouvelle boîte
#   argument 2 : définition de la couleure d'arrière-plan de la boîte
frame1 = tk.Frame(fen,bg='#022c43')                     
frame2 = tk.Frame(frame1,bg='#053f5e')
frame3 = tk.Frame(frame1,bg='#053f5e')
frame4 = tk.Frame(frame2,bg='#053f5e')
frame5 = tk.Frame(frame2,bg='#053f5e')
separation1 = tk.Frame(frame1,bg='#ffd700')             # cette boîte et la suivante servent de séparations visuelles (les deux traits jaunes sur la fenêtre)
separation2 = tk.Frame(frame2,bg='#ffd700')


#création des éléments de notre éditeur d'images
bouton_charger = tk.Button(frame5, text = "Importer une photo",font=('Consolas'),bg="#115173",fg="#ffd700", command = display)
bouton_modifier = tk.Button(frame5, text = "Modifier la photo",font=('Consolas'),bg="#115173",fg="#ffd700")
bouton_supprimer = tk.Button(frame5, text = "Effacer la photo",font=('Consolas'),bg="#115173",fg="#ffd700")
lbl = tk.Label(frame3,width=130,height=43,bg='grey',text="Pas d'image",font=('Consolas'),fg='white')
default_noimg = tk.Label(frame4, width=60,height=20,bg='grey',text="Pas d'image",font=('Consolas',10),fg='white')
default_lbl = tk.Label(frame4,bg='#053f5e')

# on affiche les éléments créés
bouton_charger.pack(padx=155,ipady=10,ipadx=10,pady=30)
bouton_modifier.pack(ipady=10,ipadx=16,pady=30)
bouton_supprimer.pack(ipady=10,ipadx=20,pady=25)
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

# créer un menu 
menu = tk.Menu(fen)

# sous-menu "Fichiers"
file_menu = tk.Menu(menu, tearoff = 0)
file_menu.add_command(label="Importer",accelerator='Ctrl+I',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=display)
file_menu.add_command(label="Enregistrer",accelerator='Ctrl+S',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
file_menu.add_command(label="Enregistrer sous",accelerator='Ctrl+Alt+S',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
file_menu.add_separator(background='#053f5e')
file_menu.add_command(label="Quitter",command=fen.destroy,accelerator='Echap',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
menu.add_cascade(label="Fichiers", menu=file_menu)

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
aide_menu.add_command(label="Documentation",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
aide_menu.add_command(label="Code Source",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=code_source)
aide_menu.add_command(label="Crédits",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
menu.add_cascade(label="Aide", menu=aide_menu)

fen.config(menu=menu)


# on "lance" notre fenêtre
fen.mainloop()
