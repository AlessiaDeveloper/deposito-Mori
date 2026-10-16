# Esercizio: Sistema Astratto di Trasporto Merci
# Requisiti
# 1. Classe Astratta: VeicoloTrasporto
# Crea una classe astratta chiamata VeicoloTrasporto, che rappresenti un veicolo generico per il trasporto di merci.
# La classe deve contenere:
# Attributi comuni (protetti)
# • _targa : stringa
# • _peso_massimo : intero (capacità di carico in kg)
# • _carico_attuale : intero (inizialmente 0)
# Metodi
# • Un costruttore che inizializza i campi comuni.
# • Un metodo concreto:
# • carica(peso)
# • Aumenta il carico attuale se possibile, altrimenti segnala che il peso supera la capacità.
# • Un metodo concreto:
# • scarica()
# • Riporta il carico attuale a 0.
# • Un metodo astratto:
# • costo_manutenzione()
# • Ogni veicolo deve avere un costo di manutenzione calcolato secondo regole diverse.
# 2. Sottoclassi Concrete

# Crea almeno tre sottoclassi che estendono la classe astratta e implementano il metodo costo_manutenzione() secondo regole differenti:
# a) Camion
# • Attributo extra: numero_assi
# • Regola manutenzione (esempio):
# • 100 € per asse + 1 € per kg di carico massimo
# b) Furgone
# • Attributo extra: alimentazione (es. "diesel", "elettrico")
# • Regola manutenzione:
# • Se elettrico: 200 €
# • Se diesel: 150 €
# c) Motocarro
# • Attributo extra: anni_servizio
# • Regola manutenzione:
# • 50 € per ogni anno di servizio
# 3. Classe GestoreFlotta
# Crea una classe che gestisca un elenco di veicoli:
# Attributi
# • veicoli : lista di oggetti derivati da VeicoloTrasporto.
# Metodi
# • aggiungi_veicolo(veicolo)
# • rimuovi_veicolo(targa)
# • costo_totale_manutenzione():
# • Somma dei costi di manutenzione di tutti i veicoli (polimorfismo sugli oggetti astratti).
# • stampa_veicoli():
# • Elenca targa, tipo e carico attuale.

from abc import ABC,abstractmethod


class VeicoloTrasporto(ABC):
    

    def __init__(self, _targa:'str',_peso_massimo:int,_carico_attuale:int):
        self._targa = _targa
        self._peso_massimo = _peso_massimo
        self._carico_attuale = _carico_attuale

# • Un metodo concreto:
# • carica(peso)
    def carica():
        caricoAggiunto = int(input('aggiungi del carico'))
# • Aumenta il carico attuale se possibile, altrimenti segnala che il peso supera la capacità.
        # if carico_attuale
# • Un metodo concreto:
    def scarica():
        caricoAggiunto = int(input('togli dal carico'))    
# • scarica()    
    @abstractmethod   
#metodo astratto con corpo vuoto
    def costo_manutenzione(self):
        pass   
    
    
class Camion(VeicoloTrasporto):
     
    
    def __init__(self, __targa:'str',__peso_massimo:int,__carico_attuale:int, numero_assi):
        VeicoloTrasporto.__init__(self, __targa, __peso_massimo, __carico_attuale)
        self._targa = __targa
        self._peso_massimo = __peso_massimo
        self._carico_attuale = __carico_attuale
        
        self.numero_assi = numero_assi
        
    def get_targa(self):
        return self .__targa

    def set_targa(self, targa):
        pass

    def get_peso_massimo(self):
        pass

    def set_peso_massimo(self, peso_massimo):
        pass

    def get_carico_attuale(self):
        pass

    def set_carico_attuale(self, carico_attuale):
        pass
# • Attributo extra: numero_assi
# • Regola manutenzione (esempio):
# • 100 € per asse + 1 € per kg di carico massimo       
    def costo_manutenzione(self):
        assiTotali = int(input('quanti assi hai? '))
        chiliCarico = int(input('quanti chili di carico stai trasportando? '))

        costoAssi = assiTotali * 100
        print(costoAssi + chiliCarico)
        
class Furgone(VeicoloTrasporto):
     
    
    def __init__(self, __targa:'str',__peso_massimo:int,__carico_attuale:int, alimentazione):
        VeicoloTrasporto.__init__(self, __targa, __peso_massimo, __carico_attuale, alimentazione)
        self._targa = __targa
        self._peso_massimo = self.__peso_massimo
        self._carico_attuale = self.__carico_attuale
        
  
    # • Attributo extra: alimentazione (es. "diesel", "elettrico")
# • Regola manutenzione:
# • Se elettrico: 200 €
# • Se diesel: 150 €    
        self.alimentazione = alimentazione

    def costo_manutenzione(self):
        alimentazione = input('seleziona se va a diesel o elettrico ')
        if alimentazione == 'diesel':
            costoAlimentazione = 150
        else:
            costoAlimentazione = 200  
        chiliCarico = int(input('quanti chili di carico stai trasportando? '))
        
        print(costoAlimentazione + chiliCarico)        
        
        
class Motocarro(VeicoloTrasporto):
     
    
    def __init__(self, __targa:'str',__peso_massimo:int,__carico_attuale:int, anni_servizio):
        VeicoloTrasporto.__init__(self, __targa, __peso_massimo, __carico_attuale, anni_servizio)
        self._targa = __targa
        self._peso_massimo = __peso_massimo
        self._carico_attuale = __carico_attuale
        
        self.anni_servizio = anni_servizio
    
# • Attributo extra: anni_servizio
# • Regola manutenzione:
# • 50 € per ogni anno di servizio            
    def costo_manutenzione(self):
        anniServizio = int(input('seleziona se va a diesel o elettrico '))
        costoAnni = anniServizio * 50
        chiliCarico = int(input('quanti chili di carico stai trasportando? '))
        
        print(costoAnni + chiliCarico)        
        

camion1 = Camion("Miao", 100, 35, 10)
camion1.costo_manutenzione()   

# 3. Classe GestoreFlotta
# Crea una classe che gestisca un elenco di veicoli:
# Attributi
# • veicoli : lista di oggetti derivati da VeicoloTrasporto.
# Metodi
# • aggiungi_veicolo(veicolo)
# • rimuovi_veicolo(targa)
# • costo_totale_manutenzione():
# • Somma dei costi di manutenzione di tutti i veicoli (polimorfismo sugli oggetti astratti).
# • stampa_veicoli():
# • Elenca targa, tipo e carico attuale.


class GestoreFlotta:
    
    listaVeicoli = [] #classe vuota
    
    def aggiungi_veicolo():
        veicolo = input('aggiungi un veicolo tra camion')
        if veicolo == camion
    
    def rimuovi_veicolo(targa):
        pass
    
    def costo_totale_manutenzione():
        pass
    
    def sommaManutenzioneVeicoli():
        pass
    def stampaVeicoli():
        pass
    def mostraInfo():
        pass