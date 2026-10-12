#esempio

class Mirko():
    
    #metodo costruttore
    #init sta per inizializzazione
    def __init__(self, eta):
        #qua stiamo definendo nel costruttore l'età
        self.eta = eta
    
    #variabile di classe
    nome= 'Mirko'
    
    #è necessario passare il parametro self
    def saluta(self):
        return('ciao')
    
#inizializzazione dell'oggetto tramite il costruttore e devi dargli i valori che si aspetta, definiti tramite costruttore      
Ogg1 = Mirko(36)

print(Ogg1.nome)
print(Ogg1.saluta())
print(Ogg1.eta)

#ESEMPIO 2


#dichiaro la classe
class Automobile:
    
    #attributo di classe
    numero_di_ruote = 4
    
    #metodo costruttore
    def __init__(self, marca, modello):
        
        #attributo di istanza
        self.marca = marca
        
        #attributo di istanza
        self.modello = modello
    
    #metodo di istanza   
    def stampa_info(self):
        print('l automobile è una', self.marca, self.modello)
        
Auto1 = Automobile('Chevrolet', 'Corvette')

Auto1.stampa_info()


#ESEMPIO DI METODO STATICO


class Calcolatrice:
    
    @staticmethod
    def somma(a,b):
        return a + b
    
#uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5,3)

print(risultato)

#ESEMPIO DI METODO DECORATO
#Il metodo mostra_numero_istanze è un metodo di classe e utilizza il decoratore
# @classmethod, il parametro cls rappresenta la classe stessa e permette di accedere ad attributi di classe.


class Contatore:
    numero_istanze = 0 #Attributo di classe
    
    def __init__(self):
        Contatore.numero_istanze +=1
        
    @classmethod
    def mostra_numero_istanze(cls):
        print('sono state create:', cls.numero_istanze, 'istanze.')
        
# Creazione di istanze
C1 = Contatore()
C2 = Contatore()

Contatore.mostra_numero_istanze()