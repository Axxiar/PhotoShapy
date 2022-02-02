###########  IMPORTATION DES MODULES  ###########
import tkinter as tk                                       
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk,ImageFilter,ImageOps,ImageDraw

# ----------------------------------------------------------------------------------------------------------------------------------------
def close(event):
    """attributions : l.69 / l.154 / l.236
    description : détruit le widget sur lequel la fonction est attribué"""
    event.widget.destroy()

def save_im():
    """attributions : l.100 / l.186 / l.253
    description : ouvre l'explorateur de fichier et permet d'enregistrer l'image 'im' au chemin spécifié par l'utilisateur"""
    global image
    savepath = filedialog.asksaveasfilename(title="Sauvegarder Sous")
    try:
        image.save(str(savepath))
    except ValueError:
        messagebox.showwarning("Erreur","Mauvaise extension\nil faut la préciser : 'exemple.png'")


def t_rotate_window(master,lbl,im):
    """attributions : bouton 'Pivoter' l.afpt
    description : fonction qui permet de faire pivoter/inverser l'image
    paramètres : master -> fenêtre principale, lbl -> label qui stock l'image, im -> image à modifier"""
    global image
    image = Image.open(im.filename)
    
    def rotate(side):
        """attributions : toplevel 'rotate_toplvl' l.afpt
        descritpion : fontion qui permet de faire pivoter l'image selon le choix de l'utilisateur
        paramètre : side -> choix de l'utilisateur"""
        global photoim, image

        if side == 'left':
            image = image.rotate(90,expand=True)
        elif side == 'right':
            image = image.rotate(270,expand=True)

        photoim = ImageTk.PhotoImage(image)
        lbl.configure(image=photoim)
        lbl.image = photoim


    def flip(orientation):
        """attributions : toplevel 'rotate_toplvl' l.afpt
        descritpion : fonction que permet de faire inverser l'image selon le choix de l'utilisateur
        paramètre : orientation -> choix de l'utilisateur"""
        global photoim, image

        if orientation == 'horizontal':
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 'vertical':
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
        photoim = ImageTk.PhotoImage(image)
        lbl.configure(image=photoim)
        lbl.image = photoim


    rotate_toplvl = tk.Toplevel(master)                                # stockage de la fenêtre principale dans la variable rotate_toplvl
    rotate_toplvl.title("Pivoter")                                     # définition du titre de la fenêtre
    rotate_toplvl.config(bg='#053f5e')                                 # définition de l'arrière plan 
    rotate_toplvl.geometry("250x400")                                  # définition de sa taille par défaut 
    rotate_toplvl.geometry("+440+510")                                 # définition de sa position par défaut (Décalage_Top ; Décalage_Left)*
    rotate_toplvl.focus()                                              # on met le focus sur le toplevel, le focus représente le widget sur lequel est l'utilisateurs
    rotate_toplvl.bind('<Escape>',close)                               # on appelle 'close()' quand la touche Echap est préssée

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

    confirm_button = tk.Button(frame5, text = "V",font=('Consolas 15 bold'),bg="#115173",fg="green",command=save_im)
    close_button = tk.Button(frame5, text = "X",font=('Consolas 15 bold'),bg="#115173",fg="red")
    confirm_button.pack(side=tk.LEFT,padx=5,ipadx=3)
    close_button.pack(side=tk.RIGHT,padx=5,ipadx=3)




