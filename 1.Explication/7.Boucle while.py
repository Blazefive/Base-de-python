#Boucle while est une boucle a condition qui peut etre traduite par 'tant que'.
#Attention, la boucle while est la boucle la plus suceptible de faire tourné votre programme a l'infinie.
#Cette boucle est assez spécial car on doit utilisé l'opération inverse de ce que l'on veut, exemple:
#While a<3 :
#Tant que a est strictement inferieur a 3:
#On veut que le programme s'arrette quand a est superieur ou égale a 3
#On peut utilisé le and et le or avec le while
#Exemple avec and:
#while a<10 and a>0:
#Exemple avec or:
#while a<10 or a>15:
#Exemple concret:

a=0
while a<3:
    a=a+1
    print (a)
#Ici le programme se finie quand notre a est superieur ou égale à 3.
