#es 1

# numero = int(input('scegi un numero'))

# if numero %2 ==0:
#     print('pari')
# else:
#     print('dispari')


#es 2 while e range

#scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i numeri da n a 0 compreso, 
# dcreementando di 1. deve potersi ripetere all'infinito
controllore= True 
while controllore:
    intero = int(input('scrivi un numero intero positivo   '))
    for intero in range(intero, -1,-1):
        print(intero)

#lo riprendo dopo

#es 3 for

# lista = []

# numero1= int(input('inserisci un numero'))
# numero2= int(input('inserisci un secondo numero'))
# lista.append(numero1)
# lista.append(numero2)
# print(lista)

# for numero in lista:
#     numero = numero ** 2
#     print(numero)


#esercizio 4

lista = []

numero1= int(input('inserisci un numero'))
numero2= int(input('inserisci un secondo numero'))
numero3= int(input('inserisci un terzo numero'))
lista.append(numero1)
lista.append(numero2)
lista.append(numero3)

for numero in lista:
    massimo = 0
    if numero > massimo:
        massimo = numero
        print(massimo)
    
    
#punto while fare con il len