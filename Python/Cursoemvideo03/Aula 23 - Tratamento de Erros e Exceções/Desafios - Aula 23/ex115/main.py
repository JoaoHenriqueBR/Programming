"""
Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu:

 - nome
 - idade

Num arquivo de texto simples.

O sistema só vai ter 2 opções:

- Cadastrar uma nova pessoa;
- Listar todas as pessoas cadastradas.
"""

from modules.interface import *
from modules.arquivo import *

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    r = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sistema'])
    escolha(r, arq)
    if r == 3:
        break


