#per leggere
File1 = open("11 lun 19/esempio.txt", "r")
print(File1)

contenutoRigaFile1 = File1.readline()

# print(contenutoRigaFile1)

contenuto_file1 = File1.read()
print(contenuto_file1)
#chiudere il file
File1.close()
#aprirlo con scrittura
File1 = open("11 lun 19/esempio.txt", "w")
File1.write("scrittura di prova")
File1.close()

File1 = open("11 lun 19/esempio.txt", "r")
# print(contenuto_file1)

with open("11 lun 19/esempio.txt", "r") as file:
    contenuto_file1 = File1.read()
print(contenuto_file1)
    

    