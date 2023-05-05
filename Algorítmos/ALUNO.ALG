Algoritmo "Aluno"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 15/6/2021
Var
// Seção de Declarações das variáveis 
   N1, N2, M: Real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva("Primeira nota: ")
   Leia(N1)
   Escreva("Segunda nota: ")
   Leia(N2)
   M <- (N1 + N2) / 2
   Escreval("A media do aluno foi ", M:4:2)
   Se (M >= 7) entao
      Escreval("Aluno APROVADO")
   senao
        Se (M >= 5) e (M <7) entao
           Escreval("Aluno em RECUPERACAO")
        senao
             Escreval("Aluno REPROVADO")
        FimSe
   FimSe
Fimalgoritmo