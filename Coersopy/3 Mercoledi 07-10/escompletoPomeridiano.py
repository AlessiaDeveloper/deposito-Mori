#es 1
numero= int(input('inserisci un numero'))

#parte 1
while numero <= 0:
    numero= int(input('riinserisci un numero'))

#parte 2   

somma = 0
if numero >= 1:
    for i in range(1, numero+1):
        if i % 2 == 0:
            #se son pari
            numeroP = i
                #allora fammi la somma
            somma= somma + numeroP

            
            #lo riprendo
print('la somma è', somma)
#  parte 3  
if numero >= 1:
    for d in range(1, numero+1):
        if d % 2 == 1:
            print('i numeri dispari sono: ', d)
            
      
    
#parte 4

#numero è un numero primo?

primo = True

# if numero         