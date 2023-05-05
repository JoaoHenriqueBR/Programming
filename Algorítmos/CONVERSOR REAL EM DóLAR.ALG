Algoritmo "Conversor Real em Dólar"
// 
//  
// Descrição   : Converte Real em Dólar através da cotação de 10/5/2021.
// Autor(a)    : João Henrique
// Data atual  : 10/5/2021
Var
// Seção de Declarações das variáveis 
   C, Q: Inteiro
   reais, dolares: Real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
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