import random

def arreglo_sin_repetidos(n):
    arr = []
    while len(arr) < n:
        num = random.randint(1, 100)
        if num in arr:
            print(f"Repetido -> {num}")
        else:
            arr.append(num)
    return arr

def ejercicio4():
    n = int(input("Ingrese cantidad de elementos: "))
    print("Arreglo sin repetidos:", arreglo_sin_repetidos(n))

ejercicio4()