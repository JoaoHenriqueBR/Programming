Algoritmo "RegraDeTres"
// 
//  
// Descri��o   : Calcula a regra de tres com base nos outros tres numeros
// Autor(a)    : Joao Henrique
// Data atual  : 27/5/2021
Var
// Se��o de Declara��es das vari�veis 
   A1, A2, X1, X: Real
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva("Escreva o numero localizado em cima/baixo do x: ")
   Leia(X1)
   Escreva("Escreva o numero localizado ao lado do x: ")
   Leia(A2)
   Escreva("Escreva o numero localizado em cima/baixo do anterior: ")
   Leia(A1)
   X <- (X1*A2) / A1
   Escreva("Com base nos numeros apresentados, o resultado de x e: ", X)
Fimalgoritmo