#include "iostream"
#include "math.h"
#include "cstdlib"
#include <stdio.h> // getchar (Linux)
using namespace std;

/*
  Elaborar um programa que calcule e apresente o volume de uma caixa retangular, por meio da fórmula VOLUME ← COMPRIMENTO * LARGURA * ALTURA.
*/

int main()
{
  setlocale(LC_ALL, "Portuguese");

  double comprimento, largura, altura, volume; // variáveis locais

  cout << "Digite o comprimento da caixa: ";
  cin >> comprimento;

  cout << "Digite a largura da caixa: ";
  cin >> largura;

  cout << "Digite a altura da caixa: ";
  cin >> altura;

  volume = comprimento * largura * altura;
  
  cout << "O volume da caixa é: " << volume << endl;

  int c = getchar(); // No Windows: system("pause");
  
return 0; }
