Algoritmo "CalculoIMC"
//  
//  
//
//
// Descrição   : Calcula o IMC da pessoa com base no Peso e Altura
// Autor(a)    : Joao Henrique
// Data atual  : 25/5/2021
Var
// Seção de Declarações das variáveis
   M, A, IMC: Real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   Escreva("Massa (KG): ")
   Leia(M)
   Escreva("Altura (m): ")
   Leia(A)
   IMC <- M / (A ^ 2)
   Escreval("IMC: ", IMC:5:2)
   Se (IMC < 17) entao
      Escreval("Muito abaixo do peso")
   senao
        se (IMC >= 17) e (IMC <= 18.5) entao
          Escreval("Abaixo do peso")
        senao
             se (IMC >= 18.5) e (IMC < 25) entao
                Escreval("Peso ideal")
             senao
                  se (IMC >= 25) e (IMC < 30) entao
                     Escreval("Soprepeso")
                  senao
                       se (IMC >= 30) e (IMC < 35) entao
                          Escreval("Obesidade")
                       senao
                            se (IMC >= 35) e (IMC < 40) entao
                               Escreval("Obesidade Severa")
                            senao
                                 Escreval("Obesidade Morbida")
                            FimSe
                       FimSe
                  FimSe
             FimSe
        FimSe
   FimSe
Fimalgoritmo