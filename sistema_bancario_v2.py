# Função para exibir o menu
def menu():
    menu = '''
======================================= BANK ========================================

[D]  - Depositar
[S]  - Saque
[E]  - Extrato
[C]  - Criar Usuário
[U]  - Usuários
[CC] - Conta Corrente

[Q]  - Sair

Escolha um dos procedimentos: '''
    return menu

# Função para realizar um depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += 'Saldo R${:.2f}'.format(valor)
        print('\nDepósito realizado com êxito. Consulte o extrato para visualização.')
    else:
        print('\nO valor informado é inválido.\n')
    return saldo, extrato

# Função para realizar um saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    ultrapassou_saldo = valor > saldo
    ultrapassou_limite = valor > limite
    ultrapassou_limite_saques = numero_saques > limite_saques
    
    if ultrapassou_saldo:
        print('Falha na operação. Saldo insuficiente. Consulte o extrato para visualização.')
    elif ultrapassou_limite:
        print('Falha na operação. Limite de R$500 por saque.')
    elif ultrapassou_limite_saques:
        print('Falha na operação. Número máximo de saques atingido.')
    elif valor > 0:
        saldo -= valor
        extrato += "Saque: R${:.2f}".format(valor)
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    return saldo, extrato

# Função para apresentar o extrato
def apresentar_extrato(saldo, extrato):
    print('\n---------------------------- EXTRATO ----------------------------\n')
    if saldo == 0:
        texto = 'Não foram realizadas movimentações.'.center(65)
        print(texto if not extrato else extrato)
        print('-' * 65)
    elif saldo != 0:
        texto = 'Saldo: R${:.2f}'.format(saldo).center(65)
        print('\n', texto)
        print('-' * 65)

# Função para criar um usuário
def criar_usuario(contas):
    nome = input('Digite seu nome: ')
    entrada_data = input('Data de nascimento (DD/MM/AAAA): ')
    cpf = input('Informe seu CPF: ')
    
    # Verifique se o CPF já existe na lista de contas
    for conta in contas:
        if conta['cpf'] == cpf:
            print("CPF já cadastrado. Não é permitido duplicação de CPF.")
            return
    
    # Verifique se a entrada tem o formato correto
    if len(entrada_data) != 10 or entrada_data[2] != '/' or entrada_data[5] != '/':
        print("Formato de data inválido. Use DD/MM/AAAA.")
        return

    # Verifique se o CPF tem o comprimento correto (11 caracteres)
    if len(cpf) != 11:
        print("CPF deve conter 11 dígitos.")
        return

    # Verifique se o CPF contém apenas dígitos
    if not cpf.isdigit():
        print("CPF deve conter apenas dígitos numéricos.")
        return
    
    endereco = input('Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ')
    contas.append({'nome': nome, 'data_nascimento': entrada_data, 'cpf': cpf, 'endereco': endereco})

# Função para listar os usuários
def listar_usuarios(contas):
    print("\n---------------------- LISTA DE USUÁRIOS -----------------------\n")
    if not contas:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in contas:
            print("Agência: {}, Nome: {}, CPF: {}".format(AGENCIA, usuario['nome'], usuario['cpf']))
    print("-" * 60)

# Define a constante AGENCIA
AGENCIA = "0001"

def main():
    saldo = 0
    saque = 0
    limite = 500
    extrato = ''
    numeros_saques = 0
    LIMITE_SAQUES = 3
    contas = []  # Armazena informações dos usuários

    while True:
        opcao = input(menu()).upper()

        if opcao == 'D':
            valor = float(input('\nInforme o valor para depósito: R$'))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 'S':
            valor = float(input('\nValor de saque: R$'))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numeros_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == 'E':
            apresentar_extrato(saldo, extrato)
        elif opcao == 'C':
            criar_usuario(contas)
        elif opcao == 'U':
            listar_usuarios(contas)
        elif opcao == 'Q':
            break

main()
