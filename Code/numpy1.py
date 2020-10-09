import numpy as np


a = np.array([1, 2, 3])
print (type(a))
print(a.shape) #stampa il numero di elementi di ogni dimensione
print(a[0], a[1], a[2]) #per stampare i 3 elementi


b = np.array([[1, 2, 3],[5, 6, 7],[7, 2, 4]])
print(b.shape) #stampa il numero di elementi di ogni dimensione


z = np.zeros((2,2)) #crea una matrice di zeri 2 righe 2 colonne
print(z)
