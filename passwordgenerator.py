import string
import random

def randompass(digits,punt,size):
    
    if(isinstance(digits,bool) and isinstance(punt,bool) and isinstance(size,int) and size>0):
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
    
    else:    
        vuelta = []

    return vuelta



