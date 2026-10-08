# scelta = ""

#la parte dei while poi me la rivedo
#FUNZIONI
    
    
    #es 2 RIUSCITO DA TRASFORMARE IN FUNZIONE ANCORA

lista = []
def creaLista():
    primo = int(input('scegli un numero positivo '))
    for i in range(1, primo+1):
        lista.append(i)
    print(lista)
    
# if scelta == 1:
creaLista()
    

# while scelta != "stoppa":

#     scelta = int(input("Scegli esercizio tra 1, 2,3, 4, 5 e 6 altrimenti scrivi stoppa"))

  #es 1 while
    # if scelta == 'uno':
    #     print(1)
        
    #     check= True
    #     def uno():
    #         while nPos >= 0 :
    #             nPos = int(input('scegli un numero positivo '))
    #             check = False

    #     uno()
    

    
    #es 3 RIUSCITO DA TRASFORMARE IN FUNZIONE ANCORA

def sommaIPari(listas):
    sommaPari = 0
    for i in listas:
        if i % 2 == 0:
                #allora fammi la somma
            sommaPari= sommaPari + i
        
    print(sommaPari)
    
sommaIPari(lista)
    
    #es 4 RIUSCITO DA TRASFORMARE IN FUNZIONE ANCORA
def stampaIDispari(listas):    
    for i in listas:
        if i % 2 == 1:
            numeroD = i
            print(numeroD)
            
stampaIDispari(lista)
        
    #es 5 usa un ciclo per vedere se un numero è Pari
    
def checkPari():
    
    numero = int(input('inserisci un numero'))
    if numero % 2 == 0:
        print(True)
    else:
        print(False)
        
checkPari()
        
    #es 6 usa un ciclo for per i numeri pari della lista
    
def pariL(listaP):
    for i in listaP:
        if i % 2 == 0:
            print(i)
            
pariL(lista)
    
#usa un if per determinare se la somma dei numeri della lista è un numero pari e stampa il risultato
def SommaSuprema(listaRandom):
    sommone = 0
    for i in listaRandom:
        sommone = sommone + i
    
    if (sommone % 2 == 0):
        print('è PARI')
    else:
        print('è DISPARI')
            
SommaSuprema(lista)

    # if scelta != 'uno'and scelta != "due" and scelta != "tre" and scelta != "quattro" and scelta != "cinque" and scelta != "sei" and scelta != "stoppa":
    #     print("Apposto")    