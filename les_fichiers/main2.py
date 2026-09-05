path = "les_fichiers/output/simple_write.txt"

file = open(path, "w")
file.write("Hello, world!\n")
file.write("This is a test file.\n")
file.close()    

append_path = "les_fichiers/output/simple_append.txt"
append_file = open(append_path, "a")    

append_file.write("Appending a new line.\n")
append_file.write("Appending another line.\n\n")      

append_file.close()
