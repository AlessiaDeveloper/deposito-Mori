# #Esercizio 1 (Facile):

# #Crea una classe chiamata Punto. 
# #Questa classe dovrebbe avere:
# #Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
# # Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
# # Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano.

# # class Punto():
# #     def __init__(self, x:int, y:int):
# #         self.x =x
# #         self.y=y
    
# #     def muovi(self, dx:int, dy:int):
# #         dx = int(input('inserisci le coordinate del punto dx'))
# #         dy = int(input('inserisci le coordinate del punto dx'))
# #         x = dx
# #         x = dy
# #         print(x)
        
# # Punto1 = Punto()

# # print(Punto1.x)
# # print(Punto1.y)

# # print(Punto1.muovi())

# # print(Punto1.x)
# # print(Punto1.y)




# # Esercizio 2 (Facile):

# # Crea una classe chiamata Libro. 

# # Questa classe dovrebbe avere:

# # Tre attributi: titolo, autore e pagine.

# # Un metodo descrizione che restituisca una stringa del tipo "Il
# # libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".


# # Extra: permetti di creare quanti libri vuole l’utente


# class Libro():
    
#     def __init__(self, titolo, autore, pagine):
#         self.titolo = titolo
#         self.autore = autore
#         self.pagine = pagine
        
#     def stampa_info(self, titolo, autore, pagine):
#         print(self.titolo, self.autore, self.pagine)

# compilalibri = True
    
# def creaLibri(self,titolo,autore,pagine)
# #definiamo le variabili da tenere fuori dal while
#     while compilalibri:
#         #chiediamo all utente di inserire titolo autore e pagine
#         #chiediamo all'utente se vuole inserire un altro libro se no usciamo dal while
#         self.titolo = input('inserisci il titolo')
#         break
        
    
#---------------------------------------ES1

class punto:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "ciao sono un str"
        
    def muovi_punti(self, dx, dy):
        self.x= dx
        self.y= dy
        
    def distanza_ordigine(self):
        return self.x, self.y


'''x = input()
y = input()

punto_mio = punto(x,y)
print(punto_mio)'''


#---------------------------------------ES2

class libro:
    
    def __init__(self, pagine, autore, titolo):
        self.pagine = pagine
        self.autore = autore
        self.titolo = titolo
        
    def stampa_libro(self):
        return self.autore, self.pagine, self.titolo

scelta = ""
lista_libri = []
while scelta != "end" :
    
    in1 = input("pagine?")
    in2 = input("autore?")
    in3 = input("titolo?")
    
    Obj = libro(in1,in2,in3)
    print(Obj.stampa_libro())
    lista_libri.append(Obj)
    
   
    scelta= input("vuoi continuare?")
    
for i in lista_libri:
    
    print(i.stampa_libro())
    




        
    