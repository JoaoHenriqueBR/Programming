Algoritmo "Porcentagem"
// 
//  
// Descrição   : Calcula a porcentagem usando imposto como exemplo
// Autor(a)    : João Henrique
// Data atual  : 11/5/2021
Var
// Seção de Declarações das variáveis 
   preco, imposto: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva("Qual o preco do produto? R$")
   Leia(preco)
   imposto <- (preco * 60)/100
   Escreva("O imposto será de R$", imposto:5:2)
Fimalgoritmo