#1
numPc =int(input('Scegli un numero'))
def indov(num:int):
    numero = num
    if numero > numPc:
        print('il numero è più alto')
    elif numero < numPc:
        print('il numero è più basso')
    else:
        print('numero azzeccato')
        #salviamo il numero se è quello giusto
        return numero
  
        
    
# while True:
    # indov(8)
    # x = 
    #     if numPc == numero:
    #         scelta = input(', hai azzeccato il numero, vuoi rigiocare? si o no? ')
    #         if scelta == 'no':
    #             break

#es 2

# scelta = int(input('scegli un numero'))
# def fibo(scelta):
#     for i in range(scelta):
