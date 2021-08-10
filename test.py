from passwordgeneratos import randompass, randompassmini, randompassnano
import string
import random

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)

tamanio = 25
soup = string.ascii_lowercase + string.digits + string.punctuation
soup = list(soup)
contra = str()

while (tamanio > 0):
    contra = contra + str(random.choice(soup))
    tamanio = tamanio - 1


# print(randompass(True,True,25))
# print(randompass(True,False,25))
# print(randompass(False,True,25))
# print(randompass(False,False,25))

# print(randompassmini(25))

print(randompassnano(True,True,32))
# sin numeros
print(randompassnano(False,True,32))
# sin string.punctuation
print(randompassnano(True,False,32))
# solo letras
print(randompassnano(False,False,32))
# no tiene que devolver nada
print(randompassnano(1, "3",'j'))

print(contra)