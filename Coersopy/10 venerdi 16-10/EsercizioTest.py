class Elettrodomestico:
#costruttore
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str):
        self._marca = marca
        self._modello = modello
        self._anno_acquisto= anno_acquisto
        self._guasto = guasto

#getter e setter    

#metodo che descrive il prodotto
    def descrizione(self):
        print(self._marca(), self._modello(), self._anno_acquisto(),self._get_guasto())

    def stima_costo_base(self):
        #da un valore numerico in base al tipo di elettrodomestico
        pass
    
elettr1 = Elettrodomestico('Hp', 'modello1', 2014, 'ha un problema con nonso')
# print(elettr1.descrizione())
    
class Lavatrice(Elettrodomestico):
    def __init__(self, __marca:str, __modello:str, __anno_acquisto:int, __guasto:str, capacita_kg:int,giri_centrifuga:int):
        super().__init__(self, __marca, __modello, __anno_acquisto)
        #attributi passati da protetti a privati
        self._marca = __marca
        self._modello = __modello
        self._anno_acquisto = __anno_acquisto
        self._guasto = __guasto
        
        #attributi lavatrice
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga
    
    #getter e setter    
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        modMarca = input('scrivi il nuovo nome della marca')
        self.__marca = modMarca

    def get_modello(self):
        return self.__modello

    def set_modello(self, modello):
        pass

    def get_anno_acquisto(self):
        #da fare controllo per vedere che l'anno non è nel futuro
        return self.__anno_acquisto

    def set_anno_acquisto(self, anno_acquisto):
        pass

    def get_guasto(self):
        return self.__guasto

    def set_guasto(self, guasto):
        pass    

#   @override  
        
    def stima_costo_base(self):
        #variabile che mettiamo per segnare che per ogni kilo ci sono 10 euro in piu di riparazione
        kg = 10
        costoBase = 150
        costo = self.capacita_kg * kg
        somma = costoBase + costo
        return somma
    
Lava1= Lavatrice('Hp', 'modello1', 2014, 'ha un problema con nonso', 10, 180)

print('il costo della riparazione della sua lavatrice è di euro', Lava1.stima_costo_base() )

class Frigorifero(Elettrodomestico):
    def __init__(self, __marca:str, __modello:str, __anno_acquisto:int, __guasto:str, litri:int,ha_freezer:bool):
        super().__init__(self, __marca, __modello, __anno_acquisto)
        #attributi passati da protetti a privati
        self._marca = __marca
        self._modello = __modello
        self._anno_acquisto = __anno_acquisto
        self._guasto = __guasto
        
        #attributi lavatrice
        self.litri = litri
        self.ha_freezer = ha_freezer
    
    #getter e setter    
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        modMarca = input('scrivi il nuovo nome della marca')
        self.__marca = modMarca

    def get_modello(self):
        return self.__modello

    def set_modello(self, modello):
        pass

    def get_anno_acquisto(self):
        #da fare controllo per vedere che l'anno non è nel futuro
        return self.__anno_acquisto

    def set_anno_acquisto(self, anno_acquisto):
        pass

    def get_guasto(self):
        return self.__guasto

    def set_guasto(self, guasto):
        pass    

#   @override  
        
    def stima_costo_base(self):
        #variabile che mettiamo per segnare che per ogni kilo ci sono 10 euro in piu di riparazione
        costoBase = 150
        costosup = 0
        
        #se il frigo ha il freezer supplemento di 100 euro ma i litri non superano i 200
        if self.ha_freezer == True & self.litri <= 200:
            costoBase = costoBase +100
            
        elif self.ha_freezer == False & self.litri > 200:   
        else:
            costosup = 0

        #i litri massimi son 200
        if self.litri <= 200 :
            costoBase = 150
        else:
            costoBase = 230

        if ha_freezer == True:
            costoTotale = costoBase+ costosup
            return costoTotale
        else:
            return costoBase
        
        #
Frigo1 = Frigorifero('Samsung', 'Bu', 1999, 'bu2', 150, True)
print('il costo della riparazione del suo frigo è di euro', Frigo1.stima_costo_base() )
