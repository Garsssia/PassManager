import string
import random


def randompass(inputdigits,inputpunt,tamanio):
    #De base las contraseñas van a tener mayusculas y minusculas
    #también definimos si tienen signos de puntuación y numeros
    
    primalpass =  random.choice(list(string.ascii_letters)) + random.choice(list(string.ascii_letters)) + random.choice(list(string.ascii_letters)) + random.choice(list(string.ascii_letters))
    
    if tamanio < 13: return False

    #añadimos a la primigenia digitos y signos de puntuación si se permite
      
    if inputdigits == True:
        primalpass = random.choice(list(string.digits)) + primalpass + random.choice(list(string.digits))       
    if inputpunt == True:
        primalpass =  random.choice(list(string.punctuation)) + primalpass + random.choice(list(string.punctuation))
        
    primalpass = str(primalpass) 
    
    #Ya tenemos generada la contraseña primigenia en cualquier caso

    #ahora vamos a cubrir el caso mayoritario, que consiste en que hay todo tipo de caracteres

    # generamos aleatoriamente los tamaños de bloque de caracteres

    if inputdigits == inputpunt == True:
        puntsize = random.randrange(tamanio-10)
        digsize = random.randrange(tamanio-puntsize-2)
        lettersize = tamanio - puntsize - digsize
        if lettersize < 1: lettersize = 0
        digmesh = list()
        puntmesh = list()
        lettermesh = list()
        while digsize > 0:
            digmesh.append(random.choice(list(string.digits)))
            digsize = digsize - 1
        while puntsize > 0:
            puntmesh.append(random.choice(list(string.punctuation)))
            puntsize = puntsize - 1
        while lettersize > 0:
           lettermesh.append(random.choice(list(string.ascii_letters)))
           lettersize = lettersize - 1
        primalpass = str(primalpass) + str(lettermesh) + str(digmesh) + str(puntsize)
        passwrd = random.shuffle(list(primalpass))
    
    #generamos el caso de solo numeros

    elif inputdigits == True and inputpunt == False:
        puntsize = 0      
        digsize = random.randrange(tamanio-10)
        lettersize = tamanio - puntsize - digsize
        if lettersize < 1: lettersize = 0
        digmesh = list()
        puntmesh = list()
        lettermesh = list()
        while digsize > 0:
            digmesh.append(random.choice(list(string.digits)))
            digsize = digsize - 1
        while puntsize > 0:
            puntmesh.append(random.choice(list(string.punctuation)))
            puntsize = puntsize - 1
        while lettersize > 0:
           lettermesh.append(random.choice(list(string.ascii_letters)))
           lettersize = lettersize - 1
        primalpass = str(primalpass) + str(lettermesh) + str(digmesh) + str(puntsize)
        passwrd = random.shuffle(list(primalpass))   
        
    #Geneeramos el bloque de no numeros pero si caracteres de puntuación
    
    elif inputdigits == False and inputpunt == True:
        puntsize = random.randrange(tamanio-10)
        digsize = 0
        lettersize = tamanio - puntsize - digsize
        if lettersize < 1: lettersize = 0
        digmesh = list()
        puntmesh = list()
        lettermesh = list()
        while digsize > 0:
            digmesh.append(random.choice(list(string.digits)))
            digsize = digsize - 1
        while puntsize > 0:
            puntmesh.append(random.choice(list(string.punctuation)))
            puntsize = puntsize - 1
        while lettersize > 0:
           lettermesh.append(random.choice(list(string.ascii_letters)))
           lettersize = lettersize - 1
        primalpass = str(primalpass) + str(lettermesh) + str(digmesh) + str(puntsize)
        passwrd = random.shuffle(list(primalpass)) 

#Generamos el caso de ni numeros ni caracteres de puntuación
    elif inputdigits == False and inputpunt == False:
        puntsize = 0
        digsize = 0
        lettersize = tamanio - len(primalpass)
        if lettersize < 1: lettersize = 0
        digmesh = list()
        puntmesh = list()
        lettermesh = list()
        while digsize > 0:
            digmesh.append(random.choice(list(string.digits)))
            digsize = digsize - 1
        while puntsize > 0:
            puntmesh.append(random.choice(list(string.punctuation)))
            puntsize = puntsize - 1
        while lettersize > 0:
           lettermesh.append(random.choice(list(string.ascii_letters)))
           lettersize = lettersize - 1
        primalpass = primalpass + lettermesh + digmesh + puntsize
        passwrd = str(random.shuffle(list(primalpass))) 
    return passwrd





print(randompass(True,True,25))

#print(str(random.randint(5)))


