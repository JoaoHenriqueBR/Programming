#include "iostream"
#include "cstdlib"
#include "math.h"
#include <stdio.h>
using namespace std;

/*
Faça o algoritmo para calcular o valor de uma prestação em atraso 
com base na multa de 2% e também do juros mensal de 1% sobre o valor 
principal. Declare vetores não explícitos para entrada do valor da dívida, Divida 
[5] e da quantidade de dias em atraso: Dias [5]. Crie os vetores de saída, 
ValorMulta[5], ValorJuros[5] e ValorPagar [5]. Ao final imprima todos os vetores 
de saída. Faça um menu de controle para controlar o programa. 
*/

double divida[5]; int dias[5]; double valorMulta[5]; double valorJuros[5]; double valorPagar[5];

void lerDados(){
  for (int i=0; i<5; i++){
    cout << "Dívida: ";
    cin >> divida[i];
    cout << "Dias: ";
    cin >> dias[i];
  }
  return;
}

void calcular(){
  for (int i=0; i<5; i++){
    valorMulta[i] = divida[i] * 0.02;
    valorJuros[i] = divida[i] * 0.01 * dias[i];
    valorPagar[i] = divida[i] + valorMulta[i] + valorJuros[i];
  }
  return;
}

void exibir(){
  for (int i=0; i<5; i++){
    cout << "\nDívida: R$ " << divida[i] << endl;
    cout << "Dias: " << dias[i] << endl;
    cout << "\nValor da Multa: R$ " << valorMulta[i] << endl;
    cout << "Valor do Juros: R$ " << valorJuros[i] << endl;
    cout << "Valor a Pagar: R$" << valorPagar[i] << endl;
  }
  return;
}

int main(){
  setlocale(LC_ALL, "Portuguese");
  int tecla;
  MENU:
    cout << "* Menu *\n1 - Ler\n2 - Calcular\n3 - Exibir\n4 - Sair\nItem: ";
    cin >> tecla;
    switch(tecla){
      case 1:
        lerDados(); 
        system("clear");
        cout << "Dados lidos com sucesso!\n" << endl;
        break;
      case 2: 
        calcular();
        system("clear"); 
        cout << "Cálculos realizados com sucesso!\n" << endl;
        break;
      case 3: exibir(); break;
      case 4: exit(0); break;
    }

  goto MENU;
  
return 0;}