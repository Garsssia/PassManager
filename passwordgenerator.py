import string
import random



def randompassnano(digits,punt,size):
    password= ()
    if(isinstance(digits,bool) and isinstance(punt,bool) and isinstance(size,int)):
        if digits == True and punt == True:
            password = random.choices(string.punctuation+string.ascii_letters+string.digits,k=size)
        elif digits == False and punt == True:
            password = random.choices(string.punctuation+string.ascii_letters,k=size)
        elif digits == True and punt == False:
            password = random.choices(string.digits+string.ascii_letters,k=size)
        elif digits == False and punt==False:
            password = random.choices(string.ascii_letters,k=size)
        vuelta = ""
        for p in password:
            vuelta += p
        return vuelta

    else:    
        return print("Parametros incorrectos")            
        

def randompassmini(tamanio):
    puntsize = random.randrange(tamanio)
    digsize = random.randrange(tamanio)
    lettersize = random.randrange(tamanio)

    internalpassize = digsize + puntsize + lettersize

    if puntsize + digsize + lettersize != tamanio:
        lettersize = lettersize + tamanio - internalpassize

 

    
    passletter = random.choices(list(string.ascii_letters),k=lettersize)
    print(passletter)    
    
    passdigit = random.choice(list(string.digits),k=digsize)
    print(passletter)
   
    passpunt = random.choice(list(string.punctuation),k=puntsize)
    print(passletter)    

    password = str(passdigit) + str(passletter) + str(passpunt)

    password = list(random.shuffle(list(password)))
    

    print(str(password))
    print(tamanio)
    
    password = str(random.choices(password,k=int(tamanio)))
    
    return password     

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
           lettersize = lettersize - 1
        primalpass = str(primalpass) + str(lettermesh) + str(digmesh) + str(puntsize)
        passwrd = str(random.shuffle(list(primalpass)))
        return passwrd
    
    #generamos el caso de solo numeros

    if inputdigits == True and inputpunt == False:
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
        return passwrd
          
       
    #Geneeramos el bloque de no numeros pero si caracteres de puntuación
    

    if inputdigits == False and inputpunt == True:
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
        return passwrd
        


#Generamos el caso de ni numeros ni caracteres de puntuación
    else:
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
        primalpass = str(primalpass) + str(lettermesh) + str(digmesh) + str(puntsize)
        passwrd = str(random.shuffle(list(primalpass)))
        return passwrd



