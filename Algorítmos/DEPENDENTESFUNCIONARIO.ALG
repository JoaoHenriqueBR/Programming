Algoritmo "DependentesFuncionario"
// 
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Joao Henrique
// Data atual  : 15/6/2021
Var
// Se��o de Declara��es das vari�veis 
   Nome: caractere
   Sal, NSal: real
   Dep: Inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   Escreva ("Qual o nome do funcionario? ")
   Leia (Nome)
   Escreva ("Qual o salario do funcionario? ")
   Leia (Sal)
   Escreva ("Qual e a quantidade de dependentes? ")
   Leia (Dep)
   Escolha Dep
           Caso 0
                NSal <- Sal + (Sal*5/100)
           Caso 1,2,3
                NSal <- Sal + (Sal*10/100)
           Caso 4,5,6
                NSal <- Sal + (Sal*15/100)
           OutroCaso
                    NSal <- Sal + (Sal*18/100)
   FimEscolha
   Escreval ("O novo salario de ", Nome, " sera de R$", NSal:5:2)
Fimalgoritmo