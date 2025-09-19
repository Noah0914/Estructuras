import random

def generar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]

def suma(arr):
    return sum(arr)

def promedio(arr):
    return sum(arr)/len(arr)

def mayor(arr):
    return max(arr)

def menor(arr):
    return min(arr)

def comparar_arreglos(arr1, arr2):
    suma1, suma2 = suma(arr1), suma(arr2)
    mayor1, mayor2 = mayor(arr1), mayor(arr2)
    menor1, menor2 = menor(arr1), menor(arr2)
    prom1, prom2 = promedio(arr1), promedio(arr2)

    print("Arreglo 1:", arr1)
    print("Arreglo 2:", arr2)

    print("a) Suma más alta:", "Arreglo 1" if suma1 > suma2 else "Arreglo 2")
    print("b) Mayor:", max(mayor1, mayor2))
    print("c) Menor:", min(menor1, menor2))

    prom_conjunto = (suma1 + suma2) / (len(arr1) + len(arr2))
    print("d) Promedio conjunto:", prom_conjunto)

    print("e) Promedio Arreglo 1:", prom1, "->", "Encima" if prom1 > prom_conjunto else "Debajo")
    print("   Promedio Arreglo 2:", prom2, "->", "Encima" if prom2 > prom_conjunto else "Debajo")

    pares1 = sum(1 for x in arr1 if x % 2 == 0)
    pares2 = sum(1 for x in arr2 if x % 2 == 0)
    print("f) Mayor cantidad de pares:", "Arreglo 1" if pares1 > pares2 else "Arreglo 2")

    imp1, imp2 = len(arr1)-pares1, len(arr2)-pares2
    print("g) Mayor cantidad de impares:", "Arreglo 1" if imp1 > imp2 else "Arreglo 2")

def ejercicio2():
    n = int(input("Ingrese cantidad de elementos: "))
    arr1, arr2 = generar_arreglo(n), generar_arreglo(n)
    comparar_arreglos(arr1, arr2)

ejercicio2()