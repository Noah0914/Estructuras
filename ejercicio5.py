import random

def arreglo_restringido(n):
    arr = []
    for i in range(n):
        if i == 0:
            arr.append(random.randint(1, 9))
        else:
            limite = ((arr[-1] // 10) + 1) * 10
            num = random.randint(arr[-1]+1, limite)
            arr.append(num)
    return arr

def ejercicio5():
    n = int(input("Ingrese cantidad de elementos: "))
    print("Arreglo restringido:", arreglo_restringido(n))

ejercicio5()