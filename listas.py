import random

# Generar lista aleatoria
cantidad = random.randint(5, 15)
vector = []
for i in range(cantidad):
    vector.append(random.randint(1, 100))

print("Lista generada:", vector)

# Búsqueda de un número
num_buscar = int(input("Digite el numero que desea buscar: "))

if num_buscar in vector:  # Verifica si esta
    print("El numero", num_buscar, "si esta en la lista.")
    cantidad_apariciones = vector.count(num_buscar)
    print("Aparece", cantidad_apariciones, "vez/veces.")

    # Mostrar las posiciones donde se encontró
    posiciones = []
    for i in range(len(vector)):
        if vector[i] == num_buscar:
            posiciones.append(i)
    print("Posiciones:", posiciones)

else:
    print("El numero", num_buscar, "no esta en la lista.")
