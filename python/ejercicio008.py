"""
string y mas!!!
"""
esto_es_una_string = "hola Jose Cordova como estas"
esto_es_otra_string = "hola mundo"

#concatenar
print(esto_es_una_string + '' + esto_es_otra_string)
#hola mundo

#MAYUSCULAS
print(esto_es_una_string.upper())

#minusculas
print(esto_es_una_string.lower())

#primera en Mayusculas
print(esto_es_una_string.capitalize())

#poner en Mayusculas la primera letra de cada palabra
print(esto_es_una_string.title())

#la longitud del string
print(len(esto_es_una_string))

#Buscar una caracter y muestra su ubicacion en indice
print(esto_es_una_string.find('e'))

#rebanar /// o slice
print(esto_es_una_string[0:2]) #inicia con cero
print(esto_es_una_string[:2]) #asume que inica con cero
print(esto_es_una_string[5:9])

#radar
#print(esto_es_una_string[::-1])
variable = 'radar'
print(variable[::])
print(variable[::-1])


 

