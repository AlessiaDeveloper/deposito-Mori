#es 1 
def inserisciNumeroPositivo():
    numero = int(input(' inserisci un numero : '))

    while numero <= 0:
        numero = int(input('Inserisci un numero: '))
  
    return numero
    #es 2 RIUSCITO DA TRASFORMARE IN FUNZIONE ANCORA

def creaLista():
    lista = []
    primo = inserisciNumeroPositivo()
    for i in range(1, primo+1):
        lista.append(i)
    print('lista creata', lista)
    return lista
# if scelta == 1:
# creaLista()
    
    
    #es 3 RIUSCITO 

def sommaIPari(listas: list):
    sommaPari = 0
    for i in listas:
        #se l'iterabile diviso due non ha il resto cioè ha il resto = a zero
        if i % 2 == 0:
            #aggiungi a somma pari l'iterabile
            sommaPari= sommaPari + i
        
    print(sommaPari)
    
# sommaIPari(creaLista())
    
    #es 4 RIUSCITO DA TRASFORMARE IN FUNZIONE ANCORA
def stampaIDispari(listas: list):    
    for i in listas:
        if i % 2 == 1:
            print(i)
            
# stampaIDispari(creaLista())
        
    #es 5 usa un ciclo per vedere se un numero è Pari
    
def checkPari(num):
    return num % 2 == 0
        
        
    #es 6 usa un ciclo for per stampare i numeri pari della lista
    
def pariL(listaP):
    for i in listaP:
        if checkPari(i) == True:
            print(i)
            
    
#usa un if per determinare se la somma dei numeri della lista è un numero pari e stampa il risultato
def SommaSuprema(listaRandom):
    sommone = 0
    for i in listaRandom:
        sommone = sommone + i
    
    if checkPari(sommone):
        print('la somma dei numeri è PARI')
    else:
        print('la somma dei numeri è DISPARI')
    print(sommone)
            

    # if scelta != 'uno'and scelta != "due" and scelta != "tre" and scelta != "quattro" and scelta != "cinque" and scelta != "sei" and scelta != "stoppa":
    #     print("Apposto")    
    
menuAperto = True    
while menuAperto:
    scelta = input('vuoi fare un esercizio? se si rispondi con 1, 2, 3, 4, 5, 6, 7 altrimenti rispondi no: ')

    match scelta:
        case '1':
            inserisciNumeroPositivo()
        case '2':
            creaLista()
        case '3':
            sommaIPari(creaLista())
        case '4':
            stampaIDispari(creaLista())
        case '5':
            checkPari(inserisciNumeroPositivo())
        case '6':
            pariL(creaLista())
        case '7':
            SommaSuprema(creaLista())
        case 'no':
            menuAperto = False
        case _:
            print('scelta non valida')    