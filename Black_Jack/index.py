from random import randint

num = randint(1,11)
ad = randint(15,21)

print("Por favor. Digite apenas:\nS-(sim)\nN-(não)")
print("Você tem {} pontos".format(num))
resp = input("Quer mais? ")
resp = resp.upper()
    
while resp == "S":
  num = num + randint(1,11)
  
  if num<21:
    print("Agora você tem {} pontos".format(num))
    resp = input("Quer mais? ")
    resp = resp.upper()
    
  elif num>21:
      print("Você passou com {} pontos, seu adversário tinha {} pontos".format(num,ad))
      break
    
  elif num==21:
      print("Você fez 21!!\nParabéns")
      break
    
while resp == "N":
  print("Vc terminou o jogo com {} pontos e seu adversário fez {} pontos".format(num,ad))
  if ad>num:
        print("Perdeu")
        break
  elif ad==num:
        print("Empatou! Que cagada")
        break
  else:
        print("Você ganhou!")
        break    