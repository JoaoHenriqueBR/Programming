Algoritmo "semnome"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/4/2021
Var
// Seção de Declarações das variáveis 
  Nome: Caractere
  N1, N2: Inteiro
  DI: Inteiro
  R: Inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
  Escreva ("Digite seu Nome: ")
  Leia (Nome)
  Escreval ("Muito prazer ", Nome)
  Escreva ("Informe um número: ")
  Leia (N1)
  Escreva ("Informe outro número: ")
  Leia (N2)
  DI <- (N1 \ N2)
  R <- (N1 % N2)
  Escreval ("A divisão inteira entre ", N1, " e ", N2, " e igual a ", DI)
  Escreva ("Resta", R)
Fimalgoritmo