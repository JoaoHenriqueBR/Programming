Algoritmo "Idade"
// 
//  
// Descri��o   : Calcula a idade com base no ano de nascimento e no ano atual.
// Autor(a)    : Jo�o Henrique
// Data atual  : 10/5/2021
Var
// Se��o de Declara��es das vari�veis 
   ano_atual, ano_nasc, idade: Inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva("Em que anos nos estamos? ")
   Leia(ano_atual)
   Escreva("Em que ano eu nasci? ")
   Leia(ano_nasc)
   idade <- ano_atual - ano_nasc
   Escreva("Em", ano_atual, " voce tera", idade, " anos")
   Se (idade >= 18) entao
      Escreval (" e ja tera atingido a maioridade. ")
   senao
      Escreval (" e nao tera atingido a maioridade. ")
   FimSe
Fimalgoritmo