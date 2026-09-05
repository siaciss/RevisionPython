path = 'les_fichiers/input/simple.txt'
file = open(path, 'r')

# content = file.read()
# print(content) 

line = file.readlines()
while line:
    print(line)
    # print(line, end='\n')   # Pour py3 et sup
    line = file.readlines()

# print(line)  # Affiche toutes les lignes du fichier sous forme de liste

file.close()