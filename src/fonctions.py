###########  IMPORTATION DES MODULES  ###########
import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import PIL
import os
import webbrowser as web
from toplevels import *
import datetime as dt
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS GLOBALES       #########################################

def dest(*args):
    """attributions : 
    description : parcours chaque widget donnés lors de son appel et le détruit.
                    permet de détruire plusieurs éléments plus facilement et rapidement
    paramètres  : - *args => l'étoile indique que la fonction prend autant de paramètre que l'on veut
                                args sera alors un tuple contenant tous les paramètres donnés lors de l'appel de la fonction"""
    for widget in args:
        widget.destroy()
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS MODIFIANT L'INTERFACE       #########################################

def f_close(event):
    """attributions : fonction 'close()' du fichier 'master_window.py'
    description : affiche un message de confirmation pour quitter (OK/CANCEL). 
        si OK, Ferme le widget sur lequel l'utilisateur est 
        si CANCEL est cliqué, Annule
    paramètres  : - event => event est le widget sur lequel se situe l'utilisateur à l'appel de la fonction"""
    
    # on stocke dans alerte une messagebox de type okcancel (présente un bouton OK et un bouton Cancel)
    #   title sera le titre de la fenêtre messagebox 
    #   message sera le texte qu'elle affiche
    alerte = messagebox.askokcancel(title="Attention", message="Es-tu sûr de vouloir quitter ?\n\n*Le travail non sauvegardé sera irrecupérable*")
    if alerte == True:              # alerte = True si l'utilisateur clique sur OK
        messagebox.showwarning(title='Au revoir',message="Merci de nous avoir utilisé :)") # on affiche une autre boîte avec du texte seulement pour dire au revoir
        event.widget.destroy()                  # on détruit le widget où à été appelée la fonction
    else:                           # alerte = False si l'utilisateur clique sur CANCEL
        pass                                    # on ne fait rien (la boîte est fermée par défaut) ... retour à l'application

def f_modify(default_lbl,default_noimg,lbl,import_button,modify_button,delete_button,frame2,frame4,frame5,master):
    """attributions : fonction 'modify()' du fichier 'master_window.py'
    description : supprime les boutons Importer,Modifier,Effacer et les remplace par les boutons permettant de modifier la photo
    paramètres  : tous les paramètres pris sont des widgets créés dans 'master_wndow.py' 
                    sur lesquels ont va faire des modifications"""
    global back,filters,crop,rotate  # on rend global les variables qui vont stocker les nouveaux boutons, pour éviter les problèmes 

    dest(import_button,modify_button,delete_button)     # on détruit les boutons de l'accueil
    
                                                                                                    # ici lambda nous permet de passer des arguments à la fonction
                                                                                                    #   qu'on associe au bouton
    back = tk.Button(frame5, text = "<",font=('Consolas',20,'bold'),bg="#ffd700",fg="#115173",command=lambda:f_back_menu(default_lbl,default_noimg,lbl,frame2,frame4,frame5,master))

    crop = tk.Button(frame5, text = "Rogner",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_crop_window(master,lbl))
    rotate = tk.Button(frame5, text = "Pivoter",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_rotate_window(master,lbl))
    filters = tk.Button(frame5, text = "Filtres",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_filters_window(master,lbl))

    back.pack(side=tk.BOTTOM,pady=10,ipadx=30)
    crop.pack(ipadx=65,ipady=5,pady=10)
    rotate.pack(ipadx=60,ipady=5,pady=10)
    filters.pack(ipadx=60,ipady=5,pady=10)

