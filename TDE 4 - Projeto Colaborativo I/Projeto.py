entradas = int(input('1 - 2 Players , 2 - Player x Bot e 3 - Bot x Bot \nSelecione uma modalidade:'))
print('--------------------------------------------------------------------------------------')
if entradas == 1:
    print('Modalidade selecionada: Player x Player')
    print('Regras do jogo: Pedra ganha da tesoura / Tesoura ganha do papel / Papel ganha da pedra')

    placarplayer1 = 0
    placarplayer2 = 0

    contador = 1
    while contador:
        print('--------------------------------------------------------------------------------------')
        jogadas1 = int(input('Pedra - 1, Papel - 2 e Tesoura - 3 \nSelecione sua jogada:'))
        jogadas2 = int(input('Pedra - 1, Papel - 2 e Tesoura - 3 \nSelecione sua jogada:'))
        print('--------------------------------------------------------------------------------------')
        if jogadas1 == 1 and jogadas2 == 2:
            print('Jogador 2 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer2 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 1 and jogadas2 == 3:
            print('Jogador 1 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 2 and jogadas2 == 1:
            print('Jogador 1 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 2 and jogadas2 == 3:
            print('Jogador 2 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer2 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 3 and jogadas2 == 1:
            print('Jogador 2 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer2 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 3 and jogadas2 == 2:
            print('Jogador 1 venceu!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 1 and jogadas2 == 1:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 0
            placarplayer2 += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 2 and jogadas2 == 2:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 0
            placarplayer2 += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 3 and jogadas2 == 3:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 0
            placarplayer2 += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nPlayer 2 =', placarplayer2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

    contador += 1

elif entradas == 2:
    import random

    print('Modalidade selecionada: Player x Bot')
    print('Regras do jogo: Pedra ganha da tesoura / Tesoura ganha do papel / Papel ganha da pedra')

    placarplayer1 = 0
    placarbot = 0

    contador = 1
    while contador:
        print('--------------------------------------------------------------------------------------')

        numeros = random.randint(1, 3)

        jogadas1 = int(input('Pedra - 1, Papel - 2 e Tesoura - 3 \nSelecione sua jogada:'))
        jogadasbot = numeros

        if jogadas1 == 1 and jogadasbot == 2:
            print('Bot escolheu:', numeros)
            print('Bot venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 1 and jogadasbot == 3:
            print('Bot escolheu:', numeros)
            print('Jogador 1 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 2 and jogadasbot == 1:
            print('Bot escolheu:', numeros)
            print('Jogador 1 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 2 and jogadasbot == 3:
            print('Bot escolheu:', numeros)
            print('Bot venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 3 and jogadasbot == 1:
            print('Bot escolheu:', numeros)
            print('Bot venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 3 and jogadasbot == 2:
            print('Bot escolheu:', numeros)
            print('Jogador 1 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 1 and jogadasbot == 1:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 0
            placarbot += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 2 and jogadasbot == 2:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 0
            placarbot += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadas1 == 3 and jogadasbot == 3:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarplayer1 += 0
            placarbot += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Player 1 =', placarplayer1, 'pontos', '\nBot =', placarbot, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

    contador += 1


elif entradas == 3:
    import random

    print('Modalidade selecionada: Bot x Bot')
    print('Regras do jogo: Pedra ganha da tesoura / Tesoura ganha do papel / Papel ganha da pedra')

    placarbot1 = 0
    placarbot2 = 0

    contador = 1
    while contador:
        print('--------------------------------------------------------------------------------------')

        numeros1 = random.randint(1, 3)
        import random

        numeros2 = random.randint(1, 3)

        jogadasbot1 = numeros1
        jogadasbot2 = numeros2

        if jogadasbot1 == 1 and jogadasbot2 == 2:
            print('Bot 1 escolheu:', numeros1)
            print('Bot 2 escolheu:', numeros2)
            print('Bot 2 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot2 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2 =', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break


        if jogadasbot1 == 1 and jogadasbot2 == 3:
            print('Bot 1 escolheu:', numeros1)
            print('Bot 2 escolheu:', numeros2)
            print('Bot 1 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2 =', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadasbot1 == 2 and jogadasbot2 == 1:
            print('Bot 1 escolheu:', numeros1)
            print('Bot 2 escolheu:', numeros2)
            print('Bot 1 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2 =', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadasbot1 == 2 and jogadasbot2 == 3:
            print('Bot 1 escolheu:', numeros1)
            print('Bot 2 escolheu:', numeros2)
            print('Bot 2 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot2 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2 =', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadasbot1 == 3 and jogadasbot2 == 1:
            print('Bot 1 escolheu:', numeros1)
            print('Bot 2 escolheu:', numeros2)
            print('Bot 2 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot2 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2=', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadasbot1 == 3 and jogadasbot2 == 2:
            print('Bot 1 escolheu:', numeros1)
            print('Bot 2 escolheu:', numeros2)
            print('Bot 1 venceu!')
            print('--------------------------------------------------------------------------------------')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot1 += 1
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2=', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadasbot1 == 1 and jogadasbot2 == 1:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot1 += 0
            placarbot2 += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2 =', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadasbot1 == 2 and jogadasbot2 == 2:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot1 += 0
            placarbot2 += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2 =', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

        if jogadasbot1 == 3 and jogadasbot2 == 3:
            print('Empate!')
            opcao = int(input('Deseja continuar? 1 - SIM e 2 - NÃO \nSelecione a opção:'))
            placarbot1 += 0
            placarbot2 += 0
            if opcao == 2:
                print('--------------------------------------------------------------------------------------')
                print('Bot 1 =', placarbot1, 'pontos', '\nBot 2 =', placarbot2, 'pontos')
                print('Obrigado por utilizar o programa! \nFeito por: João, Hugo, Nathan e Heitor.')
                break

    contador += 1


