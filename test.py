from passwordgenerator import randompass
import string
import random



print("Normal")
print(randompass(True,True,32))
# sin numeros
print("Sin Numeros")
print(randompass(False,True,32))
# sin string.punctuation
print("sin puntuacion")
print(randompass(True,False,32))
# solo letras
print("solo letras")
print(randompass(False,False,32))
# no tiene que devolver nada
print("debe devolver vacío")
print(randompass(1, "3",'j'))
print("debe devolver vacío")
print(randompass(True,True,-1))