def f_back_menu(default_lbl,default_noimg,lbl,frame2,frame4,frame5,master):
    """attributions : bouton '<' dans la fonction f_modify() / l.57
    description : fait l'inverse de 'f_close()' à savoir : supprimer les boutons de modifications des photos pour remettre les boutons de l'accueil"""
    global import_button, modify_button, delete_button
    global back,filters,crop,rotates
    
    # ici on va chercher à éviter une erreur qui a lieue à l'ouverture parceque 
    # les boutons bac, filters, crop .... n'existe pas encore
    try:
        dest(back,filters,crop,rotate)
    except:
        pass
        
    import_button = tk.Button(frame5, text = "Importer une photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_open_img(default_lbl,default_noimg,lbl))
    modify_button = tk.Button(frame5, text = "Modifier la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_modify(default_lbl,default_noimg,lbl,import_button,modify_button,delete_button,frame2,frame4,frame5,master))
    delete_button = tk.Button(frame5, text = "Effacer la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=lambda:f_delete_img(default_lbl,default_noimg,lbl))
    import_button.pack(padx=155,ipady=10,ipadx=10,pady=30)
    modify_button.pack(ipady=10,ipadx=16,pady=30)
    delete_button.pack(ipady=10,ipadx=20,pady=25)
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS POUR OUVRIR/EFFACER L'IMAGE       #########################################

def f_open_img(default_lbl,default_noimg,lbl):
    """attributions : bouton 'Importer une image' du fichier 'master_window.py' (l.afpt)
    description : permet d'ouvrir et de sélectionner depuis l'explorateur de fichiers une image puis de la charger dans la fenêtre"""
    global default_im, im                         # permet à la variable default_im d'être aussi utilisée en dehors de cette fonction 
    
    # askopenfilename est une fonction de filedialog (module tkinter) qui permet de choisir un fichier depuis l'exporateur de fichier puis de récup son chemin d'accès 
    # 
    # ici on stocke le chemin d'accès dans la variable filename
    #   
    #   title sera le nom de la fenêtre de l'explorateur de fichier
    #   initialdir = os.getcwd() permet d'indiquer que l'explorateur de fichier doit s'ouvrir au chemin d'accès où se trouve l'utilisateur
    #   filetypes définit les extensions que l'utilisateur peut choisir
    
    filename = filedialog.askopenfilename(title="Ouvrir un fichier",initialdir= os.getcwd(),filetype=((".png","*.png"), (".jpg","*.jpg"), (".jfif","*.jfif"), ("Tous les fichiers","*")))
    
    try:    # le fichier choisit par l'utilisateur pourrait être dans un format non accepté par Pillow d'où le try:
        default_im = Image.open(filename)   # default_im est l'image qui ne subira pas les modifications de sorte à avoir un aperçu de l'image de base

        # Ici on va venir réajuster la taille de l'image pour qu'elle tienne dans le label default_lbl
        if default_im.width > 420:
            diff = default_im.width - 420 
            if default_im.height > diff:
                default_im = default_im.resize((420 , default_im.height - diff))
            else:
                default_im = default_im.resize((420 , default_im.height))
        if default_im.height > 300:
            diff = default_im.height - 300
            if default_im.width > diff:
                default_im= default_im.resize((default_im.width - diff , 300))
            else:
                default_im= default_im.resize((default_im.width , 300))

        if default_im.width <= 150:
            diff = 150 - default_im.width
            default_im = default_im.resize((150 , default_im.height + diff))
        if default_im.height <= 30:
            diff = 30 - default_im.height
            default_im = default_im.resize((default_im.width + diff , 30))

        default_noimg.pack_forget()        # on enlève le label avec marqué "Pas d'image"

        default_photoim = ImageTk.PhotoImage(default_im)             # on charge l'image en élément ImageTk qu'on stocke dans default_photoim
                
        default_lbl.configure(image=default_photoim,bg='grey')  # on rajoute la photoimage au label default_lbl 
        default_lbl.image = default_photoim                  
        
#####################################################

        im = Image.open(filename)           # ici on charge la photo sélectionnée et on la stocke dans 'im'

        # on vient redimensionner l'image pour qu'elle tienne dans le label 'lbl'
        if im.width > 1170:
            diff = im.width - 1170
            if im.height > diff:
                im = im.resize((1170 , im.height - diff))
            else:
                im = im.resize((1170 , int(im.height/2)))
        if im.height > 820:
            diff = im.height - 820
            if im.width > diff:
                im = im.resize((im.width - diff , 820))
            else:
                im = im.resize((int(im.width/2) , 820))

        
        if im.width <= 300:
            diff = 300 - im.width
            im = im.resize((300 , im.height + diff))
        if im.height <= 60:
            diff = 60 - im.height
            im = im.resize((im.width + diff , 60))

        im.filename = filename
        photoim = ImageTk.PhotoImage(im)             # on charge l'image en élément photoImage du module ImageTk qu'on stocke dans 'photoim'
                
        lbl.configure(image=photoim,bg='grey',height=im.height+10,width=im.width+10,text="")  # on rajoute la photoimage au label 'slbl' 
        lbl.image = photoim

        
    except PIL.UnidentifiedImageError:  # en cas d'erreur du à une mauvaise extension, on l'indique à l'utilisateur via une alerte
        messagebox.showwarning('Erreur','Le format choisi est incorrecte')

    except AttributeError:      # erreur qui semble être levée quand on annule l'importation d'une image
        pass

    except Exception as err:    # en cas d'autres erreur, on l'envoie dans le fichier logs.txt
                                #   ainsi l'utilisateur peut accèder à un suivi des erreurs qui auraient eu lieu

        with open('logs.txt','r') as f:     # on ouvre 'logs.txt' en lecture et on récupère le nombre de lignes
            lines = 0
            for line in f:
                lines+=1
            f.close()

        if lines > 100:                     # si il y'a déjà 100 lignes d'écrites, on ouvre en écriture 
                                            #   puis on referme, cela va écraser tout le contenu déjà présent
            with open('logs.txt','w') as temp:
                temp.close()

        with open('logs.txt','a') as f:         # enfin on ouvre en mode append 
            d = dt.datetime.now().strftime("%d/%m/%Y  %H:%M")   # on récupère la date sous ce format : 01/01/2000 12:00
                                                                #   puis on indique la date et l'erreur et on ferme le fichier
            f.write(f'[{d}] Error on open_img() : {err}\n------------------------------------------------------------------------------------------------------------------------------------------\n\n')
            f.close()


def f_delete_img(default_lbl,default_noimg,lbl):
    """attributions : bouton 'Effacer la photo' (l.afpt) et l.afpt du fichier 'master_window.py'
    description : permet de supprimer les images, et de remettre un label 'Pas d'image' """
    global default_im,im
    if 'default_im' in globals() and 'im' in globals():     # on vérifie que ces deux variables existent dans les variables globales (= si une image à étée importée)
        
        default_noimg.pack(pady=10,padx=10,side=tk.TOP)
        
        default_lbl.configure(image='',bg='#053f5e')  # on rajoute l'image au label default_lbl
        lbl.configure(image='',width=130,height=43,bg='grey',text="Pas d'image",font=('Consolas'),fg='white')
        del default_im,im

    else:       # si aucune image n'a étée importée, on ne peut pas la supprimer donc on prévient l'utilisateur
        messagebox.showwarning('Erreur',"Pas d'image")
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS OUVRANT LES FENETRES DE MODIF D'IMAGE       #########################################

def f_rotate_window(master,lbl):
    """attributions : bouton 'Pivoter' (l.afpt)
    description : appelle la fonction 't_rotate_window()' du fichier 'toplevels.py'
                    mais seulement si une image à étée importée"""
    global default_im,im
    if 'im' and 'default_im' in globals():
        t_rotate_window(master,lbl,im)
    else:
        messagebox.showwarning('Erreur',"Pas d'image")

def f_filters_window(master,lbl):
    """attributions : bouton 'Filtres' (l.afpt)
    description : appelle la fonction 't_filters_window()' du fichier 'toplevels.py'
                    mais seulement si une image à étée importée"""
    global default_im,im
    if 'im' and 'default_im' in globals():
        t_filters_window(master,lbl,im)
    else:
        messagebox.showwarning('Erreur',"Pas d'image")

def f_crop_window(master,lbl):
    """attributions : bouton 'Rogner' (l.afpt)
    description : appelle la fonction 't_crop_window()' du fichier 'toplevels.py'
                    mais seulement si une image à étée importée"""
    global default_im,im
    if 'im' and 'default_im' in globals():
        t_crop_window(master,lbl,im)
    else:
        messagebox.showwarning('Erreur',"Pas d'image")
# ----------------------------------------------------------------------------------------------------------------------------------------



####################################      FONCTIONS MENU AIDE       #########################################

def f_getting_started(masterx,mastery):
    """attributions : option "Prise En Main" du sous menu "Outils" (l.afpt)
    description : demande à l'utilisateur s'il veut ouvrir l'aide en ligne (sur le site) ou sur l'appliction
                    puis execute ce que veut l'utilisateur
    paramètres  : - masterx => largeur de la fenêtre au moment de l'appelle de la fonction
                  - mastery => hauteur de la fenêtre au moment de l'appelle de la fonction"""
    alerte = messagebox.askyesno(title="Ouverture", message="Ouvrir en ligne ?")
    if alerte == True:              # alerte = True si l'utilisateur clique sur Yes
        web.open_new_tab('https://axxiar.github.io/PhotoShapy/')
    else:                           # alerte = False si l'utilisateur clique sur No
        pem_master = tk.Tk()
        pem_master.title('Prise en main')
        pem_master.geometry(f'{masterx-30}x{mastery-30}')   # on ajuste la taille de la fenêtre en fonction de la taille de la fenêtre récupérée en paramètre
        pem_master.geometry("+40+60")
        pem_master.config(bg='#022c43')
        pem_master.mainloop()


def source_code():
    """attributions : option "Code Source" du sous menu "Aide" (ligne afpt.)
    description : ouvre à l'aide du module webbrowser le lien vers le dépot github"""
    
    web.open_new_tab('https://github.com/AXXIAR/PhotoShapy')
    

def f_doc(masterx,mastery):
    """attributions : option "Prise En Main" du sous menu "Outils" (l.afpt)
    description : demande à l'utilisateur s'il veut ouvrir l'aide en ligne (sur le site) ou sur l'appliction
                    puis execute ce que veut l'utilisateur
    paramètres  : - masterx => largeur de la fenêtre au moment de l'appelle de la fonction
                  - mastery => hauteur de la fenêtre au moment de l'appelle de la fonction"""
    alerte = messagebox.askyesno(title="Ouverture", message="Ouvrir en ligne ?")
    if alerte == True:              # alerte = True si l'utilisateur clique sur Yes
        web.open_new_tab('https://axxiar.github.io/PhotoShapy/')
    else:                           # alerte = False si l'utilisateur clique sur No
        docu_master = tk.Tk()
        docu_master.title('Prise en main')
        docu_master.geometry(f'{masterx-30}x{mastery-30}')  # on ajuste la taille de la fenêtre en fonction de la taille de la fenêtre récupérée en paramètre
        docu_master.geometry("+40+60")
        docu_master.config(bg='#022c43')
        docu_master.mainloop()


def f_credit(masterx,mastery):
    """attributions : option "Prise En Main" du sous menu "Outils" (l.afpt)
    description : ouvre la page des crédits (dans l'application)
    paramètres  : - masterx => largeur de la fenêtre au moment de l'appelle de la fonction
                  - mastery => hauteur de la fenêtre au moment de l'appelle de la fonction"""
    credit_master = tk.Tk()
    credit_master.title('Prise en main')
    credit_master.geometry(f'{masterx-30}x{mastery-30}')     # on ajuste la taille de la fenêtre en fonction de la taille de la fenêtre récupérée en paramètre
    credit_master.geometry("+40+60")
    credit_master.config(bg='#022c43')
    credit_master.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------