#programa que verifica si una palabra es palindromo

palabra = input("Ingrese una palabra para verificar si es palindromo \n")

if (palabra == palabra[::-1]):
    print("palindromo")
else:
    print("no es palindromo")