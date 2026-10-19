import numpy as np

#creazione arrai con arrarange con numeri da 10 a 50
arrarange = np.arange(10,50)
print(arrarange)
#cambio di foma da un unico array a 2 con 20 cifre ciascuno
reshaped_arr = arrarange.reshape((2,20))
print(reshaped_arr)



#stampare tipo di dati 
print("Tipo di dati:", reshaped_arr.dtype)


#cambio dei dati in float con la funzione astype
reshaped_arrfloat = reshaped_arr.astype(float)
#la verifica dell'array e del tipo di dati
print(reshaped_arrfloat)
print("Tipo di dati:", reshaped_arrfloat.dtype)

#vediamo la forma dell'array
print("Forma:", reshaped_arrfloat.shape)
