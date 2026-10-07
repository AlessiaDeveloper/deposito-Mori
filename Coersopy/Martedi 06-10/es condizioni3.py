# #es1

# age = int(input('quanti anni hai? '))

# if age >= 18:
#     age = 'maggiorenne'
# else:
#     age = 'minorenne'
    

# match age:
#     case 'maggiorenne':
#         print('puoi vedere il film')
#     case 'minorenne':
#         print('non puoi vedere il film')    

# #es2

# n1 = int(input('inserisci un numero'))
# n2 = int(input('inserisci un numero'))

# scelta = input('scegli tra addizione, sottrazione, moltlipicazione e divisione')

# match scelta:
#     case 'addizione':
#         print(n1 + n2)
#     case 'sottrazione':
#         print(n1 - n2)
#     case 'moltlipicazione':
#         print(n1 * n2)  
#     case 'divisione':
#         if n2 == 0:
#             print('errore divisione per zero')
#         print(n1 / n2)      
#     case _:
#         print('operazione non valida') 


lista = ['nome', 'age', 'sesso', 'premium']
nomestr = input('qual è il tuo nome?')
lista[0] = nomestr
age = int(input('quanti anni hai? '))
lista[1]= age
sesso = input('qual è il tuo sesso?')
lista[2] = sesso[0]
premium = bool(input('Sei premium? True o False? Usa le maiuscole'))
lista[3] = premium

richiesta = input('vuoi modificare un campo tra questi? nome, anni, sesso, premium o se non vuoi modificare nulla scrivi no')

match richiesta:
    case 'no':
        print('registrato')
    case 'nome':
        nomestr = input('qual è il tuo nome?')
        lista[0] = nomestr
    case 'anni':
        age = int(input('quanti anni hai? '))
        lista[1]= age
    case 'sesso':
        sesso = input('qual è il tuo sesso?')
    case 'premium':
        premium = bool(input('Sei premium? True o False? Usa le maiuscole'))
    case _:
        print('scelta non valida')

print(lista)

lista2 =['cognome']
domanda = input('vuoi inserire dati aggiuntivi in caso affermativo aggiungi cognome')

match domanda:
    case 'no':
        print('nessun altra informazione')
    case 'si':
        cognome = input('qual è il tuo cognome?')
        lista2[0] = cognome

eliminare = input('vuoi eliminare qualche informazione tra tra questi? nome, anni, sesso, premium o se non vuoi modificare nulla scrivi no') 
match eliminare:
    case 'no':
        print('va bene')
    case 'nome':
        lista.remove(0)
    case 'anni':
        lista.remove(1)
    case 'sesso':
        lista.remove(2)
    case 'premium':
        lista.remove(3)
    case _:
        print('scelta non valida')    