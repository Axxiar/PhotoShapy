import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import os
import time
import webbrowser as web


def t_rotate_window(master,lbl,im):

    def rotatest(side,im):
        global photoim

        if side == 'left':
            im = im.transpose(Image.ROTATE_90)
        elif side == 'right':
            im = im.transpose(Image.ROTATE_270)
        photoim = ImageTk.PhotoImage(im)
        lbl.configure(image=photoim)
        lbl.image = photoim


    def flip(orientation,im):
        global photoim

        if orientation == 'horizontal':
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 'vertical':
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
        photoim = ImageTk.PhotoImage(im)
        lbl.configure(image=photoim)
        lbl.image = photoim
    # ----------------------------------------------------------------------------------------------------------------------------------------


    ####################################      CREATION ET PARAMETRAGE DE LA FENETRE PRINCIPALE       #########################################

    rotate_toplvl = tk.Toplevel(master)                                           # stockage de la fenêtre principale dans la variable master
    rotate_toplvl.title("Pivoter")                                 # changement du titre de la fenêtre
    rotate_toplvl.config(bg='#053f5e')                                # changement de l'arrière plan 
    rotate_toplvl.geometry("250x400")                                # définition de sa taille par défaut à l'ouverture
    rotate_toplvl.geometry("+150+510")                                  # définition de sa position par défaut à l'ouverture (Décalage_Top ; Décalage_Left)

    # ----------------------------------------------------------------------------------------------------------------------------------------


    ######################################      CREATION DES BOITES QUI STRUCTURE LA FENETRE     #############################################

    #   argument 1 : la fenêtre ou boîte dans laquelle on place notre nouvelle boîte
    #   argument 2 : définition de la couleure d'arrière-plan de la boîte

    frame5 = tk.Frame(rotate_toplvl,bg='#053f5e')
    frame6 = tk.Frame(rotate_toplvl,bg='#053f5e')
    frame7 = tk.Frame(rotate_toplvl,bg='#053f5e')
    frame8 = tk.Frame(rotate_toplvl,bg='#053f5e')



    frame5.pack()
    frame6.pack(ipadx=10)
    frame7.pack(pady=20)
    frame8.pack(pady=20)




    pivoter_lbl = tk.Label(frame5,bg='#053f5e',text="Pivoter",font=('Consolas',15),fg='#ffd700')
    pivoter_lbl.pack(side=tk.TOP,ipady=25)

    right_rotate = tk.Button(frame6, text = "↩",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:rotatest('left',im))
    left_rotate_button = tk.Button(frame6, text = "↪",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:rotatest('right',im))

    scale = tk.Scale(frame7,orient=tk.HORIZONTAL)

    retourner_lbl = tk.Label(frame8,bg='#053f5e',text="Retourner",font=('Consolas',15),fg='#ffd700')
    retourner_lbl.pack(side=tk.TOP,pady=25)

    horizontal_flip_button = tk.Button(frame8, text = "↔",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700", command = lambda: flip('horizontal',im))
    vertical_flip_button = tk.Button(frame8, text = "↕",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command= lambda: flip('vertical',im))



    right_rotate.pack(side=tk.RIGHT,ipadx=10)
    left_rotate_button.pack(side=tk.LEFT,ipadx=10)
    scale.pack(side=tk.BOTTOM)
    horizontal_flip_button.pack(side=tk.LEFT,ipadx=10,padx=10)
    vertical_flip_button.pack(side=tk.LEFT,ipadx=10,padx=10) 