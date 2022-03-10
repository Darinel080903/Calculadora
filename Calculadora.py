print("=============")
print(" Calculadora ")
print("============= \n")


print("---Menu de Opciones--- \n")
print("1-Suma \n")
print("2-Resta \n")
print("3-Division \n")
print("4-Multiplicacion \n")
print("5-Potencia \n")
opt=int(input("Elija una opcion: "))

if opt == 1:
    dato1=float(input("Ingresa el primer numero: "))
    dato2=float(input("Ingresa el segundo numero: "))
    suma = dato1 + dato2
    print("Su resultado es: ", str (suma))

elif opt == 2:
    dato1=float(input("Ingresa el primer numero: "))
    dato2=float(input("Ingresa el segundo numero: "))
    resta= dato1 - dato2
    print("Su resultado es: ", str (resta))

elif opt == 3:
    dato1=float(input("Ingresa el primer numero: "))
    dato2=float(input("Ingresa el segundo numero: "))
    division= dato1 / dato2
    print("Su resultado es: ", str (division))

elif opt == 4:
    dato1=float(input("Ingresa el primer numero: "))
    dato2=float(input("Ingresa el segundo numero: "))
    multi= dato1 * dato2
    print("Su resultado es: ", str (multi))

elif opt == 5:
    dato1=int(input("Ingresa el numero base: "))
    dato2=int(input("Ingresa el numero de la potencia: "))
    potencia= dato1**dato2
    print("Su resultado es: ", str (potencia))

