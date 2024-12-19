import math
import random
import os
import time




# EJERCICIOS VARIABLES
# Ejercicio 1


'''
edad= int(input("Dime la edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# Ejercicio 2

num_telefono = (input("Dime tu numero de teléfono: "))

caracteres = len(num_telefono)

num_telefono = int(num_telefono)
if caracteres == 9:
    print("Numero correcto: ",num_telefono)

else:
    print("Es incorrecto el numero: ",num_telefono)
'''
from operator import truediv

# Ejercicio 3
'''
grados = float(input("Que grados hacen: "))
grados_farenheit = (grados * (9/5) +32)

if grados_farenheit > 77.1:
    print("Hace Calor: ", grados_farenheit,"ºF")
elif grados_farenheit > 65 and grados_farenheit <= 77.1:
    print("Hace buena temperatura", grados_farenheit,"ºF")
else:
    print("Hace frio: ", grados_farenheit,"ºF")
'''


# EJERCICIOS BUCLE FOR

# Ejercicio 1
'''
for i in range(1,1001):
    print(i)
'''
# Ejercicio 2
'''
numero =int(input("Introduzca un numero: "))
total = 1
for num in range(1,numero+1):
    total = total * num
print(total)
'''
# Ejercicio 3
'''
lista = []
for i in range (0,5):
    nombres = input("Indica los nombres: ")
    lista.append(nombres)
print(lista)
'''
# Ejercicio 4
'''
lista = []
num = int(input("Cuantos nombres quieres ingresar? "))
for i in range (0,num):
    nombres = input("Indica los nombres: ")
    lista.append(nombres)
print(lista)
'''

#Ejercicio 5
'''
lista = []
num = int(input("Cuantos nombres quieres ingresar? "))
for i in range (0,num):
    nombres = input("Indica los nombres: ")
    lista.append(nombres)

i = 0
for nombres in lista:
    i+=1
    nombres_len = len(nombres)
    if nombres_len%2 == 0:
        print(f"{i}. El nombre {nombres} contiene {nombres_len} y es par")
    else:
        print(f"{i}. El nombre {nombres} contiene {nombres_len} y es impar")
'''
#EJERCICIOS BUCLE WHILE

#Ejercicio 1
'''
num_usuario = ""
suma = 0
while num_usuario !=0:
    num_usuario = int(input("Dime un numero: "))
    suma = num_usuario + suma
print(suma)
'''
#Ejercicio 2

'''
user = "felipe"
contraseña = "1234"
us = ""
pasw = ""

while us != user or contraseña != pasw:
    us = input("Escriba usuario: ")
    pasw = input("Escriba su contraseña: ")
    while us != user or contraseña != pasw:
        print("Credenciales incorrectas")
        break
print("Credenciales correctas")

'''

#Ejercicio 3
'''
numeros = int(input("¿Cuantos numeros quieres?"))
contador = 0
lista =[]
n = ""
while contador != numeros:
    n = int(input("Introduce un numero: "))
    if n > 0:
        lista.append(n)
    else:
        print("Error")
    contador += 1
for f in lista:
    print(f"{f}")
'''
#Ejercicio 4
'''
cont = 1
while cont!= 50:
    if cont%5 == 0 and cont <=30:
        print(cont)
    if cont == 30:
        print("Se ha terminado")
    cont +=1
'''

#Funciones
#Ejercicio 1


'''
def es_par(a):
    if a%2 == 0:
        return True
    else:
        return False


#Ejercicio 2

def fahrenheit_a_celsius(a):
   return  (a-32) * 5/9


tiempo = fahrenheit_a_celsius(int(input("Escribe un grado: ")))
print(f"Hacen {tiempo}ºC")
'''

#Ejercicio 3

'''
def dni(a):
    letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    posicion = a%23
    letra = letras[posicion]
    return letra
'''

#Ejercicio 1
'''
pulse = 1
while pulse != "0":
    print(random.randint(1,6))
    pulse = input("Pulse una tecla")
'''
#Ejercicio 2
'''
arch = input("Escriba el nombre del archivo: ")
print(os.path.exists(arch))
'''


#Ejercicio 3
'''
i = 0
while i !=11:
    print(i)
    time.sleep(1)
    i += 1
'''


