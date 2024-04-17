#include "iostream"
#include "math.h"
#include "cstdlib"
#include <stdio.h> // No windows, <conio.h>.
using namespace std;

/*
Fazer o código fonte de programa para ler o comprimento e 
calcular o diâmetro, calcular o raio e finalmente a área de um círculo; 
(Faça um menu com as opções necessárias, utilize goto ou while e switch case. )
*/

double const pi = 3.14;

int lerComprimento(){
  double comprimento;
  cout << "\nDigite o comprimento: ";
  cin >> comprimento;
  return comprimento;
}

void getDiametro(double comprimento){
  double diametro;
  diametro = comprimento / pi;
  cout << "\nO diâmetro é: " << diametro << endl;
  return;
}

double getRaio(double comprimento){
  double raio;
  raio = comprimento / (pi * 2);
  return raio;
}

void getArea(double raio){
  double area;
  area = pi * pow(raio, 2);
  cout << "\nA área do círculo é: " << area << endl;
  return;
}

int main(){
  setlocale(LC_ALL, "Portuguese");
  double comprimento, diametro, raio;
  char tecla;
  while (tecla != 27){
    cout << "\nMENU - CÁLCULO DE UM CIRCULO\n\n1-Diametro\n2-Raio\n3-Area\nESC-Sair\nitem: ";
    tecla = getchar(); // No Windows, getch()
    switch (tecla)
    {
      case '1':
        comprimento = lerComprimento();
        getDiametro(comprimento);
        break;
      case '2':
        comprimento = lerComprimento();
        raio = getRaio(comprimento);
        cout << "\nO raio é: " << raio << endl;
        break;
      case '3':
        comprimento = lerComprimento();
        raio = getRaio(comprimento);
        getArea(raio);
        break;
      case 27:
        cout << "\nSaindo do programa..." << endl;
        break;
      default:
        cout << "\nOpção inválida!" << endl;
        break;
    }
  int c = getchar();
  }
return 0;
}
