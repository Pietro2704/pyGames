from random import randint

op = input("Escolha entre Par ou Ímpar?\n")
op = op.upper()

while op!="PAR" and op!="ÍMPAR":
  op = input("Não entendi\n")
  op = op.upper()
  
num = int(input("Digite um número: "))
a = randint(1,2)
print("Seu adversário escolheu",a)

calc = a+num
if calc%2==0:
  i = "PAR"
else:
  i = "ÍMPAR"
if i==op:
  print("Ganhou")
  
else:
  print("Perdeu")