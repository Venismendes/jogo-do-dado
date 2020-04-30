import random

pontos_jogador1 = 1000
dado = (1, 2, 3, 4, 5, 6)
jogadores = 1

jogador = input('Olá qual o seu nome: ')
print(f'Bem vindo ao jogo do dado {jogador}')


quantidade_jogadores = input('Deseja jogador de 2 jogadores? [S/N]: ').upper()


if quantidade_jogadores == 'S':
    jogadores = 2
    jogador2 = ('Nome do segundo jogador: ')


print('=' * 40)
while jogadores == 1:
    print('Inicialmente você tem 1000 pontos!')
    print('[S] para sair!')
    print('[P] para ver seus pontos')
    print('[J] para jogar: ')
    while True:
        print('=' * 30)
        opcao = input('Opção: ').upper()
        print('=' * 30)

        while True:
            menu = True
            na = random.choice(dado)
            if na <= 3:
                valor = 'L'
            else:
                valor = 'H'

            if opcao == 'J':
                while True:
                    try:
                        aposta = int(input('Quantos pontos: '))
                        if aposta <= 0 or aposta > pontos_jogador1:
                            aposta = int(input(f'Seu valor é menor que 1 ou maior que {pontos_jogador1}: '))
                            break
                        else:
                            break
                    except ValueError:
                        print('valor inválido, somente tente só números inteiros.')
                low_high = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()
                while low_high != 'H' and low_high != 'L' and low_high != 'S':
                    print('Valor inválido')
                    low_high = input('|[L] = 123 | [H] = 456 | [S] = Sair: ').upper()

                print()
                print(f'Dado: {na} = {valor}')
                if low_high == valor and (low_high == 'L' or low_high == 'H'):
                    print(f'Você acertou e ganhou {aposta} pontos!!')
                    pontos_jogador1 = pontos_jogador1 + aposta
                    menu = False
                elif low_high == 'L' or low_high == 'H':
                    print(f'Você errou e perdeu {aposta} pontos!!')
                    pontos_jogador1 = pontos_jogador1 - aposta
                    menu = False

                print(f'Seus pontos: {pontos_jogador1}')
                print('=' * 30)

                if low_high == 'S':
                    menu = True
                    break

            if opcao == 'S':
                exit()
            if opcao == 'P':
                print(f'Você possui {pontos_jogador1} pontos.')

            if menu == True:
                print('=' * 30)
                opcao = input('Opção: ').upper()
                print('=' * 30)

else:
    print('modo 2 jogadores ainda não desenvolvido')