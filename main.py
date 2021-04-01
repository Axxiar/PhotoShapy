# ----------------------------------------------------------------------------------------------------------------------------------------
#                                                ______  _                     ______ _                       
#                                               (_____ \| |           _       / _____) |                      
#                                                _____) ) |__   ___ _| |_ ___( (____ | |__  _____ ____  _____
#                                               |  ____/|  _ \ / _ (_   _) _ \\____ \|  _ \(____ |  _ \| ___ |
#                                               | |     | | | | |_| || || |_| |____) ) | | / ___ | |_| | ____|
#                                               | |     |_| |_|\___/  \__)___(______/|_| |_\_____|  __/|_____)
#                                               |_|                                              |_|
# 
#
#   Projet NSI 1ère
#   Lycée Sophie Germain
#   Milo GARDIES & Alexis GALOPIN, classe de 1G6
#   
#   PhotoShape est un éditeur d'images écrit entièrement en Python
#   Modules utilisées : 
#         - PIL (édition d'images)
#         - Tkinter (interface graphique)
#         - Os (interactions avec le système d'exploitation)
#         - Time ()
#           
#
#
#                                                           🔄 En cours de développement 🔄
# ----------------------------------------------------------------------------------------------------------------------------------------


# importations modules
import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import os
import time

# création de nos fonctions

def display():
    global im
    filename = filedialog.askopenfilename(title="Ouvrir un fichier",initialdir= os.getcwd(),filetype=((".png","*.png"), (".jpg","*.jpg"), (".jfif","*.jfif"), ("Tous les fichiers","*")))
    try:       
        im = Image.open(filename)
        if im.height >= 20:                    
            print('too big')
            im = im.resize((im.width,150))
        if im.width >= 60:             
            print('too large')
            im = im.resize((200,im.height))
        photoim = ImageTk.PhotoImage(im)
        default_noimg.destroy()

        default_lbl.configure(image=photoim,bg='grey')
        default_lbl.image = photoim
    except:
        print('erreur')

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


def destroy(event):
    """fonction qui détruit la fenêtre sur laquelle tu es:"""
    alerte = messagebox.askokcancel(title="Attention", message="Es-tu sûr de vouloir quitter ?\n\n*Le travail non sauvegarder sera irrecupérable*")
    if alerte == True:
        messagebox.showinfo(title='Au revoir',message="Merci de nous avoir utilisé :)")
        time.sleep(1)
        event.widget.destroy()
    else:
        pass
    

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
fen = tk.Tk()                  

fen.title("PhotoShape")            
fen.config(bg='#022c43')
fen.geometry("1850x900")                                    

fen.bind('<Escape>', destroy)

frame1 = tk.Frame(fen,bg='#022c43')
frame2 = tk.Frame(frame1,bg='#053f5e')
frame3 = tk.Frame(frame1,bg='#053f5e')
frame4 = tk.Frame(frame2,bg='#053f5e')
frame5 = tk.Frame(frame2,bg='#053f5e')
separation1 = tk.Frame(frame1,bg='#ffd700')
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


# on "lance" notre fenêtre
fen.mainloop()
