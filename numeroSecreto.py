import random

secreto= random.randint(1,100)
numero = int(input("adivina el numero del 1 al 100 :"))

while numero != secreto:
    if numero < secreto:
        print("el numero es mayor")
    else:
        print ("el numero es menor")
    numero = int(input("Intenta adivinar el numero del 1 al 100 de nuevo:"))

print ("feicidades,adivinaste el numero")
