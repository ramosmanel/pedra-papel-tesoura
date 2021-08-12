from random import randint
from time import sleep
jogarnovamente = 'SIM'
while jogarnovamente == 'SIM':
    print('{:=^40}'.format('Pedra Papel Tesoura - GAME.py'))
    itens = ('Pedra', 'Papel', 'Tesoura')
    jogadapc = randint(0,2)
    print('''Suas jogadas:
     [0]PEDRA
     [1]PAPEL
     [2]TESOURA''')
    jogador = int(input('Qual sua jogada? '))
    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA!!!')
    if jogadapc == 0: #Pedra
        if jogador == 0:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Empatou!')
        elif jogador == 1:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Jogador Venceu!')
        elif jogador == 2:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Computador Venceu!')
        else:
            print('Jogada Inválida!')
    elif jogadapc == 1: #Papel
        if jogador == 0:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Computador Venceu!')
        elif jogador == 1:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Empatou!')
        elif jogador == 2:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Jogador Venceu!')
        else:
            print('Jogada Inválida!')
    elif jogadapc == 2: #Tesoura
        if jogador == 0:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Jogador Venceu!')
        elif jogador == 1:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Computador Venceu!')
        elif jogador == 2:
            print('-=' * 11)
            print('O computador jogou {}'.format(itens[jogadapc]))
            print('Jogador jogou {}'.format(itens[jogador]))
            print('-=' * 11)
            print('Empatou!')
        else:
            print('Jogada Inválida!')
    else:
        print('Operação Inválida!')
    jogarnovamente = str(input('Deseja jogar novamente? ')).upper()