# #Esercizio:  Andare a creare un sistema ripetibile che permetta di inserire: sia al fondo che nella posizione che vogliamo noi, modificare, 
# # stampare ed eliminare liste, che sono divise dal tipo che viene scelto.

# lista = [1, 3, 4, 7, 8]

# #inserire
# def inserisci(lista):
#     numero = int(input('inserisci un numero'))
#     lista.append(numero)
#     return lista

# inserisci(lista)
# print(lista)

# def modifica(lista):
#     print(lista)
#     lunghezzaLista = len(lista)
#     scelta = int(input('inserisci un numero tra 1 e 4'))
#     numeroScelto= int(input('inserisci un numero'))
#     lista[scelta] = numeroScelto

# modifica(lista)   

# def stampa(lista):
#     print(lista)                     
# # menu= True
# stampa(lista)

# def elimina(lista):
#     #non so come fare per fare scegliere all'utente il valore da eliminare quindi gli dico di scegliere il numero 1
#     sceltaD = int(input('inserisci numero 1'))
#     lista.remove(sceltaD)

# modifica(lista)  
# while menu():
#     scelta = input('cosa vuoi fare? Scegli tra ,inserire, modificare, stampare, eliminare oppure dimmi no')
    
#     match scelta:
#         case 'inserire':
#             inserisci()
#         case 'modifica':
#             modifica()
#         case 'stampare':
#             stampa()
#         case 'eliminare':
#             elimina()
#         case 'no':
#             menu = False
#         case _:
#             print('scelta non valida')    

#Esercizio:  Andare a creare un sistema ripetibile che obblighi l'utente a inserire nome e codice, poi l'utente può accedere ad un secondo pezzo del menu, 
# solo se ha inserito i dati nella fase prima e dopo un login (codice == codice e nome == nome) questa seconda parte deve permettere di visionare due operazioni,
# somme e sottrazioni e salvare ogni risultato di ogni operazione, entrambi i menu ripetibili ( menu: registrazione // login --> dentro login: le due operazioni 
# e visualizza risultati)

#funzione somma
def somma(a,b):
    print(a + b)

#funziona sottrai 
def sottrazione(a,b):
    print(a - b)

login = True

while login:
    nomeUtente = input('inserisci nome utente: ')
    codice = int(input('inserisci codice: ' ))
    nomeUtenteVero= 'charlie'
    codiceVero = 4444
    
    if nomeUtenteVero.lower() == nomeUtente.lower() and codiceVero == codice:
        login = False
        print('hai eseguito accesso')
        
scelta = input('vuoi sommare o sottrarre?')

if scelta.lower() == 'sommare':
    n1= int(input('inserisci un numero: ' ))
    n2= int(input('inserisci un secondo numero: ' ))
    somma(n1,n2)
    
elif scelta.lower() == 'sottrarre':
        n1= int(input('inserisci un numero: ' ))
        n2= int(input('inserisci un secondo numero: ' ))
        sottrazione(n1,n2)