Algoritmo "ConteAte10"
// 
//  
// Descri��o   : Repeti�ao
// Autor(a)    : Joao Henrique
// Data atual  : 28/2/2022
Var
// Se��o de Declara��es das vari�veis 
   valor, salto, contador : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   contador <- 0
   Escreva("Quer contar ate quanto? ")
   Leia(valor)
   Escreva("Qual sera o valor do salto? ")
   Leia(salto)
   Enquanto (contador <= valor) faca
            Escreval(contador)
            contador <- contador + salto
   FimEnquanto
   Escreval("Terminei de Contar")
Fimalgoritmo