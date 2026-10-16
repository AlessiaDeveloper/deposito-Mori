# Classe base

class Animale:

    def __init__(self, nome):

        self.nome = nome


    def parla(self):

        print(f"{self.nome} fa suono generico.")


# Classe derivata (eredita da Animale)

class Cane(Animale):

#sovrascrive il metodo del padre
    def parla(self):

        print(f"{self.nome} abbaia!")


animale_generico = Animale("AnimaleGenerico")

cane = Cane("Fido")


animale_generico.parla()  # Output: AnimaleGenerico fa suono generico.

cane.parla()              # Output: Fido abbaia!

#ereditarietà multipla

class Veicolo:

 def __init__(self, marca, modello):

  self.marca = marca

  self.modello = modello


 def mostra_informazioni(self):

  print(f"Veicolo marca {self.marca}, modello {self.modello}")


class DotazioniSpeciali:

 def __init__(self, dotazioni):

  self.dotazioni = dotazioni


 def mostra_dotazioni(self):

  print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")
  
  #veicolo è piu imortante perché è messo in prima posizione
class AutomobileSportiva(Veicolo, DotazioniSpeciali):

#stiamo riscrivendo il costruttore perché vogliamo aggiungere un pezzo cioè i cavalli in questo caso
    def __init__(self, marca, modello, dotazioni, cavalli):
#per richiamare il costruttore visto che abbiamo in tutti e due i padri i costruttori, mettiamo il nome
        Veicolo.__init__(self, marca, modello)  

        # Alternativa a super per l'ereditarietà multipla

        DotazioniSpeciali.__init__(self, dotazioni)

        self.cavalli = cavalli


    def mostra_informazioni(self):

        super().mostra_informazioni()  

        # Chiamiamo il metodo della prima superclasse

        print(f"Potenza: {self.cavalli} CV")

#va a prendere quello del padre, ma se aveva sovrascritto mostra dotazioni, prendeva il suo non quello del padre
        self.mostra_dotazioni()  

        # Possiamo chiamare metodi di entrambe le superclassi
        
auto_sportiva = AutomobileSportiva("Ferrari", "F8", ["ABS", "Controllotrazione", "Airbag laterali"], 720)


auto_sportiva.mostra_informazioni()

#metodo __repr__------------------
class Studente:

    def __init__(self, nome, voto):

        self.nome = nome

        self.voto = voto


    def __repr__(self):

        return f"Studente(nome={self.nome}, voto={self.voto})"


s = Studente("Mario", 28)

print(s)   # Studente(nome=Mario, voto=28)

repr(s)    # "Studente(nome=Mario, voto=28)"

#__eq__

class Prodotto:

 def __init__(self, nome, prezzo):

   self.nome = nome

   self.prezzo = prezzo


 def __eq__(self, altro):

   return self.nome == altro.nome and self.prezzo == altro.prezzo


p1 = Prodotto("Penna", 2)

p2 = Prodotto("Penna", 2)


print(p1 == p2)


# __getattribute__------------------
class Persona:

    def __init__(self, nome, eta):

        self.nome = nome

        self.eta = eta


    def __getattribute__(self, attributo):

        print(f"Sto accedendo all'attributo: {attributo}")

        return super().__getattribute__(attributo)


p = Persona("Mario", 30)


# accesso agli attributi

print(p.nome)

print(p.eta)