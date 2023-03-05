from random import randint
import time


class Player:
    def __init__(self, args):
        self.name = args[0]
        self.energy = int(args[1])
        self.power = int(args[2])


def main():
  print("Vocês tem 10.000 pontos para serem distribuidos na vida e no poder do seu personagem...")
  time.sleep(5)
  print("Construa seu personagem no formato '(nome) (vida) (poder)'")
  time.sleep(3)
  while True:
     try:
         hero = Player(input('Crie o primeiro personagem: ').split(' '))
         enemy = Player(input('Crie o segundo personagem: ').split(' '))
         fight(hero, enemy)
         break
     except:
         print('ERRO na criação da personagem. Utilize o formato "(nome) (vida) (poder)"')
         time.sleep(1)
         continue


def fight(hero, enemy):
    print('O jogo começou')
    time.sleep(1)
    print('Batalha entre %s e %s' % (hero.name, enemy.name))
    time.sleep(3)


    players = [hero, enemy]
    while hero.energy > 0 and enemy.energy > 0:
        turn(players[0], players[1])
        players.reverse()

    announcewinner(players)


def turn(attacker, defender):
    print('%s atacou %s' % (attacker.name, defender.name))
    luck = randint(0, 100)
    time.sleep(1)

    if luck <= 15:
        print('Errou!!')
    else:
        damage = attacker.power / 3
        if luck <= 70:
            print('Soco normal ( - %d HP)' % damage)
        elif luck <= 96:
            damage += damage * 0.5
            print('Soco forte! ( - %d HP)' % damage)
        elif luck > 96:
            damage += damage
            print('ATAKE ESPECIAAAL!!! ( - %d HP)' % damage)
        defender.energy -= damage
    time.sleep(3)


def announcewinner(players):
    time.sleep(1)
    for player in players:
        if player.energy > 0:
            print('Jogo acabou, o vencedor foi %s com HP restante de %d' % (player.name, player.energy))

main()