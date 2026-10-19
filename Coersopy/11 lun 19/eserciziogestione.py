#creafile
# def creaFile():
#     #apro il file con la w per crearlo funziona
#     File1 = open("11 lun 19/filecreazione.txt", "w")
#     File1.write("file creato")
#     File1.close()
#     print('file creato con successo')
    
#extra
def creaFile():
    #apro il file con la w per crearlo funziona con sintassi di f
    sceltaTitolo = input("scegli il titolo del file")
    File1 = open(f"11 lun 19/{sceltaTitolo}", "w")
    File1.write("file creato")
    File1.close()
    print('file creato con successo')
        
    
    
def modificaFile():
    #apro il file con la a per mettere del testo aggiunto con il metodo append
    
        File1 = open("11 lun 19/filecreazione.txt", "a")
        #da vedere come aggiungere del testo a capo
        #ce l'ho fatta
        testoAggiunto = input(f"\n scrivi il testo che vuoi aggiungere  ")
        
        File1.write(testoAggiunto)
        File1.close()
        print('file modificato con successo')

def leggiFile():
    #apro il file con il read
        File1 = open("11 lun 19/filecreazione.txt", "r")
        contenuto = File1.read()
        print(contenuto)
        File1.close()

def svuotaFile():
    #svuoto il file con w perché x mi da errore
        File1 = open("11 lun 19/filecreazione.txt", "w")
        File1.write('')
        File1.close()
        print('file svuotato con successo')
        


#il menu con scelta, ho tolto il no dalla scelta per uscire
menuAperto = True    
while menuAperto:
    scelta = input('vuoi creare un file?Scegli 1, vuoi modificare? scegli 2, vuoi leggere un file? scegli 3, vuoi svuotare un file? scegli 4 ')

    match scelta:
        case '1':
            creaFile()
        case '2':
            modificaFile()
        case '3':
            leggiFile()
        case '4':
            svuotaFile()
        case _:
            print('scelta non valida')    
            

