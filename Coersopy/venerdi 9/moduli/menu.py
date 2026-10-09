import utility as u 

menu = True

scelta = input('scegli tra +, -, *, / oppure scegli esci: ')

if scelta != 'no':
    num1= int(input('scegli un numero: '))
    num2 = int(input('scegli un secondo numero: '))

match scelta:
    case '+':
        print(u.somma(num1,num2))
    case '-':
        print(u.sottrazione(num1,num2))
    case '*':
        print(u.moltlipicazione(num1,num2))
    case '/':
        print(u.divisione(num1,num2))
    case 'no':
        menuAperto = False
    case _:
        print('scelta non valida')    