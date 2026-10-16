# class parametri_privati():
#     __nome = 'Donut'
    
#     def __init__(self,nome):
#         self.__nome = nome
        
# O_pp = parametri_privati('mirko')

# print(O_pp.__nome)


#lvl_0
class x:
    #lvl_1
    def y():
        #lvl_2
        if True:
            #lvl_3
            pass
        
class Parametri_privati():
    
    # variabile privata
    __nome = "mirko"
    __sole = 'sole'
    
    # variabile protetta
    _protetto = ""
    
    def __init__(self, nome):
        
        self.__nome = nome     
    # getter e setter
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome_nuovo):
        if len(nome_nuovo) < 0 :
            print("sei un pippo")
        else:
            self.__nome = nome_nuovo
            
    # metodo privato
    def __metodo_privato(self):
        print("sono dentro")
    
O_pp = Parametri_privati("mirko")
O_pp = Parametri_privati("sole")

print(O_pp.get_nome())
O_pp.set_nome("Marco")
print(O_pp.get_nome())


print(O_pp._protetto)

class Computer:

 def __init__(self, nome_proc):

   self.__processore = nome_proc # Attributo privato


 def get_processore(self):

   return self.__processore


 def set_processore(self, processore):

   self.__processore = processore


pc = Computer("Intel i5")

print(pc.get_processore()) 

# Accede all'attributo privato tramite il getter

pc.set_processore("AMD Ryzen 5") 

# Modifica l'attributo privato tramite il setter

print(pc.get_processore())



# Variabile globale
numero = 10

def funzione_esterna():
# Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna (locale):", numero)

    def funzione_interna():
    # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)

    funzione_interna()

print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)