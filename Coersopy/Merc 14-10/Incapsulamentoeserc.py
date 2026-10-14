# # Classe ContoBancario:

# # Attributi privati:

# # __titolare (stringa che rappresenta il nome del titolare del conto)

# # __saldo (decimale che rappresenta il saldo del conto)

# # Metodi pubblici:

# # deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.

# # preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.

# # visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.

# # Gestione dei Metodi e Sicurezza:

# # I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).

# # Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate 
# # (e.g., il titolare deve essere una stringa non vuota)

# class ContoBancario:

#     __titolare = ""
#     __saldo = 0
    
#     #costruttore 
#     def __init__(self, titolare, saldo):
            
#         self.__titolare = titolare
#         self.__saldo = saldo     
#         # getter e setter
#     def get_titolare(self):
#         return self.__titolare
#     def set_titolare(self):
#         sceltaTitolare = input('scegli nome titolare')
#         self.__titolare = sceltaTitolare
#     def set_saldo(self, importo ):
#         self.__saldo += importo
#         print(self.__saldo)
#     def get_saldo(self):
#         return self.__saldo
    
    
#    #metodi pubblici
   
#     def deposita(self):
#         scelta_saldo = int(input('sceldi la cifra da prelevare'))
#         self.set_saldo(scelta_saldo)

            
#     # def preleva():

        
#     # visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
    
#     def visualizza_saldo(self):
#         return self.get_saldo()
    
        
# #Persona1


# ESERCIZIO 2 SCUOLA ------------------------

# Sistema di gestione studenti

# Immagina di dover creare un sistema di gestione per una scuola che deve mantenere le informazioni sugli studenti, i professori e
# le lezioni. Seguendo il paradigma della programmazione orientata agli oggetti (OOP), dovrai implementare le classi necessarie
# usando incapsulamento, ereditarietà .


# Specifiche

# Classe Persona:

# Crea una classe base chiamata Persona che rappresenti una persona generica.

# Attributi:

# nome: stringa

# eta: intero

# Metodi:

# __init__(self, nome, eta): costruttore che inizializza nome ed eta.

# presentazione(self): metodo che stampa una frase con il nome e l'età della persona.

# Classe Studente:

# Crea una sottoclasse di Persona chiamata Studente.

# Attributi:

# voti: lista di interi che rappresentano i voti dello studente.

# Metodi:

# __init__(self, nome, eta, voti): costruttore che inizializza il nome, l'età e i voti dello studente.

# calcola_media(self): metodo che restituisce la media dei voti.

# Override del metodo presentazione(self) per includere la media dei voti nella presentazione.

# Classe Professore:

# Crea una sottoclasse di Persona chiamata Professore.

# Attributi:

# materia: stringa che rappresenta la materia insegnata.

# Metodi:

# __init__(self, nome, eta, materia): costruttore che inizializza il nome, l'età e la materia insegnata dal professore.

# Override del metodo presentazione(self) per includere la materia nella presentazione.

class Persona:
    
    #attributi
    
    
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta=eta

    def presentazione(self):
        print(f"Sono{self.nome}, eta {self.eta}")
        
        

class Studente(Persona):
    
    __voti = []
    
    #costruttore
    def __init__(self, nome, eta, __voti):

        Persona.__init__(self, nome, eta)  

        self.__voti = __voti
        
    def get_voti(self):
        return self.__voti
    def set_voti(self):
        votoIta= int(input('inserisci il voto che hai in italiano'))
        self.__voti.append(votoIta)
        votoMate= int(input('inserisci il voto che hai in matematica'))
        self.__voti.append(votoMate)
        votoScie= int(input('inserisci il voto che hai in scienze'))
        self.__voti.append(votoScie)
        return self.voti
               
           
    #funzione per modificare i voti

    def calcola_media(self):
        media= sum(self.__voti) / len(self.__voti)
        return media

    def presentazione(self):

        print(f"Sono {self.nome}, eta {self.eta} e la media dei voti è {self.calcola_media()} ")
    

        
class Professore(Persona):
    
    #attributi
    __materia_insegnata = ""
    
    def __init__(self, nome, eta, __materia_insegnata):

        Persona.__init__(self, nome, eta)  

        self.__materia_insegnata = __materia_insegnata
        
    def get_materia_insegnata(self):
        return self.__materia_insegnata
    def set_materia_insegnata(self):
        materia_insegnataN = input('qual è la materia che insegni?')
        materia_insegnata = materia_insegnataN
        return materia_insegnata
        
    def presentazione(self):
        self.get_materia_insegnata()
        print(f"Sono {self.nome}, eta {self.eta} e la materia che insegno è {self.__materia_insegnata} ") 
        
        
Per1 = Professore('Italo', 45, 'scienze')       
print(Per1.presentazione())
Alu1 = Studente('Gennaro',15, [8,7,8] ) 
print(Alu1.presentazione())


    