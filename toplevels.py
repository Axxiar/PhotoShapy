import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk,ImageFilter,ImageOps
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

    pivoter_lbl = tk.Label(frame5,bg='#053f5e',text="PIVOTER",font=('Consolas',15),fg='#ffd700')
    pivoter_lbl.pack(side=tk.TOP,ipady=25)

    right_rotate = tk.Button(frame6, text = "↩",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:rotatest('left',im))
    left_rotate_button = tk.Button(frame6, text = "↪",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:rotatest('right',im))

    retourner_lbl = tk.Label(frame8,bg='#053f5e',text="INVERSER",font=('Consolas',15),fg='#ffd700')
    retourner_lbl.pack(side=tk.TOP,pady=25)

    horizontal_flip_button = tk.Button(frame8, text = "↔",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700", command = lambda: flip('horizontal',im))
    vertical_flip_button = tk.Button(frame8, text = "↕",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command= lambda: flip('vertical',im))



    right_rotate.pack(side=tk.RIGHT,ipadx=10)
    left_rotate_button.pack(side=tk.LEFT,ipadx=10)
    horizontal_flip_button.pack(side=tk.LEFT,ipadx=10,padx=10)
    vertical_flip_button.pack(side=tk.LEFT,ipadx=10,padx=10) 





def t_filters_window(master, lbl, im):

    def filtretest(choix,im):
        global photoim

        if choix == 'filtre1':
            im = im.filter(ImageFilter.BLUR)
        if choix == 'filtre2':
            im = im.filter(ImageFilter.SHARPEN)
        if choix == 'filtre3':
            im = im.convert(mode=("L"))
        if choix == 'filtre4':
            im = im.filter(ImageFilter.CONTOUR)
        if choix == 'filtre10':
            im = im.filter(ImageFilter.EDGE_ENHANCE)
        if choix == 'filtre6':
            im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
        if choix == 'filtre7':
            im = im.filter(ImageFilter.EMBOSS)
        if choix == 'filtre8':
            im = im.filter(ImageFilter.FIND_EDGES)
        if choix == 'filtre9':
            im = im.filter(ImageFilter.SMOOTH)
        if choix == 'filtre5':
            im = im.filter(ImageFilter.SMOOTH_MORE)
        photoim = ImageTk.PhotoImage(im)
        lbl.configure(image=photoim)
        lbl.image = photoim
        


    filters_toplvl = tk.Toplevel(master)
    filters_toplvl.title("Filtres")
    filters_toplvl.config(bg='#053f5e')
    filters_toplvl.geometry("300x750")
    filters_toplvl.geometry("+350+150")

    frame5 = tk.Frame(filters_toplvl,bg='#053f5e')
    frame6 = tk.Frame(filters_toplvl,bg='#053f5e')
    frame7 = tk.Frame(filters_toplvl,bg='#053f5e')
    frame8 = tk.Frame(filters_toplvl,bg='#053f5e')


    frame5.pack(ipady=50)
    frame6.pack(ipadx=10)
    frame7.pack(pady=20)
    frame8.pack(pady=20)

    filtre_lbl = tk.Label(frame5,bg='#053f5e',text="CHOISIR UN FILTRE",font=('Consolas',15),fg='#ffd700')
    filtre_lbl.pack(ipadx=40,ipady=2,pady=2)

    filtre_1 = tk.Button(filters_toplvl, text = "Flouter x2",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:filtretest('filtre1',im))
    filtre_2 = tk.Button(filters_toplvl, text = "Affûter",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:filtretest('filtre2',im))
    filtre_3 = tk.Button(filters_toplvl, text = "Noir et Blanc",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:filtretest('filtre3',im))
    filtre_4 = tk.Button(filters_toplvl, text = "Flippant",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:filtretest('filtre4',im))
    filtre_5 = tk.Button(filters_toplvl, text = "Flouter",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:filtretest('filtre5',im))
    filtre_6 = tk.Button(filters_toplvl, text = "Contraster",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:filtretest('filtre6',im))
    filtre_7 = tk.Button(filters_toplvl, text = "Gaufrer",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:filtretest('filtre7',im))
    filtre_8 = tk.Button(filters_toplvl, text = "Flippant x2",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:filtretest('filtre8',im))

    filtre_3.pack(ipady=1,pady=3,expand=tk.YES)
    filtre_5.pack(ipady=1,pady=3,expand=tk.YES)
    filtre_1.pack(ipady=1,pady=3,expand=tk.YES)
    filtre_2.pack(ipady=1,pady=3,expand=tk.YES) 
    
    filtre_6.pack(ipady=1,pady=3,expand=tk.YES)
    filtre_7.pack(ipady=1,pady=3,expand=tk.YES)
    filtre_4.pack(ipady=1,pady=3,expand=tk.YES)
    filtre_8.pack(side=tk.RIGHT,ipady=1,pady=3,expand=tk.YES)