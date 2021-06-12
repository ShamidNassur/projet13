#8. Utilisez l’instruction break pour interrompre une boucle for d’affichage des entiers
de 1 à 10 compris, lorsque la variable de boucle vaut 5.
for i in range(1, 11):
    if i==5:
        print("j'ai gangé", i, "!")
        break
        
        #Utilisez l’instruction continue pour modifier une boucle for d’affichage de tous entiers de 1 à 10 compris, sauf lorsque la varia

for i in range(1, 11):
    print(i)
    if (i==5):
        print("ne tient pas compte")
        continue
    print(i!=5)