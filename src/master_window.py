

# afpt = à faire plus tard
# l. = ligne

###########  IMPORTATION DES MODULES  ###########
import tkinter as tk
from fonctions import *
# ----------------------------------------------------------------------------------------------------------------------------------------


######################################################    CREATION DES FONCTIONS    #####################################################
def rotate_window():
    """attributions : bouton 'Pivoter' l. afpt
    description : appelle la fonction 'f_rotate_window()' du fichier 'fonctions.py'
    """
    f_rotate_window(master,lbl)

def filters_window():
    """attributions : bouton 'Filtres' l. afpt
    description : appelle la fonction 'f_filters_window()' du fichier 'fonctions.py'
    """
    f_filters_window(master,lbl)

def crop_window():
    """attributions : bouton 'Rogner' l. afpt
    description : appelle la fonction 'f_crop_window()' du fichier 'fonctions.py'
    """
    f_crop_window(master,lbl)

def modify():
    """attributions : bouton 'Modifier une photo' l. afpt
    description : appelle la fonction 'f_modify()' du fichier 'fonctions.py'
    """
    f_modify(default_lbl,default_noimg,lbl,import_button,modify_button,delete_button,frame2,frame4,frame5,master)

def open_img():
    """attributions : bouton 'Importer une photo' l. afpt
    description : appelle la fonction 'f_open_img()' du fichier 'fonctions.py'
    """
    f_open_img(default_lbl,default_noimg,lbl)

def delete_img():
    """attributions : bouton 'Effacer la photo' l. afpt
    description : appelle la fonction 'f_delete_img()' du fichier 'fonctions.py'
    """
    f_delete_img(default_lbl,default_noimg,lbl)


def close(event):
    """attributions : option "Quitter" du sous menu "Fichiers" (l.afpt)
    description : appelle la fonction 'f_close()' du fichier 'fonctions.py'
    paramètres  :  - event => event est le widget sur lequel l'utilisateur est à l'appel de la fonction"""
    f_close(event)

def getting_started():
    """attributions : option "Prise en main" du sous menu "Aide" l.afpt
    description : récupère la largeur et hauteur de l'écran de l'utilisateur, puis appelle la fonction 'f_getting_started()
                    du fichier 'fonctions.py' en lui passant en argument la largeur et hauteur de la fenêtre"""
    masterx=master.winfo_width()
    mastery=master.winfo_height()
    f_getting_started(masterx,mastery)
    

def doc():
    """attributions : option "Documentation" du sous menu "Aide" l.afpt
    description : récupère la largeur et hauteur de l'écran de l'utilisateur, puis appelle la fonction 'f_doc()'
                    du fichier 'fonctions.py' en lui passant en argument la largeur et hauteur de la fenêtre"""
    masterx=master.winfo_width()
    mastery=master.winfo_height()
    f_doc(masterx,mastery)


def credit():
    """attributions : option "Credits" du sous menu "Aide" l.afpt
    description : récupère la largeur et hauteur de l'écran de l'utilisateur, puis appelle la fonction 'f_credit()'
                    du fichier 'fonctions.py' en lui passant en argument la largeur et hauteur de la fenêtre"""
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

master.bind('<Escape>', close)                           # lorsque la touche Echap est préssée, on appelle la fonction close cf. (l.afpt)
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
separation2 = tk.Frame(frame2,bg='#ffd700')             #                                        //
# ----------------------------------------------------------------------------------------------------------------------------------------


################################################    CREATION DES BOUTONS ET LABELS   #####################################################

#   argument 1 : la fenêtre ou boîte dans laquelle on place notre bouton
#   argument 2 : le texte du bouton
#   argument 3 : la police de ce texte
#   argument 4 : la couleur d'arrière-plan
#   argument 5 : la couleur d'avant-plan (ici le texte)
#   argument 6 : la commande attribuée qui est appelée lors du clic sur le bouton
import_button = tk.Button(frame5, text = "Importer une photo",font=('Consolas'),bg="#115173",fg="#ffd700", command = open_img)
modify_button = tk.Button(frame5, text = "Modifier la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=modify)
delete_button = tk.Button(frame5, text = "Effacer la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=delete_img)

# lbl est le label central contenant l'image qui subira les modifications
lbl = tk.Label(frame3,width=130,height=43,bg='grey',text="Pas d'image",font=('Consolas'),fg='white')              

# default_noimg est le label en haut à gauche affiché lorsqu'il n'y a pas d'image
default_noimg = tk.Label(frame4, width=60,height=20,bg='grey',text="Pas d'image",font=('Consolas',10),fg='white')
# default_lbl est le label en haut à gauche affiché lorsqu'il y a une image. Celle-ci ne subira pas de modification et montre sa photo de départ à l'utilisateur
default_lbl = tk.Label(frame4,bg='#053f5e')                          
# ----------------------------------------------------------------------------------------------------------------------------------------


###################################################    AFFICHAGE DES ELEMENTS CREES    ####################################################

# Quelques paramètres de la fonction .pack() [fontcion qui permet d'impacter les éléments ci dessus sur notre fenêtre] :
#
#   padx, pady met du padding extérieur sur l'axe x ou y
#   ipadx, ipady met du padding intérieur sur l'axe x ou y
#   expand permet au widget concerné de s'étirer autant qu'il a de place
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

# sous-menu (en format cascade) "Fichiers" dans le menu file
menu.add_cascade(label="Fichiers", menu=file_menu)


#   label est le nom de "l'option" 
#   accelerator est un texte qui s'affiche juste à droite du label (ici on l'utilise pour indiquer les raccourcis)
#   background et foreground sont les couleurs d'arrière et avant-plan (le texte) par défaut
#   background et foreground sont les couleurs d'arrière et avant-plan (le texte) lorsqu'on passe la souris dessus
file_menu.add_command(label="Importer",accelerator='Ctrl+I',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=open_img)
file_menu.add_command(label="Enregistrer",accelerator='Ctrl+S',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
file_menu.add_command(label="Enregistrer sous",accelerator='Ctrl+Alt+S',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
file_menu.add_separator(background='#053f5e')   # le separator est une simple ligne horizontale
file_menu.add_command(label="Quitter",accelerator='Echap',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=master.destroy)


#sous-menu "Outils"
tools_menu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label="Outils", menu=tools_menu)

tools_menu.add_command(label="Ajuster (RGB)",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
tools_menu.add_command(label="Rogner",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=crop_window)
tools_menu.add_command(label="Filtres",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=filters_window)
tools_menu.add_command(label="Pivoter",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=rotate_window)


#sous-menu "Aide"
help_menu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label="Aide", menu=help_menu)

help_menu.add_command(label="Prise en main",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=getting_started)
help_menu.add_command(label="Documentation",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700', command=doc)
help_menu.add_command(label="Code Source",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=source_code)
help_menu.add_command(label="Crédits",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=credit)


master.config(menu=menu)    # on modifie le master pour lui ajouter notre menu
# ----------------------------------------------------------------------------------------------------------------------------------------


######################################################    LANCEMENT DE LA FENETRE    #####################################################

master.mainloop()
