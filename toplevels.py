import tkinter as tk                                       

from PIL import Image,ImageTk,ImageFilter,ImageOps
# ----------------------------------------------------------------------------------------------------------------------------------------



def t_rotate_window(master,lbl,im):
    global image
    image = Image.open(im.filename)
    
    def rotate(side):
        global photoim, image

        if side == 'left':
            image = image.rotate(90,expand=True)
        elif side == 'right':
            image = image.rotate(270,expand=True)

        photoim = ImageTk.PhotoImage(image)
        lbl.configure(image=photoim)
        lbl.image = photoim


    def flip(orientation):
        global photoim, image

        if orientation == 'horizontal':
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 'vertical':
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
        photoim = ImageTk.PhotoImage(image)
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

    frame1 = tk.Frame(rotate_toplvl,bg='#053f5e')
    frame2 = tk.Frame(rotate_toplvl,bg='#053f5e')
    frame3 = tk.Frame(rotate_toplvl,bg='#053f5e')
    frame4 = tk.Frame(rotate_toplvl,bg='#053f5e')
    frame5 = tk.Frame(rotate_toplvl,bg='#053f5e')



    frame1.pack()
    frame2.pack(ipadx=10)
    frame3.pack(pady=20)
    frame4.pack(pady=20)
    frame5.pack()

    pivoter_lbl = tk.Label(frame1,bg='#053f5e',text="PIVOTER",font=('Consolas',15),fg='#ffd700')
    pivoter_lbl.pack(side=tk.TOP,ipady=25)

    right_rotate = tk.Button(frame2, text = "↩",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:rotate('left'))
    left_rotate_button = tk.Button(frame2, text = "↪",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:rotate('right'))

    retourner_lbl = tk.Label(frame4,bg='#053f5e',text="INVERSER",font=('Consolas',15),fg='#ffd700')
    retourner_lbl.pack(side=tk.TOP,pady=25)

    horizontal_flip_button = tk.Button(frame4, text = "↔",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700", command = lambda: flip('horizontal'))
    vertical_flip_button = tk.Button(frame4, text = "↕",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command= lambda: flip('vertical'))



    right_rotate.pack(side=tk.RIGHT,ipadx=10)
    left_rotate_button.pack(side=tk.LEFT,ipadx=10)
    horizontal_flip_button.pack(side=tk.LEFT,ipadx=10,padx=10)
    vertical_flip_button.pack(side=tk.LEFT,ipadx=10,padx=10)    

    confirm_button = tk.Button(frame5, text = "V",font=('Consolas 15 bold'),bg="#115173",fg="green")
    close_button = tk.Button(frame5, text = "X",font=('Consolas 15 bold'),bg="#115173",fg="red")
    confirm_button.pack(side=tk.LEFT,padx=5,ipadx=3)
    close_button.pack(side=tk.RIGHT,padx=5,ipadx=3)




def t_filters_window(master, lbl, im):
    global image
    image = Image.open(im.filename)

    def filtre(choix):
        global photoim, image

        if choix == 'filtre1':
            image = image.filter(ImageFilter.BLUR)
        if choix == 'filtre2':
            image = image.filter(ImageFilter.SHARPEN)
        if choix == 'filtre3':
            image = image.convert(mode=("L"))
        if choix == 'filtre4':
            image = image.filter(ImageFilter.CONTOUR)
        if choix == 'filtre10':
            image = image.filter(ImageFilter.EDGE_ENHANCE)
        if choix == 'filtre6':
            image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        if choix == 'filtre7':
            image = image.filter(ImageFilter.EMBOSS)
        if choix == 'filtre8':
            image = image.filter(ImageFilter.FIND_EDGES)
        if choix == 'filtre9':
            image = image.filter(ImageFilter.SMOOTH)
        if choix == 'filtre5':
            image = image.filter(ImageFilter.SMOOTH_MORE)
        photoim = ImageTk.PhotoImage(image)
        lbl.configure(image=photoim)
        lbl.image = photoim
        


    filters_toplvl = tk.Toplevel(master)
    filters_toplvl.title("Filtres")
    filters_toplvl.config(bg='#053f5e')
    filters_toplvl.geometry("380x530")
    filters_toplvl.geometry("+425+200")

    frame = tk.Frame(filters_toplvl,bg='#053f5e')
    frame1 = tk.Frame(filters_toplvl,bg='#053f5e')
    frame2 = tk.Frame(filters_toplvl,bg='#053f5e')
    frame3 = tk.Frame(filters_toplvl,bg='#053f5e')
    
    frame.pack(ipady=5)

    filtre_lbl = tk.Label(frame,bg='#053f5e',text="CHOISIR UN FILTRE",font=('Consolas',25),fg='#ffd700')
    filtre_lbl.pack(side=tk.TOP,ipady=10,pady=8)

    filtre_1 = tk.Button(filters_toplvl, text = "Noir et Blanc",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre3'))
    filtre_2 = tk.Button(frame1, text = "Flouter",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre5'))
    filtre_3 = tk.Button(frame1, text = "x2",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre1'))
    filtre_4 = tk.Button(filters_toplvl, text = "Affûter",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre2'))
    filtre_5 = tk.Button(filters_toplvl, text = "Contraster",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre6'))
    filtre_6 = tk.Button(filters_toplvl, text = "Gaufrer",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre7'))
    filtre_7 = tk.Button(frame2, text = "Contours",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre4'))
    filtre_8 = tk.Button(frame2, text = "Négatif",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre8'))

    filtre_1.pack(ipady=1,pady=5)
    frame1.pack(ipadx=5)
    filtre_2.pack(ipady=1,pady=5,ipadx=4,side=tk.LEFT)
    filtre_3.pack(ipady=1,pady=5,ipadx=4,side=tk.RIGHT)
    filtre_4.pack(ipady=1,pady=5) 
    filtre_5.pack(ipady=1,pady=5)
    filtre_6.pack(ipady=1,pady=5)
    frame2.pack(pady=5)
    filtre_7.pack(ipady=1,pady=5,side=tk.LEFT)
    filtre_8.pack(ipady=1,pady=5,side=tk.RIGHT)

    frame3.pack()

    confirm_button = tk.Button(frame3, text = "V",font=('Consolas 15 bold'),bg="#115173",fg="green")
    close_button = tk.Button(frame3, text = "X",font=('Consolas 15 bold'),bg="#115173",fg="red")
    confirm_button.pack(side=tk.LEFT,padx=5,ipadx=3)
    close_button.pack(side=tk.RIGHT,padx=5,ipadx=3)
# ----------------------------------------------------------------------------------------------------------------------------------------


def t_crop_window(master,lbl,im):
    crop_toplvl = tk.Toplevel(master)
    crop_toplvl.title("Rogner")
    crop_toplvl.config(bg='#053f5e')
    crop_toplvl.geometry("380x530")
    crop_toplvl.geometry("+350+150")


    frame5 = tk.Frame(crop_toplvl,bg='#053f5e')

    confirm_button = tk.Button(frame5, text = "V",font=('Consolas 15 bold'),bg="#115173",fg="green")
    close_button = tk.Button(frame5, text = "X",font=('Consolas 15 bold'),bg="#115173",fg="red")
    confirm_button.pack(side=tk.LEFT,padx=5,ipadx=3)
    close_button.pack(side=tk.RIGHT,padx=5,ipadx=3)
# ----------------------------------------------------------------------------------------------------------------------------------------