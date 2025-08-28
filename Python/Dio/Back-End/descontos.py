# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# Aplique o desconto se o cupom for válido:
if cupom in descontos.keys():
  preco_final = preco - (preco * descontos[cupom])
  print(f'{preco_final:.2f}')
else:
  print(preco)
