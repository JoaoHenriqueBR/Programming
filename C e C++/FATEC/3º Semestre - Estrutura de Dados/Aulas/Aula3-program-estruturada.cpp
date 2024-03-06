#include "iostream"
#include "cstdlib"
#include "math.h"
#include <stdio.h>
using namespace std;

// Criando as funções de entrada/leitura

double lervalorX() {
  double x;
  cout << "\nDigite a nota 1: ";
  cin >> x;
  return x;
}

double lervalorY() {
  double x;
  cout << "\nDigite a nota 2: ";
  cin >> x;
  return x;
}

// Funções de cálculo

double getmediaG(double x, double y){
  double mg;
  mg = sqrt(x*y);
  return mg;
}

// Funções de voids ou exibição ou sáida

void exibir(double x, double y, double mg){
  cout << "\nNota 1: " << x;
  cout << "\nNota 2: " << y;
  cout << "\nMédia: " << mg;
  getchar();
}

int main(void){
  double vx, vy, mg;
  char tecla;
  while (tecla != 27){
    cout << "\nmenu\n1-Executar\nESC-Sair\nitem: ";
    tecla = getchar();
    switch (tecla)
    case '1': {
        vx = lervalorX();
        vy = lervalorY();
        mg = getmediaG(vx, vy);
        exibir(vx, vy, mg); // chamando o void exibir
        break;
    }
    
  }
return 0; }
