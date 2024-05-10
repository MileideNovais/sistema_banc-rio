def recomendar_plano (consumo):
  # TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
  if consumo < 11:
    plano_ideal= "Plano Essencial Fibra"
    
  elif consumo >10 and consumo <21:
    plano_ideal= "Plano Prata Fibra"
    
  else:
    plano_ideal= "Plano Premium Fibra"

# TODO: Retorne> o plano de internet adequado:
  return plano_ideal 

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Qual seu consumo mensal de dados (GB) ?"))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano (consumo)
print(recomendar_plano(consumo))