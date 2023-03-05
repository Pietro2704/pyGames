from random import choice

lista = ["pedra","papel","tesoura"]
p = choice(lista)

#print(p)#------teste de mesa

n = input("Escreva pedra, papel ou tesoura:\n")
n = n.lower()

while n!="pedra" and n!="papel" and n!="tesoura":
  n = input("Não entendi.\n")
  
while p==n:
  p=choice(lista)
  #print(p)#----teste de mesa
  
while p!=n:
  if p == "pedra" and n=="tesoura":
    print("Seu oponente jogou pedra.\nVocê Perdeu")
    break
  
  elif p=="papel" and n=="pedra":
    print("Seu oponente jogou papel.\nVocê Perdeu")
    break
  
  elif p=="tesoura" and n=="papel":
    print("Seu oponente jogou tesoura.\nVocê Perdeu")
    break
  
  else:
    print("Seu oponente jogou {}.\nVocê Ganhou".format(p))
    break