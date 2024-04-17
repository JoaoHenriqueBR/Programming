#include "iostream"
#include "cstdlib"
#include "math.h"
#include <stdio.h>
using namespace std;

/*
Ler dois inteiros (variáveis A e B) e imprimir o resultado do quadrado da diferença do primeiro valor pelo segundo.
*/

int lerA(){
  double a;
  cout << "\nDigite o valor de A: ";
  cin >> a;
  return a;
}

int lerB(){
  double b;
  cout << "\nDigite o valor de B: ";
  cin >> b;
  return b;
}

void getquadrado(double a, double b){
  double q;
  q = pow((a - b), 2);
  cout << "\nO quadrado da diferença é: " << q << endl;
  return;
}

int main(){
  double a, b;
  setlocale(LC_ALL, "Portuguese");
  a = lerA();
  b = lerB();
  getquadrado(a, b);
  int c = getchar();
  return 0;
}
