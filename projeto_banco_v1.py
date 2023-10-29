#Criando um Sistema Bancário com Python

# Operação de Depósito

menu = '''
============================== BANK ==============================

[D] - Depositar
[S] - Saque
[E] - Extrato
[Q] - Sair

Escolha o tipo de operação que deseja realizar: '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu).upper()

    if opcao == 'D':

        valor = float(input('\nInforme o valor para depósito: R$'))

        print('\nDepósito realizado com êxito. Consulte o extrato para vizualização.\n')
        print('='*66)

        if valor > 0:

            saldo += valor
            extrato += 'Depósito: R${:.2f}\n'.format(valor)

        else:
            print('\nO valor informado é inválido. Limite de depósito: R$500.00.\n')
            print('='*66)

    elif opcao == 'S':

        if saldo == 0:

            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif numero_saques < LIMITE_SAQUES:

            saque = float(input('\nValor de saque: R$'))

            if saque <= limite and saldo >= saque:

                print('\nO valor de saque foi R${:.2f}. Consulte o extrato para vizualização.\n'.format(saque))
                print('='*66)

                saldo -= saque
                extrato += 'Saque: R${:.2f}\n'.format(valor)
                numero_saques += 1

            else:

                print('\nOperação falhou! O valor do saque excede o limite.\n')
                print('='*66)

        else:
            
            print('\nOperação falhou! Número máximo de saques excedido.\n')

    elif opcao == 'E':

        print('\n---------------------------- EXTRATO ----------------------------\n')
        
        if saldo == 0:

            texto = 'Não foram realizadas movimentações.'.center(65)
            print(texto if not extrato else extrato)

            print('-'* 65) 

        elif saldo != 0:
            texto = 'Saldo: R${:.2f}'.format(saldo).center(65)
            print('\n',texto)

            print('-'* 65) 

    elif opcao == 'Q':

        print('\nVocê saiu do programa de Operações de Depósito. Obrigado pelo teste!')

        break

    else:

        print('Operação inválida, por favor selecione novamente a opção desejada.')

        texto = 'Gostaria de voltar para o programa? (SIM/NÃO)'
        voltar_programa = input(texto).upper()

        if voltar_programa == "SIM":
            
            while True:

                opcao = input(menu).upper()