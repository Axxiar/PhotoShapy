import tkinter as tk                                       
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import os
import time
import webbrowser as web
from fonctions import dest,f_getting_started,source_code,f_doc,f_credit


def rotate_window():
    def back_menu():
        global import_button
        global modify_button
        global delete_button
        try:
            dest(back,draw,filters,crop,rotate,adjust)
        except:
            print('pas encore')
            
        import_button = tk.Button(frame5, text = "Importer une photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=open_img)
        modify_button = tk.Button(frame5, text = "Modifier la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=modify)
        delete_button = tk.Button(frame5, text = "Effacer la photo",font=('Consolas'),bg="#115173",fg="#ffd700",command=delete_img)
        import_button.pack(padx=155,ipady=10,ipadx=10,pady=30)
        modify_button.pack(ipady=10,ipadx=16,pady=30)
        delete_button.pack(ipady=10,ipadx=20,pady=25)


    def modify():
        global back
        global draw
        global filters
        global crop
        global rotate
        global adjust

        dest(import_button,modify_button,delete_button)
        
        back = tk.Button(frame5, text = "<",font=('Consolas',20,'bold'),bg="#ffd700",fg="#115173",command=back_menu)

        draw = tk.Button(frame5, text = "Dessiner",font=('Consolas'),bg="#115173",fg="#ffd700")
        crop = tk.Button(frame5, text = "Rogner",font=('Consolas'),bg="#115173",fg="#ffd700")
        rotate = tk.Button(frame5, text = "Pivoter",font=('Consolas'),bg="#115173",fg="#ffd700")
        filters = tk.Button(frame5, text = "Filtres",font=('Consolas'),bg="#115173",fg="#ffd700")
        adjust = tk.Button(frame5, text = "Ajuster (RGB)",font=('Consolas'),bg="#115173",fg="#ffd700")

        back.pack(side=tk.BOTTOM,pady=10,ipadx=30)
        draw.pack(ipadx=60,ipady=5,pady=10)
        crop.pack(ipadx=65,ipady=5,pady=10)
        rotate.pack(ipadx=60,ipady=5,pady=10)
        filters.pack(ipadx=60,ipady=5,pady=10)
        adjust.pack(ipadx=33,ipady=5,pady=10)


    def open_img():
        """attribution : bouton "Importer" (l.afpt)
        description : permet d'ouvrir et de sélectionner depuis l'explorateur de fichiers une image 
        puis de la charger dans la fenêtre"""
        global im                          # permet à la variable im d'être aussi utilisée en dehors de cette fonction 
        global photoim
        global image

        filename = filedialog.askopenfilename(title="Ouvrir un fichier",initialdir= os.getcwd(),filetype=((".png","*.png"), (".jpg","*.jpg"), (".jfif","*.jfif"), ("Tous les fichiers","*")))
        try:                                                        # try fait comprendre à python qu'on essaye quelque chose
            im = Image.open(filename)           # ici on charge la photo sélectionnée et on la stocke dans im 
                                                #(le fichier choisit peut ne pas être dans un format accepté par Pillow) d'où le try:
            
            if im.height >= 20:                     # pas besoins de commenter ca sera modifié
                print('too big')                    # |
                im = im.resize((im.width,150))      # |
            if im.width >= 60:                      # |
                print('too large\n')                # |
                im = im.resize((200,im.height))     # |
            
            image = im
            photoim = ImageTk.PhotoImage(im)             # on charge l'image en élément ImageTk qu'on stocke dans im 
            
            default_noimg.destroy()

            default_lbl.configure(image=photoim,bg='grey')  # on rajoute l'image au label default_lbl 
            default_lbl.image = photoim                     #   (celui qui n'aura pas de modifications pour afficher à l'utilisateur son image de départ) 

            lbl.configure(image=photoim)
            lbl.image =photoim 
            
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
            del im
        else:
            print("pas d'image")



    def close(event):
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

    def getting_started():
        """"""
        masterx=master.winfo_width()
        mastery=master.winfo_height()
        f_getting_started(masterx,mastery)
        

    def doc():
        #- renvoyer sur le site (docu à créer)
        """bloub"""
        masterx=master.winfo_width()
        mastery=master.winfo_height()
        f_doc(masterx,mastery)


    def credit():
        """"""
        masterx=master.winfo_width()
        mastery=master.winfo_height()
        f_credit(masterx,mastery)

    def rotatest(side):
        global image
        global photoim
        if 'image' in globals():
            if side == 'left':
                image = image.transpose(Image.ROTATE_90)
            elif side == 'right':
                image = image.transpose(Image.ROTATE_270)
            photoim = ImageTk.PhotoImage(image)
            default_lbl.configure(image=photoim)
        else:
            print("pas d'image")

    def flip(orientation):
        global image
        global photoim
        if 'image' in globals():
            if orientation == 'horizontal':
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 'vertical':
                image = image.transpose(Image.FLIP_TOP_BOTTOM)
            photoim = ImageTk.PhotoImage(image)
            default_lbl.configure(image=photoim)
        else:
            print("pas d'image")

    # ----------------------------------------------------------------------------------------------------------------------------------------


    ####################################      CREATION ET PARAMETRAGE DE LA FENETRE PRINCIPALE       #########################################

    master = tk.Tk()                                           # stockage de la fenêtre principale dans la variable master

    master.title("PhotoShapy")                                 # changement du titre de la fenêtre
    master.config(bg='#022c43')                                # changement de l'arrière plan 
    master.geometry("1850x900")                                # définition de sa taille par défaut à l'ouverture
    master.geometry("+25+25")                                  # définition de sa position par défaut à l'ouverture (Décalage_Top ; Décalage_Left)

    master.bind('<Escape>', close)                           # lorsque, sur la fenêtre, la touche Echap est préssée, on appelle la fonction destroy (l.afpt)
    # ----------------------------------------------------------------------------------------------------------------------------------------


    ######################################      CREATION DES BOITES QUI STRUCTURE LA FENETRE     #############################################

    #   argument 1 : la fenêtre ou boîte dans laquelle on place notre nouvelle boîte
    #   argument 2 : définition de la couleure d'arrière-plan de la boîte
    frame1 = tk.Frame(master,bg='#022c43')                     
    frame2 = tk.Frame(frame1,bg='#053f5e')
    frame3 = tk.Frame(frame1,bg='#053f5e')
    frame4 = tk.Frame(frame2,bg='#053f5e')
    frame5 = tk.Frame(frame2,bg='#053f5e')
    frame6 = tk.Frame(frame2,bg='#053f5e')
    frame7 = tk.Frame(frame2,bg='#053f5e')
    frame8 = tk.Frame(frame2,bg='#053f5e')
    separation1 = tk.Frame(frame1,bg='#ffd700')             # cette boîte et la suivante servent de séparations visuelles (les deux traits jaunes sur la fenêtre)
    separation2 = tk.Frame(frame2,bg='#ffd700')

    frame1.pack(fill=tk.BOTH,expand=tk.YES)
    frame2.pack(padx=20,ipadx=20,ipady=20,side=tk.LEFT)
    frame3.pack(padx=20,ipady=10,ipadx=10,side=tk.RIGHT)
    frame4.pack(pady=20,padx=10)
    separation2.pack(ipadx=160,pady=20)
    frame5.pack()
    frame6.pack(ipadx=10)
    frame7.pack(pady=20)
    frame8.pack(pady=20)

    separation1.pack(ipady=380,expand=tk.YES)



    pivoter_lbl = tk.Label(frame5,bg='#053f5e',text="Pivoter",font=('Consolas',15),fg='#ffd700')
    pivoter_lbl.pack(side=tk.TOP,ipady=25)

    right_rotate = tk.Button(frame6, text = "↩",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=open_img)
    left_rotate_button = tk.Button(frame6, text = "↪",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command=lambda:rotatest('right'))

    scale = tk.Scale(frame7,orient=tk.HORIZONTAL)

    retourner_lbl = tk.Label(frame8,bg='#053f5e',text="Retourner",font=('Consolas',15),fg='#ffd700')
    retourner_lbl.pack(side=tk.TOP,pady=25)

    horizontal_flip_button = tk.Button(frame8, text = "↔",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700", command = lambda: flip('horizontal'))
    vertical_flip_button = tk.Button(frame8, text = "↕",font=('Consolas 20 bold'),bg="#115173",fg="#ffd700",command= lambda: flip('vertical'))

    right_rotate.pack(side=tk.RIGHT,ipadx=10)
    left_rotate_button.pack(side=tk.LEFT,ipadx=10)
    scale.pack(side=tk.BOTTOM)
    horizontal_flip_button.pack(side=tk.LEFT,ipadx=10,padx=10)
    vertical_flip_button.pack(side=tk.LEFT,ipadx=10,padx=10)



    lbl = tk.Label(frame3,width=130,height=43,bg='grey',text="Pas d'image",font=('Consolas'),fg='white')                    # lbl est un label qui contiendra l'image sur laquelle on verra les modifications
    default_noimg = tk.Label(frame4, width=60,height=20,bg='grey',text="Pas d'image",font=('Consolas',10),fg='white')       # default_noimg est le label par défaut quand il n'y a pas d'image
    default_lbl = tk.Label(frame4,bg='#053f5e')         # default_lbl est le label qui contiendra l'image par défaut sans ses changements

    lbl.pack(pady=10,padx=10,expand=tk.YES)
    default_lbl.pack(side=tk.TOP)
    default_noimg.pack(pady=10,padx=10,side=tk.TOP)



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
    file_menu.add_command(label="Quitter",accelerator='Echap',background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=master.destroy)


    #sous-menu "Outils"
    tools_menu = tk.Menu(menu, tearoff = 0)
    tools_menu.add_command(label="Ajuster (RGB)",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
    tools_menu.add_command(label="Rogner",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
    tools_menu.add_command(label="Filtres",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
    tools_menu.add_command(label="Dessiner",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
    tools_menu.add_command(label="Pivoter",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700')
    menu.add_cascade(label="Outils", menu=tools_menu)

    #sous-menu "Aide"
    help_menu = tk.Menu(menu, tearoff = 0)
    help_menu.add_command(label="Prise en main",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=getting_started)
    help_menu.add_command(label="Documentation",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700', command=doc)
    help_menu.add_command(label="Code Source",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=source_code)
    help_menu.add_command(label="Crédits",background='#053f5e',foreground='#ffd700',activeforeground='#053f5e',activebackground='#ffd700',command=credit)
    menu.add_cascade(label="Aide", menu=help_menu)

    master.config(menu=menu)
    # ----------------------------------------------------------------------------------------------------------------------------------------


    ######################################################    LANCEMENT DE LA FENETRE    #####################################################

    master.mainloop()

rotate_window()