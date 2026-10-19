import numpy as np
# Creazione di un array unidimensionale

arr = np.array([1, 2, 3, 4, 5])


# Creazione di un array bidimensionale

arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# ----------------------------------------------------------------------

# Utilizzo di alcuni metodi

#serve a sapere la forma di un determinato elemento 
#due elementi con forme diverse non collaborano tra di loro
#essendo in una tupla, dopo che li hai valorizzati rimangono così
print("Forma dell'array:", arr2d.shape)  # Output: (2,3)


print("Dimensioni dell'array:", arr2d.ndim)  # Output: 1

#serve a sapere di che tipo di dato è formato l'array
print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)


print("Numero di elementi:", arr.size)  # Output: 5


print("Somma degli elementi:", arr.sum())  # Output: 15


print("Media degli elementi:", arr.mean())  # Output: 3.0


print("Valore massimo:", arr.max())  # Output: 5


print("Indice del valore massimo:", arr.argmax()) 

#metodo arange, crea un array con il range
arrarange = np.arange(4)
print(arrarange)

#il reshape modifica la forma, se questa è possibile, ad esempio 6 elementi possono diventare due elementi da 3
arr1 = np.arange(6)
reshaped_arr = arr.reshape((2,3))
print(reshaped_arr)