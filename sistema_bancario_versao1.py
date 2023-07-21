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
# Se o extrato estiver em branco, exibir a mensagem 'Não foram realizadas movimentações'

saldo_atual = 0.0
valor_saque = 0.0
numero_saques = 0
extrato_depositos = ''
extrato_saques = ''

while True:
    opcao = int(input('''\n ======== Menu ========
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair
Digite a operação desejada: '''))

    if opcao == 1:
        saldo_deposito = float(input('\nDigite o valor do depósito: '))
        saldo_atual += saldo_deposito
        extrato_depositos += f'R$ {saldo_deposito:.2f}\n'
    elif opcao == 2:
        if numero_saques < 3:
            valor_saque = float(input('\nDigite o valor do saque: '))
            if saldo_atual >= valor_saque and valor_saque <= 500:
                saldo_atual -= valor_saque
                numero_saques += 1
                extrato_saques += f'R$ {valor_saque:.2f}\n'
            else:
                print('\nValor de saque inválido. Verifique seu saldo ou limite máximo de R$500 por saque.')
        else:
            print('\nNúmero máximo de saques diários excedido.')
    elif opcao == 3:
        if extrato_depositos != '' or extrato_saques != '':
            print(f'\nExtrato dos depósitos:\n{extrato_depositos}Extrato dos saques:\n{extrato_saques}Saldo atual: R$ {saldo_atual:.2f}')
        else:
            print('\nNão foram realizadas movimentações.')
    elif opcao == 0:
        break
    else:
        print('\nOperação inválida. Por favor, selecione novamente a operação desejada.')
