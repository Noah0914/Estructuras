def fibonacci(n):
    arr = [0, 1]
    while len(arr) < n:
        arr.append(arr[-1] + arr[-2])
    return arr[:n]

def ejercicio3():
    n = int(input("¿Cuántos números de Fibonacci?: "))
    print("Serie Fibonacci:", fibonacci(n))

ejercicio3()