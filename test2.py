itens = []
i=0

# TODO: Crie um loop para solicita os itens ao usuário:
while i < 3:
# TODO: Solicite o item e armazena na variável "item":
  item = input("Insira equipamento:")
# TODO: Adicione o item à lista "itens":
  itens.append(item)
  i=i+1
# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")