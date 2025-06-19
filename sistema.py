menu = """
+-------------------------+
|        BEM VINDO        |
| DIGITE A OPÇÃO DESEJADA:|
|-------------------------|
|[D] Realizar deposito.   |
|[S] Realizar saque.      |
|[E] Consultar Extrato.   |
|[0] Sair.                |
+-------------------------+

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        print("#### VOCÊ ESCOLHEU DEPOSITO! ####")
        try: #FILTRA ENTRADAS STRING
            valor = float(input("Digite o valor que deseja depositar ou digite 0 para voltar ao menu: "))
            if valor < 0:
                print("ALERTA !! Digite APENAS valores POSITIVOS. ")
                input("Aperte qualquer tecla para voltar ao menu: ")
                continue
            if valor == 0:
                continue
            else:
                saldo += valor
                extrato += f" * Você depositou R${valor:.2f}.\n"
                print("Valor Depositado na conta com sucesso!")
        except ValueError:
            print("ALERTA !! Entrada inválida! Por favor, Digite APENAS NÚMEROS.")
        input("Aperte qualquer tecla para voltar ao menu: ")



    elif opcao == "s":
        print("#### VOCÊ ESCOLHEU SAQUE! ####")
        try: #FILTRA ENTRADAS STRING
            if numero_saques < LIMITE_SAQUES:
                solicitacao = float(input("Digite o valor do saque ou digite 0 para voltar ao menu: "))
                if saldo < solicitacao:
                    print("ALERTA !! Saldo insuficiente!")
                    input("Aperte qualquer tecla para voltar ao menu: ")
                elif solicitacao > limite:
                    print("ALERTA !! Seu LIMITE DE SAQUE é de R$500,00 por SAQUE.")
                    input("Aperte qualquer tecla para voltar ao menu: ")
                elif solicitacao < 0:
                    print("ALERTA !! Digite apenas VALORES POSITIVOS! ")
                    input("Aperte qualquer tecla para voltar ao menu: ")
                elif solicitacao == 0:
                    continue
                else:
                    saldo -= solicitacao
                    extrato += f" * Você sacou R${solicitacao:.2f}.\n"
                    numero_saques += 1
            else:
                print("ALERTA!! Você JÁ ATINGIU seu limite de TRÊS saques diários.")
                input("Aperte qualquer tecla para voltar ao menu: ")
            continue
        except ValueError:
            print("ALERTA !! Por favor digite APENAS números.")
        input("Aperte qualquer tecla para voltar ao menu: ")



    elif opcao == "e":
        print(f"""
#### VOCÊ ESCOLHEU EXTRATO! ####
HISTORICO DE TRANSAÇÕES: 
{extrato if extrato else ' * Nenhuma movimentação realizada na conta.'}
Seu saldo atual é: R$ {saldo:.2f}.
""")
        input("Aperte qualquer tecla para voltar ao menu: ")



    elif opcao == "0":
        print("Obrigado por usar nosso sistema, Até logo!")
        break



    else:
        print("ALERTA !! Digite uma opção valida!")
        input("Aperte qualquer tecla para voltar ao menu: ")
        continue