# Ejercicio 1
# Crea un script que genere una estructura de carpetas llamada proyecto, con
# subcarpetas src y docs. Luego, elimina la carpeta docs
import time
import os
import shutil
from os.path import split

'''
os.mkdir("proyecto")
os.mkdir("src")
os.mkdir("docs")

shutil.move("src","proyecto/src")
shutil.move("docs","proyecto/docs")

os.rmdir("proyecto/docs")
'''

# Ejercicio 2
# Escribe un programa que cree un archivo llamado registro.txt en una carpeta
# logs, mueva ese archivo a otra carpeta llamada backup, y elimine el
# archivo original.
'''
os.mkdir("logs")
with open("registro.txt", "w"):
    pass
shutil.move("registro.txt","logs/registro.txt")
os.mkdir("backup")
shutil.move("logs/registro.txt", "backup/registro.txt")
time.sleep(2)
os.remove("backup/registro.txt")

'''
# Ejercicio 3
# Desarrolla un script que pida una lista de nombres de archivos, los cree en un
# directorio específico y luego elimine todos los archivos creados.
'''
os.mkdir("proyecto")
lista = []

for i in range(5):
    a = input("Escriba el nombre del archivo: ")
    with open(f"proyecto/{a}","w"):
        pass
    lista.append(a)

#ELIMINAR
for f in lista:
    print(f"Eliminando archivo... {f}")
    os.remove(f"proyecto/{f}")
    time.sleep(2)
'''

# Ejercicio piramide
'''
num = int(input("Indica de cuantas lineas quieres la piramide: "))
for i in range(num):
    esp = " " * (num-i)
    ast = "*" * (2 * i - 1)
    var += (esp+ast) + "\n"

with open("ejer.txt","w") as f:
    f.write(var)
'''
#Ejercicio 4
'''
with open("datos.txt", "r") as f:
    mensaje = f.read()


fichero = open("datos.txt", "r")
contador = 0
for i in fichero:
    contador+=1
cont_lin = str(contador)


num_carac = len(mensaje)
num_carac_1 = str(num_carac)


num_pala = mensaje.split()
num_palabras = len(num_pala)
num_palabras_1 = str(num_palabras)

with open("info.txt", "w") as f:
    f.write(f"Numero de caracteres: {num_carac_1}\n")
    f.write(f"Numero de palabras: {num_palabras_1}\n")
    f.write(f"Numero de lineas: {cont_lin}\n")

#Ejercicio 5
''''''
p = ''
for i in range(5):
    texto = input("Inotroduce una frase: ")
    p += texto + "\n"
    with open("notas.txt","w") as f:
        f.write(f"{p}\n")
'''
'''
#Ejercicio 6

import subprocess


resultado = subprocess.run("dir", shell=True, capture_output=True, text = True)

with open("listado.txt","w") as f:
    f.write(resultado.stdout)
'''
#Ejercicio 7
'''
hora = subprocess.run("date /t && time /t", shell=True, capture_output=True, text = True)
print(hora.stdout)

#Ejercicio 8

dom = input("Introduce el dominio: ")
ping = subprocess.run(f"ping {dom}", shell=True, capture_output=True, text = True)
print(ping.stdout)
'''

import nmap

red = input("Dime la red a escanear: ")
port = input("Indica el puerto: ")
print(f"Iniciamos espaneo de {red}  ")

s= nmap.PortScanner()
s.scan(red, arguments=port)

for host in s.all_hosts():
    print(f"{host} ({s[host]["tcp"]})")

