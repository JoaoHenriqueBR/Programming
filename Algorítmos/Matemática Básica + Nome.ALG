Algoritmo "semnome"
// 
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/4/2021
Var
// Se��o de Declara��es das vari�veis 
  Nome: Caractere
  N1, N2: Inteiro
  DI: Inteiro
  R: Inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
  Escreva ("Digite seu Nome: ")
  Leia (Nome)
  Escreval ("Muito prazer ", Nome)
  Escreva ("Informe um n�mero: ")
  Leia (N1)
  Escreva ("Informe outro n�mero: ")
  Leia (N2)
  DI <- (N1 \ N2)
  R <- (N1 % N2)
  Escreval ("A divis�o inteira entre ", N1, " e ", N2, " e igual a ", DI)
  Escreva ("Resta", R)
Fimalgoritmo