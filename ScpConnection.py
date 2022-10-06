#!/usr/bin/env python3
from os import system

def clear():
    system("clear")

#Needs Questions

print("--------------------------")
print("    1.Con Key Privada")
print("    2.Con Password")
print("--------------------------")
modo = input("Que modo usar =  [1]  :    ")

clear()

ip= input("IP =   Ej: 192.168.58.128  :      ")
clear()

origen = input("Ruta de lo que deseas pasar =   Ej: /home/alonso/ejemplo.txt :      ")
clear()

user = input("Usuario =  Ej: alonso ")
clear()

destino = input("Ruta donde lo deseas pasar =   Ej: /home/alonso/ :    ")
clear()

idfile = "/home/alonso/alonso :   "
clear()

port = input("Puerto para conexión, Ej: [22]    :")
clear()
password = input("Contraseña,     :")

if modo == "1":
    idfile = input("Introduce la ruta de tu KEY Privada   Ej: /home/alonso/alonso  :     ")
    system(f"scp -i {idfile} -p{port} {origen} {user}@{ip}:{destino}")

elif modo == "2":
    #system(f"scp -p{port} {origen} {user}@{ip}:{destino}")
    system(f"sshpass -p {password} scp {origen} {user}@{ip}:{destino}")

else:
    print ("Seleccione una opción valida [1-2]")

