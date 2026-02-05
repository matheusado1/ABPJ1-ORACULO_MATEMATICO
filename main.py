# Sistema Financeiro Pessoal 

receitas = []
despesas = []

while True:
    print("\nMENU FINANCEIRO ")
    print("1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Ver saldo")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor da receita: "))
        receitas.append(valor)
        print("Receita adicionada com sucesso!")

    elif opcao == "2":
        valor = float(input("Digite o valor da despesa: "))
        despesas.append(valor)
        print("Despesa adicionada com sucesso!")

    elif opcao == "3":
        saldo = sum(receitas) - sum(despesas)
        print(f"Saldo atual: R$ {saldo:.2f}")
