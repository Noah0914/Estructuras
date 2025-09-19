import random
import statistics

def generar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]

def imprimir_arreglo(arr):
    print("Arreglo:", arr)

def suma(arr):
    return sum(arr)

def promedio(arr):
    return sum(arr)/len(arr)

def mayor(arr):
    return max(arr)

def menor(arr):
    return min(arr)

def ordenar_asc(arr):
    return sorted(arr)

def ordenar_desc(arr):
    return sorted(arr, reverse=True)

def moda(arr):
    try:
        return statistics.mode(arr)
    except statistics.StatisticsError:
        return "No hay moda"

def mediana(arr):
    return statistics.median(arr)

def buscar(arr, num):
    return [i for i, val in enumerate(arr) if val == num]

def ejercicio1():
    n = int(input("Ingrese la cantidad de elementos: "))
    arreglo = generar_arreglo(n)

    while True:
        print("\nMENÚ EJERCICIO 1")
        print("a. Imprimir arreglo original")
        print("b. Suma")
        print("c. Promedio")
        print("d. Mayor")
        print("e. Menor")
        print("f. Ordenar ascendente")
        print("g. Ordenar descendente")
        print("h. Moda")
        print("i. Mediana")
        print("j. Buscar número")
        print("k. Salir")
        opcion = input("Elija una opción: ").lower()

        if opcion == "a":
            imprimir_arreglo(arreglo)
        elif opcion == "b":
            print("Suma:", suma(arreglo))
        elif opcion == "c":
            print("Promedio:", promedio(arreglo))
        elif opcion == "d":
            print("Mayor:", mayor(arreglo))
        elif opcion == "e":
            print("Menor:", menor(arreglo))
        elif opcion == "f":
            print("Ascendente:", ordenar_asc(arreglo))
        elif opcion == "g":
            print("Descendente:", ordenar_desc(arreglo))
        elif opcion == "h":
            print("Moda:", moda(arreglo))
        elif opcion == "i":
            print("Mediana:", mediana(arreglo))
        elif opcion == "j":
            num = int(input("Ingrese número a buscar: "))
            pos = buscar(arreglo, num)
            if pos:
                print(f"El número {num} está en posiciones {pos} ({len(pos)} vez/veces).")
            else:
                print("No se encontró.")
        elif opcion == "k":
            break
        else:
            print("Opción inválida.")
ejercicio1()