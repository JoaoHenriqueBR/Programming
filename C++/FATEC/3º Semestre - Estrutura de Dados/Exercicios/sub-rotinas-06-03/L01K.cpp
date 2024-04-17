#include "iostream"
#include "math.h"
#include "cstdlib"
#include <stdio.h>
using namespace std;

/*
Elaborar um programa que efetue a apresentação do valor da conversão em dólar de um valor lido em real. 
O programa deve solicitar o valor da cotação do dólar e também a quantidade de reais disponível com o usuário, para que seja apresentado o valor em moeda americana.
*/

void conversao(double cotacao, double real){
  double dolar;
  dolar = real / cotacao;
  cout << "\nO valor em dólar é: " << dolar << endl;
  return;
}

int main(){
  setlocale(LC_ALL, "Portuguese");
  double cotacao, real;
  cout << "\nDigite o valor em real: ";
  cin >> real;
  cout << "\nDigite a cotação do dólar: ";
  cin >> cotacao;
  conversao(cotacao, real);
  int c = getchar();
  return 0;
}
