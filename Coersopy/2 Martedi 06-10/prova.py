print(" Configurato ")

numeri = [1, 2, 3, 4]
nomi = ['lulu', 'nida', 'gatto']
misto = [1, 2, 'ciao']
print(numeri[1])

numeri[1] = 18
print(numeri)

#mettiamo 27 alla fine della lista
numeri.append(27)

#vediamo la lunghezza della lista
print(len(numeri))

#inseriamo in una posizione specifica alla posizion 4 metti 75
numeri.insert(4, 75)



#rimuove il 27
numeri.remove(27)

#mette i numeri ordinati a contrario, cioè dal più grande al più basso
numeri.sort(reverse= True)

print(numeri)

#PRENDI SOLO IL 75

settantacinque = numeri[0]

print(settantacinque)

#clear rimuove gli elementi da una lista
dungeon = ['Carl', 'Donut']

dungeon.clear()
