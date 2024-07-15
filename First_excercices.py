import os
# # # PROBLEMAS EN CLASES :
# # 001.-  EJEMPLO 1: Mi primer programa, el típico “Hola Mundo” 

print("Hola Mundo\n")

# # 002 : EJEMPLO 2 : Mi segundo programa, un saludo personalizado
# # Se requiere realizar un programa que inicie, pregunte el nombre del usuario, luego lo salude,
# # imprimiendo a pantalla el mensaje “Hola ” seguido del nombre ingresado y luego termine.

username=input("Ingresa tu nombre de usuario:\n")
print(f"Hola, {username}.\n")
input("Presiona para continuar.")

# # 003 : Ejercicio propuesto 1 : Sumar dos números 

os.system("cls")
num1 = int(input("Ingresa el primer numero:\n"))
num2 = int(input("Ingresa el segundo un numero:\n"))
suma= num1 + num2
print(f"La suma del primer numero con el segundo es: {suma}.\n")
input("Presiona para continuar.")

# # 004 :  Dados dos números enteros entregar el resultado del primero menos el segundo (resta)

os.system("cls")
num1 = int(input("Ingresa el primer numero:\n"))
num2 = int(input("Ingresa el segundo un numero:\n"))
resta = num1 - num2
print(f"La resta del primer numero con el segundo es: {resta}.\n")
input("Presiona para continuar.")

# # 005 : Dados dos números (enteros o decimales) entregar el resultado del producto de ambos (multiplicación).

os.system("cls")
num1 = int(input("Ingresa el primer numero:\n"))
num2 = int(input("Ingresa el segundo un numero:\n"))
mult = num1 * num2
print(f"La multiplicacion del primer numero con el segundo es: {mult}.\n")
input("Presiona para continuar.")

# # 006 : Dado un número entero o decimal entregar el doble del número, es decir el resultado 
# # obtenido al duplicarlo (es decir, multiplicar el número por 2)

os.system("cls")
num1 = int(input("Ingresa un numero:\n"))
dupl = num1 * 2
print(f"El doble del numero ingresado es: {dupl}.\n")
input("Presiona para continuar.")

# # 007 : Dado un número entero o decimal entregar el resultado del cuadrado de dicho número 
# # (nota: elevar al cuadrado es lo mismo que multiplicar el número por sí mismo una vez)
# # Lo común no es describir el algoritmo con palabras; lo común es plantear un problema y 
# # luego definir el algoritmo para resolver ese problema concreto.  Veamos ejemplos :

os.system("cls")
num1 = int(input("Ingresa un numero:\n"))
math = num1 * num1
print(f"El cuadrado del numero ingresado es: {math}.\n")
input("Presiona para continuar.")

# # 008 : Convertir Distancias.
# # Cada día recorro un distancia aproximada de entre 8.5 y 9.7 kilómetros en bicicleta 
# # para llegar desde mi casa a mi lugar de trabajo.  Un amigo extranjero me pregunto ¿Cuánto es eso en millas? 
# # , y yo no supe que responder.   Necesito poder expresar cualquier distancia en millas.

os.system("cls")
distancia=int(input("Ingresa la distancia recorrida:\n"))
millas = distancia * 0.621371
print(f"{distancia} kilometros es igual a {millas} millas.\n")
input("Presiona para continuar.")

# # 009 : Convertir Temperatura.
# # En Miami la temperatura actual es de 100 grados (Farenheit), lo cual me parece que es mucho, 
# # pero no sé cómo interpretar.  Me gustaría poder saber ¿cuál es la temperatura equivalente en
# # la escala que usamos en Chile? (Celsius).   Quisiera poder convertir cualquier temperatura.

os.system("cls")
temp = int(input("Ingresa la distancia recorrida:\n"))
fahrenheit = temp * 33.8
print(f"{temp} grados Celsius es igual a {fahrenheit} grados Fahrenheit.\n")
input("Presiona para continuar.")

# # 010 : Liquidación.
# # El vendedor me ha dicho que todos los computadores están rebajados en un 20% por ser la semana
# # tecnológica, pero además tienen un 10% adicional, sobre el precio ya rebajado si pago con la tarjeta 
# # de la tienda.  Para un computador “gamer” que me gustó cuyo precio normal es $1.399.990.- quisiera saber ambos precios.  
# # En general me gustaría poder calcularlo para cualquier otro computador.  

os.system("cls")
precio = int(input("Ingresa el precio del producto para saber el descuento:\n$"))
descuento20 = precio * 0.8
descuentocontarjeta = descuento20 * 0.9
print(f"el valor de {precio} solo con el descuento del 20% es: ${int(descuento20)}\n")
print(f"el valor de {precio} con el descuento del 30% y pagando con la tarjeta de la tienda es: ${int(descuentocontarjeta)}\n")
input("Presiona una tecla para continuar.")
      
# input("Presiona para continuar.")

#  011 : Mi peso en la luna.
# Acá en la tierra mi peso aproximado es 80 kilos. Me gustaría saber mi peso en la luna (teórico, 
# no es que vaya a ir allá a pesarme  ); donde la gravedad es menor.  Para cualquier valor (peso en kilos), 
# me gustaría saber el valor lunar equivalente.

os.system("cls")
peso= int(input("Ingresa tu peso:\n"))
peso_luna= peso * 0.166
print(f"{peso}Kg equivalen a {peso_luna}Kg, si estuvieramos en la luna equivale.")
input("Presiona una tecla para continuar.")

# 012 : Mi edad 
# Naci en 1971, actualmente es 2024, ¿Cuál es mi edad (aproximada), este año? 
# (Nota: digo “edad aproximada” porque puede ser que aun no haya pasado el día de mi cumpleaños)  

os.system("cls")
actualidad=2024
nacimiento= int(input("Ingresa el año de nacimiento:\n"))
excercice= nacimiento - actualidad
print("La edad aproximada segun el año de nacimiento ingresado es:", excercice)
input("Presiona una tecla para finalizar.")