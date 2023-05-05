Algoritmo "SomadorNumerico"
// 
//  
// Descrição   : Repetiçao (SOMA, MENOR, MAIOR)
// Autor(a)    : Joao Henrique
// Data atual  : 28/2/2022
Var
// Seção de Declarações das variáveis 
   cont, N, S, maior, menor : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   cont <- 1
   S <- 0
   Enquanto (cont <= 5) faca
            Escreva ("Digite o ", cont, "o. Valor : ")
            Leia (N)
            Se (N > maior) entao
               maior <- N
            FimSe
            Se (N < maior) entao
               menor <- N
            FimSe
            Se (0 = menor) entao
               menor <- N
            FimSe
            S <- S + N
            cont <- cont + 1
   FimEnquanto
   Escreval("A Soma de todos os valores foi ", S)
   Escreval("O maior valor digitado foi ", maior)
   Escreval("O menor valor digitado foi ", menor)
Fimalgoritmo