Algoritmo "Conversor Fahreheint"
// 
//  
// Descri��o   : Converte Fahreheint
// Autor(a)    : Jo�o Henrique
// Data atual  : 10/5/2021
Var
// Se��o de Declara��es das vari�veis 
   F, C: Real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva("Qual e a temperatura aqui? ")
   Leia(F)
   C <- (F - 32) / 1.8
   Escreva("No Brasil estaria ", C:4:1)
Fimalgoritmo