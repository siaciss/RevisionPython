with_path = "les_fichiers/output/with.txt"

with open(with_path, "w") as with_file:
    with_file.write("Appending a new line using 'with' statement.\n")
    with_file.write("Appending another line using 'with' statement.\n\n")   

with open(with_path, "a") as with_file:
    with_file.write("Appending a new line using 'with' statement.\n")
    with_file.write("Appending another line using 'with' statement.\n\n")   


with open(with_path, "r") as with_file:
    content = with_file.read()
    print(content)
