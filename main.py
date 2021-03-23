import tkinter as tk                                       # on importe tkinter avec le préfixe tk (ca veux dire que quand on voudra appeler une fonction du module tkinter, faudra faire tk.[ta_fonction])
from PIL import Image                                      # on importe Image du module PIL
image = Image.open('fond_ecran.jfif')                      # on charge l'image 'fond_ecran.jfif' à l'avance pour juste avoir à l'afficher après

def openimg():                                             # fonction qui ouvre notre image préchargée ^
    image.show()                                            

def destroy(event):                                         # fonction qui détruit la fenêtre sur laquelle tu es
    event.widget.destroy()                                      # on détruit la fenêtre
    print(f'la fenêtre :  {event.widget} a été fermée\n')       # on print le nom de la fenêtre fermée

def openwindow():                                           # fonction qui créer une autre fenêtre avec un texte "bonjoir" et qui aura la possibilité d'être fermée si on appuie sur la touche Echap lorsqu'on est dessus
    top = tk.Toplevel()                                         # on créer une nouvelle fenêtre
    label_2 = tk.Label(top, text = 'bonjoir')                   # on y rajoute le texte : "bonjoir"
    label_2.pack()                                              # on affiche le texte ^
    top.bind('<Escape>', destroy)                               # lorsque la touche Echap est préssée, on appelle la fonction destroy() *qui ferme la fenêtre sur laquelle on est*

def keypressed(event):                                      # fonction qui print la touche préssé lorsque tu es dans l'entrée de texte créée ci dessous v
    print(f'La touche {event} a été préssée')

# on créer la fenêtre principale  :
fen = tk.Tk()                  

# on lui donne "PhotoShape" comme nom :
fen.title("PhotoShape")            

# on lui défini les dimensions par défaut qu'elle aura à son ouverture :
fen.geometry("720x480")                                    


fen.bind('<Escape>', destroy)         # lorsque la touche Echap est préssée (SEULEMENT SI on est sur la fenetre principale), on appelle destroy() *qui ferme la fenêtre principale*

# on créer une entrée de texte:
entree_texte = tk.Entry(fen)      


entree_texte.bind('<Key>', keypressed)          # lorsqu'une touche est préssée (SEULEMENT SI on est dans l'entrée de texte) ('<Key>' = n'importe laquelle), on appelle keypressed() *qui affiche la touche préssée*


# on créer un bouton : "Ouvrir une fenêtre" qui execute openwindow() quand on clique dessus :
bouton_fenetre = tk.Button(fen, text = "Ouvrir une fenêtre", command = openwindow)

# on créer un bouton : "Ouvrir la photo" qui execute openimg() quand on clique dessus :
bouton_image = tk.Button(fen, text = "Ouvrir la photo", command = openimg)              

# on affiche dans la fenêtre les éléments créés ci dessus (entree_texte, bouton_fenetre, bouton_image) :
entree_texte.pack()
bouton_fenetre.pack()
bouton_image.pack()

# on affiche notre fenêtre principale avec tout ce qu'on a créé
fen.mainloop()