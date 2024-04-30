def menu():

    menu = """
    Escolha a opção desejada:
    [u]cadastrar usuário
    [c] cadastrar conta bancária
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

def saque (*,valor, saldo, limite, extrato,  numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo,  extrato

def deposito(valor, extrato, saldo, /):
    
    if valor > 0:

        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado  com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo,  extrato

def extratos (saldo, /,*, extrato):
    if extrato == "":
        print ("Não foram realizadas movimentações!")
    else:
        print(f""" ### Movimentações:###
        {extrato}
        O seu saldo  é R$ {saldo:.2f}""")
    return saldo, extrato

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None       

def criar_usuario(usuarios):
    cpf = input("Informe CPF do usuário(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def cadastrar_conta(AGENCIA, numero_conta, usuarios):
    contas= []
    cpf = input("Informe o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)

    
    if usuario:
        print(f" Conta {numero_conta}, criada com sucesso!")
        numero_conta = len(contas) + 1
    
        return {"AGENCIA":AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    

        
    else:
        print("Usúario não encontrado! Utilize opção cadastrar novo usuário")
        
    

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    AGENCIA = "0001"
    contas = []
    numero_conta=0
    


    while True:

        opcao = menu()

        
        if opcao == "d":
            
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(valor, extrato, saldo)
        
        elif opcao == "s":
            
            valor = float(input("Informe o valor do saque: "))
            
            saldo,  extrato = saque(saldo=saldo, valor= valor, extrato= extrato, limite = limite, numero_saques= numero_saques, LIMITE_SAQUES= LIMITE_SAQUES,)

        elif opcao == "e":
         
         extratos(saldo, extrato=extrato)

        elif opcao == "q":
            print("Obrigado (a) por utilizar nosso sistema!")
            break
       
        elif opcao == "u":
            criar_usuario (usuarios)

        elif opcao == "c":

            cadastrar_conta (AGENCIA, numero_conta, usuarios)

            numero_conta = len(contas) + 1
        
        
        else:
            print("Opção inválida! Escolha novamente a opção desejada.")



main()   