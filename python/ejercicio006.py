#Ingrese un numero y diga si es par o impar

num1 = int(input("Ingrese un numero: "))

if (num1 == 0) :
    print("cero")
elif (num1 % 2 == 0) :
    print("numero es par")
else :
    print("numero es impar")  