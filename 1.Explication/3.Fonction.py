#Généralement on crée une fonction pour  dans un meme block des instruction et pour pouvoir les réutilisé.
#On commence une fonction par: def nomfonction(valeur1,valeur2,...):
# Exemple:
def addition(a,b):

#On peut ensuite écrire nos instruction.
    resultat=a+b
#On utilise les return pour mettre fin a une fonction, il retourne le résultat qui met fin a la fonction.
    return resultat


#Une fois nos fonction terminé , ou pour la testé, on crée une section Main comme ci-dessou, il est préférable de bien indiquer qu'il sagit du main.

################Main#################
#Dans le main on y indique les valeur inconnue que nous voulons utilisé dans les fonctions.!!!! Elle doivent être avant votre print !!!!
#Exemple:
a=5
b=6
#On utilise un print avec le nom de la fonction que l'on veut utilisé et affiché, il est important de respecté la ponctation suivante : print(nomfonction(valeur1,valeur2,...)
#Exemple :
print (addition(a,b))
#Nous pouvons aussi faire comme ceci:
print (addition(5,6))
#Dans ce cas la, il n'est pas la peine de déclaré que a=5 et que b=6.




#Voicis la fonction ci-dessu en condensé, pour l'utilisé, mettez le texte du dessu en commentaire et enlevé les commentaire du texte d'en dessou (Les commentaire sont définie par les '##').
##def addition(a,b):
##    resultat=a+b
##    return resultat
##
##
##################Main#################
##a=5
##b=6
##print (addition(a,b))
##print (addition(5,6))
