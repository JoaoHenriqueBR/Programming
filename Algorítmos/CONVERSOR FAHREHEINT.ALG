Algoritmo "Conversor Fahreheint"
// 
//  
// Descrição   : Converte Fahreheint
// Autor(a)    : João Henrique
// Data atual  : 10/5/2021
Var
// Seção de Declarações das variáveis 
   F, C: Real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva("Qual e a temperatura aqui? ")
   Leia(F)
   C <- (F - 32) / 1.8
   Escreva("No Brasil estaria ", C:4:1)
Fimalgoritmo