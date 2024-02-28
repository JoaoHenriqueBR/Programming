#include "iostream"
#include "math.h"
#include "cstdlib"
#include <stdio.h> // getchar (Linux)
using namespace std;

/*
  Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, utilizando a fórmula PRESTACAO ← VALOR + (VALOR * TAXA/100) * TEMPO).
*/

int main()
{
  setlocale(LC_ALL, "Portuguese");

  double valor, taxa, tempo, prestacao; // variáveis locais

  cout << "Digite o valor da prestação: ";
  cin >> valor;

  cout << "Digite a taxa de juros: ";
  cin >> taxa;

  cout << "Digite o tempo de atraso: ";
  cin >> tempo;

  prestacao = valor + (valor * taxa / 100) * tempo;

  cout << "O valor da prestação em atraso é: " << prestacao << endl;

  int c = getchar(); // No Windows: system("pause");
  
return 0; }