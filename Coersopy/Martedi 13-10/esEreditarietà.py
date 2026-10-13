# Classe base

class Animale:

#classe animale generico con parametri nome ed età che vengono passati al costruttore
    def __init__(self, nome:str, eta:int):

        self.nome = nome
        self.eta = eta

#metodo fai suono che si cambierà con il tipo di animale
    def fai_suono(self):

        print(f"{self.nome} fa suono generico.")


# Classe Leone derivata (eredita da Animale)

class Leone(Animale):

#sovrascrive il metodo del padre ruggendo
    def fai_suono(self):

        print(f"{self.nome} ruggisce!")

#suo metodo speciale che può fare solo leone    
    def corsa(self):
        print(f"{self.nome} sta correndo")    
        
class Giraffa(Animale):

#di nuovo stessa cosa ma ho cercato e il verso della giraffa è il landito ma non so coniugarlo penso sia landendo
    def fai_suono(self):

        print(f"{self.nome} fa un verso da giraffa!")

# mangia      
    def mangia(self):
        print(f"{self.nome} sta mangiando")
                 
class Gatto(Animale):

#sovrascrive il metodo del padre miagolando
    def fai_suono(self):

        print(f"{self.nome} miagola!")        
        
    def fusa(self):
        print(f"{self.nome} sta facendo le fusa") 



An1 = Leone("Simba", 2)
An2 = Giraffa("Corvette", 4)
An3 = Gatto("Duchessa", 3)

# An3.fusa()
# An2.fai_suono()
# An1.corsa()

# esecizio delle 12

class Prodotto:

#classe animale generico con parametri nome ed età che vengono passati al costruttore
    def __init__(self, nome:str, costo_produzione:int, prezzo_vendita:int):

        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

#metodo fai suono che si cambierà con il tipo di animale
    def calcola_profitto(self):

        print(self.prezzo_vendita - self.costo_produzione)



class Elettronica(Prodotto):

        def __init__(self, nome:str, costo_produzione:int, prezzo_vendita:int, garanzia):
        #per richiamare il costruttore visto che abbiamo in tutti e due i padri i costruttori, mettiamo il nome
            Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)   
        #sovrascrive il metodo del padre garanzia
            self.garanzia = garanzia
            
class Abbigliamento(Prodotto):

        def __init__(self, nome:str, costo_produzione:int, prezzo_vendita:int, materiale):
        #per richiamare il costruttore visto che abbiamo in tutti e due i padri i costruttori, mettiamo il nome
            Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)   
        #sovrascrive il metodo del padre materiale
            self.materiale = materiale

Prod1 = Prodotto('sedia', 70, 120)
Prod1.calcola_profitto()

#EXTRA
class Fabbrica:
        #variabile di classe impostata a 0
    inventario = []
    
    #metodo costruttore
    def aggiungi_prodotto(self):
        #qua dobbiamo metterci un prodotto che stiamo creando
        #qua vorrei mettere un if per controllare se il prodotto è elettronico o di abbigliamento
        scelta = input('il tuo prodotto è elettronico o  abbigliamento?')
        if scelta == 'elettronico':
            nome_prodotto = input('inserisci nome prodotto')
            costo_produzione = int(input('metti il costo di produzione'))
            prezzo_vendita = int(input('metti il costo di prezzo di vendita'))
            garanzia = int(input('inserisci gli anni di garanzia'))
            
        class Elettronica(Prodotto):
            
            
            
        #se il prodotto è elettronico allora crea un prodotto che eredita garanzia   
        self.inventario.append(prodotto)    
    
    