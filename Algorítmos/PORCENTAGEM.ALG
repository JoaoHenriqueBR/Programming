Algoritmo "Porcentagem"
// 
//  
// Descri��o   : Calcula a porcentagem usando imposto como exemplo
// Autor(a)    : Jo�o Henrique
// Data atual  : 11/5/2021
Var
// Se��o de Declara��es das vari�veis 
   preco, imposto: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva("Qual o preco do produto? R$")
   Leia(preco)
   imposto <- (preco * 60)/100
   Escreva("O imposto ser� de R$", imposto:5:2)
Fimalgoritmo