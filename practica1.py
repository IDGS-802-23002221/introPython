# opercion de multiplicacion de a * b utilizando sumas 
# a=3 
# b=4 
# salida: 3+3+3+3 = 12


resultado = 0 
tem = ""
i = 0 
a = 3 
b = 6

# mientras que i sea menor que b
while i < b: 
    tem += str (a) + "+"
    # sumar a al resultado 
    resultado += a
    # incrementar i en 1
    i += 1

# agregar = entre tem y el resultado
print(tem[:-1], " = ", resultado)

################################################# de aqui para abajo son ejercicios de practica :)
# Tienes un número llamado n

# Debes sumar todos los números desde 1 hasta n

# Usar únicamente while

# Al final debes mostrar la expresión completa y el resultado

# n = 10 
# suma = 0 
# i = 0 
# tem = ""

# while i < n: 
#     tem += str(i+1) + "+"
#     suma += (i+1)
#     i += 1
# print("la expresion es:", tem[:-1], " = ", suma)

###############################################
# imprime los numeros del 1 al 10 usando while 

# n = 1 
# while n <= 10: 
#     print(n)
#     n+=1
# print("fin del ciclo")    


########################################
# Imprime los números del 10 al 1 (en reversa).
# n = 10 
# while n >= 1: 
#     print(n)
#     n -= 1  

############################################
# Imprime solo los números pares del 1 al 20.
# x = 0 
# while x < 20:
#     x += 2
#     print(x)

############################################
# Calcula la suma de los números pares del 1 al 100.























