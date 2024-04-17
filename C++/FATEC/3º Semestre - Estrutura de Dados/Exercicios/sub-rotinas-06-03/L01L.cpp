#include "iostream"
#include "math.h"
#include "cstdlib"
#include <stdio.h>
using namespace std;

/*
Elaborar um programa que efetue a leitura de três valores (A, B e C) e apresente como resultado final à soma dos quadrados dos três valores lidos.
*/

int lerA (){
  double A;
  cout << "\nDigite o valor de A: ";
  cin >> A;
  return A;
}

int lerB (){
  double B;
  cout << "\nDigite o valor de B: ";
  cin >> B;
  return B;
}

int lerC (){
  double C;
  cout << "\nDigite o valor de C: ";
  cin >> C;
  return C;
}

void sumquadrado(double a, double b, double c){
  double soma;
  soma = pow(a, 2) + pow(b, 2) + pow(c, 2);
  cout << "\nA soma dos quadrados é: " << soma << endl;
  return;
}

int main(){
  double A, B, C;
  setlocale(LC_ALL, "Portuguese");
  A = lerA();
  B = lerB();
  C = lerC();
  sumquadrado(A, B, C);
  int c = getchar();
  return 0;
}
