import os

def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a,b):
    return a + b

os.system('cls')
saludar("carlos")

os.system('pause')

def main():
    os.system('cls')
    saludar("juan")
    resultado_suma = sumar(5,7)
    print("la suma de 5 y 7 es:", resultado_suma)

    if __name__ == "__main__":
        main()  

