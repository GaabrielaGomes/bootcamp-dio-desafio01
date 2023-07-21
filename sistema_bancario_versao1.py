# Operação de Deposito:
# tem que ser possivel depositar valores na conta bancaria.
# Todos os depositos devem ser armazenados em uma variável e exibidos na operação de extrato

# Operação de Saque:
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$500 por saque.
# Caso o usuario não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possivel sacar o dinheiro por falta de saldo
# todos os saques devem ser armazenados em uma variável e exibidos na operaçã de extrato

#Operação de Extrato
# Deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx

saldo_atual = 0.0
valor_saque = 0.0
numero_saques = 0
saldo = ''
saque = ''

while True:
    opcao = int(input('''\n ======== Menu ========
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair
 Digite operação escolhida: '''))

    if opcao == 1:
        saldo_deposito = float(input('\n Digite valor do depósito: '))
        saldo_atual += saldo_deposito
        saldo += f'{saldo_deposito:.2f} '
    elif opcao == 2:
        if numero_saques <= 2:
            valor_saque = float(input('\n Digite valor do saque: '))
            if saldo_atual >= valor_saque:
                if valor_saque < 500:
                    saldo_atual -= valor_saque
                    numero_saques += 1
                    saque += f'{valor_saque:.2f} '
                else:
                    print('\n Limite de 500 reais excedido, por favor selecione novamente a operação desejada')
            else:
                print('\n Saldo insuficiente!')
        else:
            print('\n Erro ao fazer saque. Número máximo de saques excedidos')
    elif opcao == 3:
        print(f'\n Extrato dos depósitos: R${saldo}\n Extrato dos saques: R${saque}\n Saldo atual: R${saldo_atual:.2f}')
    elif opcao == 0:
        break
    else:
        print('\n Operação inválida, por favor selecione novamente a operação desejada')