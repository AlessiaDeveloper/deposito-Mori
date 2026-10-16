#classe padre


class Fabbrica:

    listaRegistro = []
    
        
# attributo listaRegistro = lista vuota in cui vengono messi i prodotti di giornata
        
        
    def aggiungiProdotto(self):
        #mi serve che dentro la lista ci sia un'altra lista con gli elementi nome  e quantità
        prodotto = input('inserisci nome prodotto')
        quantita = int(input('inserisci la quantità del prodotto'))
        self.listaRegistro.append(prodotto)
        print(self.listaRegistro)


class Prodotto(Fabbrica):

#sovrascirittura del costruttore con modifiche aggiungendo i nuovi attributi, che sono privati quindi regole del incapsulamento fatte
    def __init__(self, listaRegistro, nome, quantita):
        
        super().__init__(self, listaRegistro)
        
        self.__nome = nome
        self.__quantita = quantita
        
        def get_nome(self):
            pass

        def set_nome(self, nome):
            pass

        def get_quantita(self):
            pass

        def set_quantita(self, quantita):
            pass







#ma io devo inserire i prodotti ad esempio in aggiungi prodotto quindi il metodo dove deve stare?

    
        
        
# attributo listaRegistro = lista vuota in cui vengono messi i prodotti di giornata
        listaRegistro = []
menuAperto = True    
#il menù per scegliere un azione

Fabbrica1 = Fabbrica()

while menuAperto:
    scelta = input('Quale azione vuoi fare? 1 se vuoi aggiungere un prodotto, 2 visualizzare la produzione, 3 per cercare un prodotto, 4 per modificare la quantità, 5 per rimuovere il prodotto, 6 per calcolare il totale dei prezzi prodotti, 7 per uscire: ')

    match scelta:
        case '1':
            Fabbrica1.aggiungiProdotto()
            pass
        case '2':
            # visualizzaProdotto
            pass
        case '3':
            #cercaProdotto
            pass
        case '4':
            #modificaquantità
            pass
        case '5':
            #rimuoviProdotto
            pass
        case '6':
            # calcolatotprezzi
            pass            
        case '7':
            menuAperto = False            
        case _:
            print('scelta non valida')    
