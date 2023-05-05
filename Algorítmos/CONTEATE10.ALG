Algoritmo "ConteAte10"
// 
//  
// Descrição   : Repetiçao
// Autor(a)    : Joao Henrique
// Data atual  : 28/2/2022
Var
// Seção de Declarações das variáveis 
   valor, salto, contador : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
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