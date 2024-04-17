#include "iostream"
#include "math.h"
#include "cstdlib"
#include <stdio.h> // getchar (Linux)
using namespace std;

/*
  Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula:
  Volume <- π * Raio² * Altura
*/

double const pi = 3.14; // constante

int main()
{
  setlocale(LC_ALL, "Portuguese");

  double raio, altura, volume; // variáveis locais

  cout << "Digite o raio da lata: ";
  cin >> raio;

  cout << "Digite a altura da lata: ";
  cin >> altura;

  volume = pi * pow(raio, 2) * altura;

  cout << "O volume da lata é: " << volume << endl;

  int c = getchar(); // No Windows: system("pause");
  
return 0; }
