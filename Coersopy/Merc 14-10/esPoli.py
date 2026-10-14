#è tutto rotto

class MetodoPagamento:

    def __init__(self, importo):

        self.importo = importo
    
    def effettua_pagamento():
        print('effettua pagamento')
    
class Paypal(MetodoPagamento):


    def effettua_pagamento(self):
        print("pagamento fatto con Paypal")
        
class CartaDiCredito(MetodoPagamento):



    def effettua_pagamento(self):

        print("pagamento fatto con CartaDiCredito")
        
    
class Bonifico(MetodoPagamento):

    def effettua_pagamento(self):

        print("pagamento fatto con Bonifico")
        

Pag1 = Bonifico(18)

print(Pag1.effettua_pagamento())


class GestorePagamenti(Pag1):
    #classe 

    def effettua_pagamento(istanza):
            istanza.effettua_pagamento()
            
    effettua_pagamento(Pag1)
    

# Pagamento1 = GestorePagamenti()
# print(Pagamento1)

    
