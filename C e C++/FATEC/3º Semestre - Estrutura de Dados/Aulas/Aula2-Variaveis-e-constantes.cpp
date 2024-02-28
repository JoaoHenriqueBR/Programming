#include "iostream"
#include "cstdlib"
#include "math.h"
#include <stdio.h>
using namespace std;

/* Variável: Trata-se de um espaço na memória que sofrerá alteração durante a execução do programa.
   Constantes: São espaços na memória que não sofrerão alteração durante a execução do programa.

   Variável Local: São criadas dentro de funções ou voids.
   Variável Global: São criadas fora de funções ou voids, ocupam mais memória, pois permanecem mais tempo ocupando a memória.
   Escopo: É a área de alcance de uma variável.

 Programa Exemplo: Cálculo de Média ponderada com pesos
 pes1 = 0.35
 pes2 = 0.65
 nota1 = ?
 nota2 = ?
 mediaP = nota1 * pes1 + nota2 * pes2;
 Se mediaP >= 6 escreva "Aluno Aprovado" senão "Aluno Reprovado!"

*/

// Váriaveis Globais
  double const pes1 = 0.35; // constante
  double const pes2 = 0.65; // constante

  double nota1, nota2, mediaP; // Variáveis globais
int main()
{
  setlocale(LC_ALL, "Portuguese"); // configura idioma para português

  system("clear"); // apaga a tela, No Windows: system("cls");

  cout << "Digite a nota 1: "; // Ler a Nota 1
  cin >> nota1;

  cout << "Digite a nota 2: "; // Ler a Nota 2
  cin >> nota2;

  mediaP = nota1 * pes1 + nota2 * pes2; // Calcular a Média Ponderada

  if (mediaP >= 6) // Se a Média Ponderada for maior que 6
    cout << "\nAluno Aprovado!";
  else
    cout << "\nAluno Reprovado!";

  // saída de dados, impressão dos resultados
  cout << "\nO valor da média ponderada é: " << mediaP << endl;

  int c = getchar(); // No Windows: system("pause");
  
}