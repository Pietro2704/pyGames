import random 
a = random.randint(1,10)  
tentativa = 3  

while tentativa > 0: 
    num = int(input('escolha um numero de 1 a 10:')) 

    if num < a: 
        print('tente um numero maior') 
        tentativa = tentativa -1  

    elif num > a: 
        print ('tente um numero menor') 
        tentativa = tentativa -1 

    else: 
        print ('parabens você acertou') 
        break 

print('Suas chances acabaram') 