Algoritmo "Conversor Real em D�lar"
// 
//  
// Descri��o   : Converte Real em D�lar atrav�s da cota��o de 10/5/2021.
// Autor(a)    : Jo�o Henrique
// Data atual  : 10/5/2021
Var
// Se��o de Declara��es das vari�veis 
   C, Q: Inteiro
   reais, dolares: Real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
   C <- 1
   Escreva ("Quantas vezes quer usar o conversor? ")
   Leia(Q)
   Enquanto (C <= Q) faca
           Escreva("Quantos Reais eu tenho? R$")
           Leia(reais)
           dolares <- reais/5.22
           Escreval("Posso ter US$", dolares:5:2)
           C <- C + 1
   FimEnquanto
Fimalgoritmo