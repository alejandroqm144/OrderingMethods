

import random
import time

numb = [random.randint(2, 100) for _ in range(8)]
print("Lista de números aleatorios: ")
print(numb)
print(" ")
time.sleep(2.5)

def insertion_sort(numb):
    for i in range(1, len(numb)):
        key = numb[i]
        j = i - 1
        while j >= 0 and key < numb[j]:
            numb[j + 1] = numb[j]
            j -= 1
        numb[j + 1] = key
    return numb

n = insertion_sort(numb)

print("Lista ordenada por método de Inserción: ")
print(n)
print(" ")
time.sleep(2.5)
