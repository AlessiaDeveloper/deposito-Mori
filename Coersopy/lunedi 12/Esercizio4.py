# Crea una classe chiamata Garage. Questa classe dovrebbe avere:

# Un attributo di istanza capienza (numero massimo di auto) passato al costruttore.

# Un attributo di istanza auto_presenti (lista di stringhe con le targhe), inizialmente vuota.

# Un metodo parcheggia che accetti una targa e aggiunga l'auto alla lista. Se il garage è pieno, stampa un messaggio di errore. Se la targa è già presente, 
# avvisa che l'auto è già in garage.

# Un metodo rimuovi che accetti una targa e rimuova l'auto corrispondente. Se la targa non è presente, stampa un messaggio di errore.

# Un metodo posti_liberi che restituisca il numero di posti ancora disponibili.

# EXTRA Un metodo statico formato_targa_valido che accetti una stringa e restituisca True se la targa rispetta il formato italiano 
# (2 lettere, 3 numeri, 2 lettere — es. "AB123CD"), False altrimenti. Suggerimento: si può usare il metodo .isalpha() e .isdigit() sulle sottostringhe.

# EXTRA Il metodo parcheggia deve usare formato_targa_valido per rifiutare targhe non valide prima di aggiungerle.



class Garage:
    
    def __init__(self,capienza,auto_presenti):
        self.auto_presenti = auto_presenti
        self.capienza = capienza
        #lista vuota in cui andranno messe le auto
        self.lista_auto_presenti = []
     
        
    def parcheggia(self):
        
        #chiede all'utente di aggiungere la targa dell'auto
        targa = input('inserisci il nome della targa')
        
        #assegno a numeroAuto un valore di tipo int con all interno il numero di elementi all'nterno della lista
        numeroAuto = len(self.lista_auto_presenti)
        
        #se gli elementi della lista sono maggiori della capienza del garage stampo errore
        if numeroAuto >= self.capienza:
            print('non è possibile parcheggiare qui')
        
        #se targa è già presente in lista auto presenti
        elif targa in self.lista_auto_presenti:
            print('auto già presente')
        
        #altrimenti la appendo in fondo alla lista, e aggiorno il numero di auto presenti
        else:
            self.lista_auto_presenti.append(targa)
            self.auto_presenti +=1
            
        
    def rimuovi(self):
        rimuovi_targa = input('inserisci il nome della targa per rimuovere la macchina')
        #se la targa non è già dentro la lista stampo un errore
        if rimuovi_targa not in self.lista_auto_presenti: 
            print('errore auto non presente nel parcheggio')
        #altrimenti rimuovo la targa e aggiorno la lista auto togliendo uno
        else:
            self.lista_auto_presenti.remove(rimuovi_targa)
            self.auto_presenti -=1
        
    def posti_liberi(self):
        # printa i posti ancora disponibili. Quindi bisogna fare capienza - auto_presenti
        return self.capienza - self.auto_presenti

        
Garage1 = Garage(10,0)

print(Garage1.auto_presenti)
Garage1.parcheggia()
print(Garage1.auto_presenti)
Garage1.rimuovi()
print(Garage1.auto_presenti)
print(Garage1.posti_liberi())


