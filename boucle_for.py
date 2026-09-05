# for pour imprimer les nombres de 0 a 4
print("Boucle for pour imprimer les nombres de 0 a 4 : ")
for i in range(5):
    print(i)

print("Boucle for pour imprimer les nombres de 1 a 10 avec un pas de 3 : ")
for i in range(1, 11, 3):  # for pour imprimer les nombres de 1 a 10 avec un pas de 3
    print(i)

print("Boucle for pour imprimer les nombres de 10 a 1 avec un pas de -2 : ")
for i in range(10, 0, -2):  # for pour imprimer les nombres de 10 a 1 avec un pas de -2
    print(i)


fruits = ["pomme", "banane", "cerise", "orange"]
print("Boucle for pour imprimer les fruits : ")
for fruit in fruits:  # for pour imprimer les elements de la liste fruits
    print(fruit)

for i in range(len(fruits)):  # for pour imprimer les elements de la liste fruits avec l'index
    print("Fruit {} : {}".format(i + 1, fruits[i]))  # i + 1 pour commencer l'index a 1 au lieu de 0

for i in range(len(fruits)):
    if i % 2 == 0:  # for pour imprimer les elements de la liste fruits avec l'index pair
        #print(f"Fruit {i + 1} : {fruits[i]}")
        print("Fruit %d : %s" % (i + 1, fruits[i]))  # i + 1 pour commencer l'index a 1 au lieu de 0

for index, fruit in enumerate(fruits):  # for pour imprimer les elements de la liste fruits avec l'index en utilisant enumerate
    #print(f"Fruit {index + 1} : {fruit}")   
    print("Fruit %d : %s" % (index + 1, fruit))  # index + 1 pour commencer l'index a 1 au lieu de 0

print("Boucle for pour imprimer les elements de la liste fruits avec l'index en utilisant enumerate en commencant l'index a 1")
for index, fruit in enumerate(fruits, start=1):  # for pour imprimer les elements de la liste fruits avec l'index en utilisant enumerate
    #print(f"Fruit {index + 1} : {fruit}")   
    print("Fruit %d : %s" % (index, fruit))  # index + 1 pour commencer l'index a 1 au lieu de 0

enlevee = ["raisin", "fraise", "cerise", "kiwi", "pomme"]
enl = 0
for fruit in fruits:
    if fruit in enlevee:  # for pour imprimer les elements de la liste fruits sauf ceux qui sont dans la liste enlevee
        enl += 1
        print("Fruit %s est enlevee" % fruit)
        continue

print("Nombre de fruits enlevees : {}".format(enl))

enlevee2 = ["raisin", "fraise", "kiwi"]
for fruit in fruits:
    if fruit in enlevee2:  # for pour imprimer les elements de la liste fruits sauf ceux qui sont dans la liste enlevee
        print("Fruit %s est enlevee" % fruit)
        break
else:
    print("Aucun fruit n'est enlevee dans la liste fruits")  # else s'executera si la boucle for se termine sans rencontrer un break
