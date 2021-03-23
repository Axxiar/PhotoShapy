# PhotoShape 
PhotoShape est un éditeur basique d'images en python

### Rappel commandes git :
- git clone [lien du dépo] =
- git pull = récupérer toutes les modifs faites sur le depot par les autres

Pour apporter une modif sur github :
1 git checkout [branche]                *te déplace dans la branche où tu as fait tes modifs (main à éviter)*
2 git add [fichier] ou git add .        *git add . ajoutera tous les fichiers*
3 git commit -m "nom_du_commit"         *par exemple : git commit -m "ajout d'un bouton qui ouvre une fenêtre"*
4 git push


**Quelques infos importantes :**
- *Le fichier '.gitignore' est tout bête : lorsque j'envoie un push vers la page github, celui-ci ignore tous les fichiers dont le nom est écrit dans '.gitignore'*
*j'y ai mit .vscode parceque c'est un fichier créé auto par Visual Studio Code qui lui permet de savoir quelle version de python j'utilise dans mon projet*
*vu que t'as pas forcément la même config ou la même version de python que moi, je veux pas qu'il soit envoyé sur le dépo*

- *si tu voies un truc du style print(f"Bonjour {prénom}") c'est un formattage de string propre à python :*
*tu met un f avant les guillemets et tout ce qui va être entre acolades dans les guillemets (ici prénom) sera considéré comme une variable*
*en gros ca affiche la variable en question directement en string peut importe son type*

*ici : print(f"Bonjour {prénom}") revient à print("Bonjour "+ str(prénom))*

