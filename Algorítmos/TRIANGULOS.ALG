Algoritmo "triangulos"
// 
//  
// Descrição   : Diz o tipo do triângulo com base no número de lados apresentado
// Autor(a)    : João Henrique
// Data atual  : 30/4/2021
Var
// Seção de Declarações das variáveis 
   L1, L2, L3: Real
   EQ, ES, TRI: Logico
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   Escreva("Digite o primeiro lado: ")
   Leia (L1)
   Escreva("Digite o segundo lado: ")
   Leia (L2)
   Escreva("Digite o terceiro lado: ")
   Leia (L3)
   TRI <- (L1 < L2 + L3) e (L2 < L1 + L3) e (L3 < L1 + L2)
   EQ <- (L1=L2) e (L2=L3)
   ES <- (L1<>L2) e (L2<>L3) e (L1<>L3)
   Escreval ("Pode formar um TRIANGULO? ", TRI)
   Escreval ("O triangulo e EQUILITERO? ", EQ)
   Escreval ("O triangulo e ESCALENO? ", ES)
Fimalgoritmo