#EJERCICIO 1
'''
cont = 0
prueba = None
dificultad = None
intentos = None


#Indica la dificultad que queremos añadir al juego

while True:
    dificultad = int(input("Que dificultad quieres?\n 0.Facil\n 1.Medio\n 2.Dificil\n\n Introduzca: "))
    if dificultad == 0:
        num = random.randint(1,10)
        intentos = 5
        break
    elif dificultad == 1:
        num = random.randint(1,50)
        intentos = 10
        break
    elif dificultad ==2:
        num = random.randint(1,100)
        intentos = 20
        break
    # Si el numero es distinto se repetira el bucle
    else:
        print("Inserte un valor entre 0 y 2 \n")


# Selecciona los intentos
# Nos da la pista de si es mayor o menor
# Aumenta el contador

while True:
    if cont >= intentos:
        print("\nHA SUPERADO EL LIMITE!!!")
        break
    prueba = int(input("Adivina el numero: "))
    cont += 1
    if num > prueba:
        print("El numero es mayor")
    elif num < prueba:
        print("El numero es menor")
    # Cuando aciertes el numero saldra el bucle
    else:
        print("Correcto lo has adivinado!!")
        print(f"Lo has averiguado a la {cont}")
        break

'''
'''
#Ejercicio 2
def contar (a):
    vocales = "aeiou"
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    cont_vocales = 0
    cont_consonantes = 0

    for letra in a.lower():
        if letra in vocales:
            cont_vocales +=1
        elif letra in consonantes:
            cont_consonantes +=1
    return cont_vocales, cont_consonantes

b = (contar(input("Introduzca una frase:")))

print("Numero de Vocales",b[0])
print("Numero de consonantes",b[1])
'''

#Ejercicio 3
'''
def numero(a):

    if a > 10:
        print("Numero alto")
    elif a < 0:
        print("Numero negativo")
    elif a <= 9 and a > 0:
        print("Numero bajo")
    elif a == 0:
        print("Fin del programa")
    else:
        print("Error")
    return a

while True:
    num = (numero(int(input("Introduzca un numero: "))))
    if num ==0:
        break
'''



#PIEDRA, PAPEL O TIJERA

cont_usuario = 0
cont_pc = 0

def calculo(num_usuario, num_pc):
    if num_usuario == num_pc:
        return "EMPATE"
    #GANA EL PC
    elif num_usuario == "piedra" and num_pc == "papel":
        return "PC"
    elif num_usuario == "papel" and num_pc == "tijera":
        return "PC"
    elif num_usuario == "tijera" and num_pc == "piedra":
        return "PC"
    #GANA EL USUARIO
    else:
        return "USUARIO"

def calcular(numero):
    if numero ==1:
        return "piedra"
    elif numero ==2:
        return "papel"
    else:
        return "tijera"

while True:

    # Variables para asignar piedra/papel/tijera

    num_usuario = int(input("\n 1. Piedra \n 2. Papel\n 3. Tijera\n Introduce: "))
    num_pc = random.randint(1, 3)

    #Asignamos las variables a las funciones para que el numero se transforme en texto

    num_usuario = calcular(num_usuario)
    num_pc = calcular(num_pc)

    #Pasamos las variables de piedra/papel/tijera a una llamada calculo para que nos diga quien ha ganado.

    ganador = calculo(num_usuario, num_pc)

    print(f"\nEl usuario ha elegido:  {num_usuario}")
    print(f"El pc ha elegido:  {num_pc}\n")

    time.sleep(2)
    if ganador == "EMPATE":

        print("Han quedado empate")
    elif ganador=="PC":

        print("Ha ganado el PC")
        cont_pc +=1
    elif ganador =="USUARIO":

        print("Ha ganado el usuario")
        cont_usuario +=1

    #MARCADOR
    print("*" * 80)
    print("\t" * 8, "MARCADOR")
    print("\t" * 4, "USUARIO: ", cont_usuario, "\t" * 4, "PC: ", cont_pc)
    print("*" * 80)

    time.sleep(2)
     #PARA VER QUIEN HA GANADO
    if cont_pc == 3:
        print("\nHa ganado el pc al mejor de 3")
        break
    elif cont_usuario==3:
        print("\nHa ganado el usuario al mejor de 3")
        break

