menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
 
Digite a opção Desejada => """

saldo = 0
limite_de_saque = 500
extrato = ""
numero_de_saques = 0
LIMITE_NUMERO_SAQUES = 3

while True:
    
    opcao = str(input(menu))
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor >0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Depósito de {valor} realizado com sucesso!")
            
        else:
            print("Valor informado é inválido, repita a operação!")
            
    elif opcao =="2":
        valor =float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_de_saque
        excedeu_numero_saques = numero_de_saques >= LIMITE_NUMERO_SAQUES
        
        if excedeu_saldo:
            print("Você não possui saldo suficiente, refaça a operação ou tire um extrato.")
        elif excedeu_limite:
            print("Valor acima do limite permitido.")
        elif excedeu_numero_saques:
            print("Você excedeu o número de saques diários, tente novamente no próximo dia útil ou contate seu gerente.")
            
        elif valor>0:
            saldo -= valor
            extrato += f"Saque Realizado {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Saque de {valor} realizado com sucesso!")
            
        else:
            print("Valor informado é inválido, repita a operação!")
            
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("Obrigado por utilizar o nosso banco!")
        print("Phone Banking 24 horas por dia (11) 2233-9977")
        print("==========================================")
        
    elif opcao == "0":
        print("Obrigado por usar o nosso banco!")
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a opção desejada!")