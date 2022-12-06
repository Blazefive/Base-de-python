Nom='Dubois'
Prenom='Jean'
Age=24
Compt_en_banque=26589.24

def teste(g,k):
    return 1+3


#Affichage
#On utilise print seulement pour afficher, python ne retien pas les modification si vous n'utilisez que "print"
#La syntaxe pour le print est la suivante :
#print(ce que vous voulez affiché)
#Exemple :
print (Nom)
print (Age)
print(Compt_en_banque)
#Vous pouvez affiché un texte diectement avec un print
print("Ceci est un texte d'essai")
#Ou encore des opération
print(4+6)

#Tant que une quelque chose est entre guillemets, il affichera caractère pour caractère ce qu'il ya entre.
Variable='58+63*89-2'
print (Variable)

#Si vous voulez affichez une appostrophe dans une chaine de caractère avec un print vous utiliserez \' , Exemple:
print('Bonjour, j\'ai 62 ans')
#Vous pouvez concaténé des informations, exemple:
print('Bonjour, '+'ca va ?')
print('Hello, je suis '+Prenom+', comment ca va ?')

#Mais vous ne pouvez pas utilisé la concaténation avec des integer ou float, exemple:
#print ('J\'ai'+Age+' ans' )
#Ce script au dessue ne marche pas
#il faut utilisé la méthode str(nom_variable), exemple:
print ('J\'ai '+str(Age)+' ans' )

#Dernière petite chose, pour    ffiché un espace , vous avec juste a utilisé ' ',Exemple:
print('yo'+'ca va ?')
print('yo'+' '+'ca va ?')
#Et pour un retour a la ligne on utilise \n, exemple:
print('salut \n'+'ca boom ?')