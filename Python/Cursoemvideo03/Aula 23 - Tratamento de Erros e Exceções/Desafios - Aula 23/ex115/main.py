"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu:

 - nome
 - idade

Num arquivo de texto simples.

O sistema só vai ter 2 opções:

- Cadastrar uma nova pessoa;
- Listar todas as pessoas cadastradas.
"""

from modules import interface

while True:
    r = interface.menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sistema'])
    interface.escolha(r)
    if r == 3:
        break


