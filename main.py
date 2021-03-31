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
#           
#
#
#                                                           🔄 En cours de développement 🔄
# ----------------------------------------------------------------------------------------------------------------------------------------


# importations modules
import tkinter as tk                                       
from tkinter import filedialog
from PIL import Image,ImageTk
import os

# création de nos fonctions

def display():
    global im
    filename = filedialog.askopenfilename(title="Ouvrir un fichier",initialdir= os.getcwd(),filetype=((".png","*.png"), (".jpg","*.jpg"), (".jfif","*.jfif"), ("Tous les fichiers","*")))
    try:       
        im = Image.open(filename)
        if im.height >= 700:                    
            print('too big')
            im = im.resize((im.width,700))
        if im.width >= 1000:             
            print('too large')
            im = im.resize((1000,im.height))
        im = im.resize((500,im.height))
        im = im.resize((im.width,500))
        photoim = ImageTk.PhotoImage(im)
        lbl.configure(image=photoim)
        lbl.image = photoim
    except NameError:
        print(NameError)

def rotate():
    """fonction qui vérifie qu'une image est affichée et si oui qui la tourne de 45° à gauche puis la réaffiche"""
    global photoim,im
    if 'im' in globals():       # on vérifie si la variable existe dans les variables globales (en gros si on a une image ouverte dans la fenêtre)
        im = im.rotate(45,expand=True)
        photoim = ImageTk.PhotoImage(im)
        lbl.configure(image = photoim)
        lbl.image = photoim
    else:
        print('Aucune image')


def destroy(event):
    """fonction qui détruit la fenêtre sur laquelle tu es:"""
    event.widget.destroy()   
    print(f'la fenêtre :  {event.widget} a été fermée\n')

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
fen.geometry("1090x720")                                    

fen.bind('<Escape>', destroy)


leftframe = tk.Frame(padx=5,pady=5)

# création des éléments de notre éditeur d'images
bouton_rotate = tk.Button(leftframe, text = "Tourner la photo", command = rotate)           

bouton_display = tk.Button(leftframe, text = "Ouvrir une photo", command = display)     

lbl = tk.Label(leftframe,bg='#022c43')

# on affiche les éléments créés
bouton_rotate.grid(row=0,column=0)
bouton_display.grid(row=0,column=1)
lbl.grid(row=1)

leftframe.pack(expand=tk.YES)

# on "lance" notre fenêtre
fen.mainloop()
