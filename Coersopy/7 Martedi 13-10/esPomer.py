#classe che raggruppa i giocatori
class Squadra:
    def __init__(self, nomeSquadra):
        self.nomeSquadra = nomeSquadra
         #una lista vuota a cui aggiungere i membri
        # self.team = team
        # team = []
        
#dobbiamo aggiungere i membri al team, quindi  creiamo una funzione che metta i membri dentro il team con l'append
#non so come appenderglielo ma forse sbaglio
    # def appendiGiocatore():
        
    #     team.append()
        
        

#classe padre di allenatore giocatore e assistente
class MembroSquadra:
    
    def __init__(self, nome, eta):

        self.nome = nome

        self.eta = eta
        
    def descrivi(self):
        #se il membrosquadra è
        if MembroSquadra == Allenatore:
            print(f"nome: {self.nome}, età: {self.eta}, anni di esperienza: {self.anni_di_esperienza}, nomeSquadra: {self.nomeSquadra}")

#membrosquadra è il padre di allenatore      
class Allenatore(MembroSquadra, Squadra):
    
    #prendo il costruttore del padre e ci aggiungo anni di esperienza
    def __init__(self, nome, eta, anni_di_esperienza, nomeSquadra):

        MembroSquadra.__init__(self, nome, eta)
        
        Squadra.__init__(self, nomeSquadra)
        #parametro nuovo
        self.anni_di_esperienza = anni_di_esperienza
    
    #metodo che spiega come sta andando la direzione dell'allenamento    
    def dirige_allenamento():
        print('dirige bene')
         
class Giocatore(MembroSquadra, Squadra):
    
    #prendo il costruttore del padre e ci aggiungo ruolo e numero maglia
    def __init__(self, nome, eta, ruolo, numero_maglia):

        MembroSquadra.__init__(self, nome, eta)
        
        #parametro nuovo
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
    
    #metodo che spiega come sta andando la direzione dell'allenamento    
    def gioca_partita(self):
        #può includere azioni specifiche
        if self.ruolo == 'attaccante':
            print('sta attaccando')
        elif self.ruolo == 'difensore':
            print('sta difendendo discretamente')
        else:
            print('ha parato un calcio di rigore')
            
        
class Assistente(MembroSquadra, Squadra):
    
    #prendo il costruttore del padre e ci aggiungo specializzazione
    def __init__(self, nome, eta, specializzazione):

        MembroSquadra.__init__(self, nome, eta)
        
        #parametro nuovo
        self.specializzazione = specializzazione
    
    #metodo che spiega come sta andando la direzione dell'allenamento    
    def supporta_team(self):
        if self.specializzazione == 'fisioterapista':
        #può includere azioni specifiche come massaggia i polpacci
            print('ripara strappi muscolari')
        else: 
            
            print('sta portando l acqua ai membri della squadra')
        
    
#almeno la classe funziona        
Ronaldo = Giocatore('Ronaldo', 35, 'attaccante', 15)
Ronaldo.gioca_partita()
print(Ronaldo.numero_maglia)

#Allenatore
All1 = Allenatore('Bandini', 65, 27, 'Gialli')
All1.descrivi()