def t_filters_window(master, lbl, im):
    """attributions : bouton 'Filtres' l.afpt
    description : fonction qui permet de mettre des filtres à l'image
    paramètres : master -> fenêtre principale, lbl -> label qui stock l'image, im -> image à modifier"""
    global image
    image = Image.open(im.filename)

    def filtre(choix):
        """attributions : toplevel 'filters_toplvl' l.afpt
        descritpion : fonction que permet de mettre des filtres à l'image selon le choix de l'utilisateur
        paramètre : choix -> choix de l'utilisateur"""
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
        


    filters_toplvl = tk.Toplevel(master)                               # stockage de la fenêtre principale dans la variable filters_toplvl
    filters_toplvl.title("Filtres")                                    # définition du titre de la fenêtre
    filters_toplvl.config(bg='#053f5e')                                # définition de l'arrière plan 
    filters_toplvl.geometry("350x600")                                 # définition de sa taille par défaut 
    filters_toplvl.geometry("+440+200")                                # définition de sa position par défaut (Décalage_Top ; Décalage_Left)
    filters_toplvl.focus()
    filters_toplvl.bind('<Escape>',close)                              # on appelle 'close()' quand la touche Echap est préssée

    #   argument 1 : la fenêtre ou boîte dans laquelle on place notre nouvelle boîte
    #   argument 2 : définition de la couleure d'arrière-plan de la boîte
    frame = tk.Frame(filters_toplvl,bg='#053f5e')
    frame1 = tk.Frame(filters_toplvl,bg='#053f5e')
    frame2 = tk.Frame(filters_toplvl,bg='#053f5e')
    
    frame.pack(ipady=5)

    filtre_lbl = tk.Label(frame,bg='#053f5e',text="CHOISIR UN FILTRE",font=('Consolas bold',20),fg='#ffd700')
    filtre_lbl.pack(side=tk.TOP,ipady=10,pady=8)

    filtre_1 = tk.Button(filters_toplvl, text = "Noir et Blanc",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre3'))
    filtre_2 = tk.Button(frame1, text = "Flouter",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre5'))
    filtre_3 = tk.Button(frame1, text = "x2",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre1'))
    filtre_4 = tk.Button(filters_toplvl, text = "Affûter",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre2'))
    filtre_5 = tk.Button(filters_toplvl, text = "Contraster",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre6'))
    filtre_6 = tk.Button(filters_toplvl, text = "Gaufrer",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre7'))
    filtre_7 = tk.Button(filters_toplvl, text = "Contours",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre4'))
    filtre_8 = tk.Button(filters_toplvl, text = "Négatif",font=('Consolas 15',19),bg="#115173",fg="#ffd700",command=lambda:filtre('filtre8'))

    filtre_1.pack(ipady=1,pady=5, ipadx=4)
    frame1.pack(ipadx=5)
    filtre_2.pack(ipady=1,pady=5, ipadx=3,side=tk.LEFT)
    filtre_3.pack(ipady=1,pady=5, ipadx=5,side=tk.RIGHT)
    filtre_4.pack(ipady=1,pady=5, ipadx=39) 
    filtre_5.pack(ipady=1,pady=5, ipadx=18)
    filtre_6.pack(ipady=1,pady=5, ipadx=34)
    filtre_7.pack(ipady=1,pady=5, ipadx=25)
    filtre_8.pack(ipady=1,pady=5, ipadx=36)

    frame2.pack()
    confirm_button = tk.Button(frame2, text = "V",font=('Consolas 15 bold'),bg="#115173",fg="green",command=save_im)
    close_button = tk.Button(frame2, text = "X",font=('Consolas 15 bold'),bg="#115173",fg="red")
    confirm_button.pack(side=tk.LEFT,padx=5,ipadx=3, pady=15)
    close_button.pack(side=tk.RIGHT,padx=5,ipadx=3, pady=15)



def t_crop_window(master,lbl,im):
    global image, clicked, pos1, pos2
    image = Image.open(im.filename)

    def click(event):
        global image, clicked, pos1, pos2
        
        if clicked <2:
            x0 = event.x - 2
            x1 = event.x + 2
            y0 = event.y - 2
            y1 = event.y + 2
            drawim = ImageDraw.Draw(im)
            drawim.ellipse([x0, y0, x1, y1],fill="red")
            photoim = ImageTk.PhotoImage(im)
            lbl.config(image=photoim)
            lbl.image = photoim
            crop_toplvl.lift()

            if clicked == 0:
                pos1 = (event.x,event.y)
                clicked += 1
            else:
                pos2 = (event.x,event.y)

                drawim.rectangle([pos1,pos2],outline="red",width=3)
                image = image.crop((pos1[0],pos1[1],pos2[0],pos2[1]))
                clicked += 1
                photoim = ImageTk.PhotoImage(image)
                lbl.config(image=photoim)
                lbl.image = photoim
                crop_toplvl.lift()
                
            


    crop_toplvl = tk.Toplevel(master)
    crop_toplvl.title("Rogner")
    crop_toplvl.config(bg='#053f5e')
    crop_toplvl.geometry("700x250")
    crop_toplvl.geometry("+150+500")
    crop_toplvl.focus()
    crop_toplvl.bind('<Escape>',close)

    clicked = 0
    pos1 = (0,0)
    pos2 = (0,0)
    lbl.bind('<Button-1>',click)


    frame1 = tk.Frame(crop_toplvl,bg='#053f5e')
    frame1.pack(pady=30)
    frame2 = tk.Frame(crop_toplvl,bg='#053f5e')
    frame2.pack(pady=20)

    info_text = tk.Label(frame1,font=('Consolas 11'),bg="#053f5e",fg="#ffd700",
    text="""Cliquez sur la photo de gauche pour sélectionner le rognage\n\nPensez à enregistrer ave le bouton V ci-dessous\npuis à réouvrir votre image modifier pour pouvoir la recouper""")

    info_text.pack()

    confirm_button = tk.Button(frame2, text = "V",font=('Consolas 15 bold'),bg="#115173",fg="green",command=save_im)
    close_button = tk.Button(frame2, text = "X",font=('Consolas 15 bold'),bg="#115173",fg="red")
    confirm_button.pack(side=tk.LEFT,padx=5,ipadx=3)
    close_button.pack(side=tk.RIGHT,padx=5,ipadx=3)
