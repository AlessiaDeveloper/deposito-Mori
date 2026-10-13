
# Esercizio 6 (Facile) @classmethod: 

# Crea una classe chiamata Animale. Questa classe deve avere:

# Un attributo di classe numero_animali, inizializzato a 0.

# Due attributi di istanza: nome e specie, passati al costruttore.

# Il costruttore deve incrementare numero_animali di 1 ogni volta che viene creato un nuovo animale.

# Un metodo di classe quanti_animali che stampi una stringa del tipo "Numero di animali creati: 'numero_animali'".

# Crea almeno 3 oggetti Animale e poi chiama quanti_animali direttamente dalla classe, senza usare nessuna delle istanze create.

class Animale:
    
    #variabile di classe impostata a 0
    numero_animali = 0
    
    #metodo costruttore
    def __init__(self, nome, specie):
        #qua stiamo definendo nel costruttore nome e specie
        self.nome = nome
        self.specie = specie
        #quando viene creato un nuovo animale, aggiungi uno
        Animale.numero_animali +=1
    
    
    #è necessario passare il parametro self
    @classmethod
    def quanti_animali(cls):
        print('Numero di animali creati:', Animale.numero_animali)
        

# Creazione di istanze degli animali passandogli  il nome e la specie
An1 = Animale('Porcospino', 'porcospino')
An2 = Animale('Capretta', 'capra')
An3 = Animale('Romeo', 'gatto')

Animale.quanti_animali()

# Esercizio 5 (Facile) @staticmethod: 

# Crea una classe chiamata Convertitore. Questa classe dovrebbe avere:

# Un metodo statico euro_in_dollari che accetti un importo in euro e restituisca il valore convertito in dollari, usando un tasso fisso di 1.08.

# Un metodo statico km_in_miglia che accetti una distanza in chilometri e restituisca il valore convertito in miglia, usando un fattore fisso di 0.621371.

# Testa la classe chiamando entrambi i metodi direttamente dalla classe, senza creare alcun oggetto.

class Convertitore:

        @staticmethod
        def euro_in_dollari(importo):
            #applico la formula per convertire in dollari
            print(importo * 1.08)
        
        @staticmethod
        def km_in_miglia(km):
            #applico la formula per convertire in miglia
            print(km * 0.621371)


C1 = Convertitore.km_in_miglia(18)
C2 = Convertitore.euro_in_dollari(180)
     
        