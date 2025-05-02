pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print()
# Mostra as chaves do dicionário:
print(pessoas.keys())
print()

# Mostra os valores do dicionário:
print(pessoas.values())
print()

# Mostra os itens do dicionário:
print(pessoas.items())
print()

# Deleta um item
# del pessoas['sexo']

# Substitui o valor do nome
# pessoas['nome'] = 'João'

# Adiciona um item (Em um dicionário não é necessário .append)
pessoas['peso'] = 98.5

# Em laço de repetição o items pode ser usado para substituir o enumerate.
for k, v in pessoas.items():
  print(f'{k} = {v}')

