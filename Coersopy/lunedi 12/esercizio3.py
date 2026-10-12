# Esercizio 3 (Medio): 

# Crea una classe chiamata ContoCorrente. Questa classe dovrebbe avere:

# Due attributi di istanza: intestatario e saldo (il saldo iniziale deve essere passato al costruttore, con valore di default 0).

# Un metodo deposita che accetti un importo e lo aggiunga al saldo. Se l'importo è negativo o zero, stampa un messaggio di errore senza modificare il saldo.

# Un metodo preleva che accetti un importo e lo sottragga dal saldo. Se il saldo non è sufficiente, stampa un messaggio di errore senza modificare il saldo.

# Un metodo stampa_saldo che stampi una stringa del tipo "Il saldo di 'intestatario' è: 'saldo' €".

class ContoCorrente:
        
        def __init__(self,intestatario,saldo):
            self.intestatario = intestatario
            self.saldo = saldo
            saldo= 0

        def deposita(self):
            nuovoSaldo = int(input('inserisci un saldo'))
            if nuovoSaldo <= self.saldo:
                print('errore, inserisci importo superiore a 0 euro')
            else:
                self.saldo = nuovoSaldo
                return self.saldo
        
        def preleva(self):
            prelievo_saldo = int(input('inserisci una cifra da prelevare'))
            if self.saldo <= prelievo_saldo:
                print('errore, saldo insufficiente')
            else:
                self.saldo = self.saldo - prelievo_saldo
                return self.saldo
        
        def stampa_saldo(self):
            print('il saldo di', self.intestatario, 'è di Euro', self.saldo)

Obj = ContoCorrente('Alessia',0)

print(Obj.saldo)
Obj.deposita()
print(Obj.saldo)
Obj.preleva()
print(Obj.saldo)
print(Obj.stampa_saldo())
scelta = ""

# menuAperto = True    
# while menuAperto:
#     scelta = input('vuoi fare un esercizio? se si rispondi con 1, 2, 3, 4, 5, 6, 7 altrimenti rispondi no: ')

#     match scelta:
#         case '1':
#             inserisciNumeroPositivo()
#         case '2':
#             creaLista()
#         case '3':
#             sommaIPari(creaLista())
#         case '4':
#             stampaIDispari(creaLista())
#         case '5':
#             checkPari(inserisciNumeroPositivo())
#         case '6':
#             pariL(creaLista())
#         case '7':
#             SommaSuprema(creaLista())
#         case 'no':
#             menuAperto = False
#         case _:
#             print('scelta non valida')     