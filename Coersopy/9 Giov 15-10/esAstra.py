from abc import ABC,abstractmethod

#classe padre classe astratta
class Impiegato(ABC):
    
    def __init__(self, nome,cognome,stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio
    
    @abstractmethod   
    def calcola_stipendio(self):
        #metodo astratto con corpo vuoto
        pass

# classe figlio1

class ImpiegatoFisso(Impiegato):
    
    def calcola_stipendio(self):
        print(self.stipendio)
        
class ImpiegatoAProvvigione(Impiegato):
    #assegno a provvigione un valore  che andrà a essere sommato in cui effettuo il calcola stipendio
    provvigione = 100
    def __init__(self, nome, cognome, stipendio, provvigione):
        Impiegato.__init__(self, nome, cognome, stipendio)
        
        self.provvigione = provvigione
    
    
    
    def calcola_stipendio(self):
        print(self.stipendio + self.provvigione)
    #prove
Ab = ImpiegatoFisso('Allo', 'MAllo', 2300)
Ab.calcola_stipendio()


def esegui(o):
    o.calcola_stipendio()
    
esegui(Ab)