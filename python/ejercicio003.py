#area y perimetro de un triangulo
print("Programa que calcula el area y perimetro de un triangulo")

base = int(input("Ingrese la base del triangulo: "))

altura = int(input("Ingrese la altura del triangulo: "))

lado = int(input("Ingrese un lado del triangulo: "))

#CALCULOS
perimetro = ((base*altura)/2) 
area = base+lado+lado

print("El area del triangulo es: ")
print(area)
print("El perimetro del triangulo es: ")
print(perimetro)