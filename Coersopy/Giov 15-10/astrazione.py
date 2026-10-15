from abc import ABC,abstractmethod

class Pippi_Astratto(ABC):
    @abstractmethod
    
    def Metodo_obbligatorio(self):
        
        pass

class Pippi_reale(Pippi_Astratto):
    
    def Metodo_obbligatorio(self):
        print('sono reale')
        
        
Pr1 = Pippi_reale()
Pr1.Metodo_obbligatorio()