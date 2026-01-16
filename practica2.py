'''
practica2.py
crear un programa que tena un menu con las siguientes opciones: 
1. suma 
2.- resta 
3.- multiplicacion
4.- division 
5.- salir 

cada opcion deber ser una funcion diferente 
'''
def suma():
    a = int(input("Ingrese el primer numero para sumar: "))
    b = int(input("Ingrese el segundo numero para sumar: "))
    return a + b

def resta ():
    a = int(input("Ingrese el primer numero para restar: "))
    b = int(input("Ingrese el segundo numero para restar: "))
    return a - b

def multiplicacion():
    a = int(input("Ingrese el primer numero para multiplicar: "))
    b = int(input("Ingrese el segundo numero para multiplicar: "))
    return a * b

def division():
    a = int(input("Ingrese el primer numero para dividir: "))
    b = int(input("Ingrese el segundo numero para dividir: "))
   
    return a / b

def salir(): 
     exit()
   

while True:
        print("Menu de operaciones:")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicacion")
        print("4.- Division")       
        print("5.- Salir")

        opcion = input("Seleccione una opcion (1-5): ")
        if opcion == '1':
               print("El resultado de la suma es:", suma())
        elif opcion == '2':
              print("El resultado de la resta es:", resta())
        elif opcion == '3':
              print("El resultado de la multiplicacion es:", multiplicacion())
        elif opcion == '4':
              print("El resultado de la division es:", division())
        elif opcion == '5':
              salir()