# overriding dei metodi sovrascrittura------------

class Animale:

    def emetti_suono(self):

        print("Questo animale fa un suono")


class Cane(Animale):

    def emetti_suono(self):

        print("Bau")


class Gatto(Animale):

    def emetti_suono(self):

        print("Miao")
        
# SImulazione di overloading ----------------------
#la variabile a e la variabile b possono avere comportamenti diversi in base a cosa sono

class Stampa:

    def mostra(self, a=None, b=None):

        if a is not None and b is not None:

            print(a + b)

        elif a is not None:

            print(a)

        else:

            print("Niente da mostrare")
            
# DUck Typing-------------------------------------- 


class Cerchio:

    def disegna(self):

        print("Disegno un cerchio")


class Rettangolo:

    def disegna(self):

        print("Disegno un rettangolo")


def disegna_figura(figura):

    # Anche qui, basta che 'figura' abbia il metodo 'disegna'

    figura.disegna()


figure = [Cerchio(), Rettangolo()]     # figure[0]=Cerchio() / figure[1]=Rettagolo()


# Iteriamo e disegniamo ogni figura

for figura in figure:

    disegna_figura(figura)

# FUNZIONE built-in len() -----------------------------

# Lista

print(len([1, 2, 3]))  # Output: 3


# Stringa

print(len("Ciao"))     # Output: 4


# Dizionario

print(len({"a": 1, "b": 2}))  # Output: 2


