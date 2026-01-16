# pedir al usuario que ingrese 20 numero repetidos y sin repetir los almacenes en una lista y luego muestra la lista ordenada de menor a mayor,
# tambien nos diga cuantos son repetidos y cuantas veces se repitieron
# separalos entre pares e impares

listaNum = []
repeticiones = []
repeticionesaux = []
while True: 

    for i in range (1, 5):
        n = int(input(f"ingresa el numero {i}:"))
        listaNum.append(n)
    print("lista recibida: ", listaNum)
    
    listaNum.sort()
    print("la lista ordenada :", listaNum)

    for num in listaNum:
        repeticionesc = listaNum.count(num)
        if repeticionesc > 1 and num not in repeticiones:
            repeticiones.append(num)
            repeticionesaux.append(f"el numero{num} se repite {repeticionesc} veces")
            
            
    break  
print(repeticionesaux)