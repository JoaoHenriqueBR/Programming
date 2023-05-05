Algoritmo "ParOuImpar"
//
//
// Descrição   : Verifica se o numero e par ou impar usando o Se e o senao
// Autor(a)    : Joao Henrique
// Data atual  : 25/5/2021
Var
   // Seção de Declarações das variáveis
   N: Inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreva ("Digite um numero qualquer: ")
   Leia(N)
   Se (N % 2 = 0) entao
      Escreval("O numero ", N, " e PAR")
   senao
      Escreval("O numero ", N, " e IMPAR")
   FimSe
Fimalgoritmo