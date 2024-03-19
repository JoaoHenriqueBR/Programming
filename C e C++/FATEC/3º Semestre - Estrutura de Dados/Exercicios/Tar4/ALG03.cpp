#include "iostream"
#include "cstdlib"
#include "math.h"
#include <stdio.h>
using namespace std;

/*
Crie um algoritmo que tenha um vetor de idades e um vetor de nomes, 
cujos dados deverão ser lidos pelo teclado. Ao final Exiba o nome da pessoa 
de maior idade, menor idade, a média das idades e o saldo das idades.
*/

int idade[5]; string nome[5];

void lerDados(){
  for (int i=0; i<5; i++){
    cout << "Nome: ";
    cin >> nome[i];
    cout << "Idade: ";
    cin >> idade[i];
  }
  return;
}

void calcular(){
  int maior, menor;
  string nomeMaior, nomeMenor;
  int tot = sizeof(idade)/sizeof(int);
  int soma = 0;
  for (int i = 0; i<tot; i++){
    if (idade[i] > maior || i == 0){
      maior = idade[i];
      nomeMaior = nome[i];
    }
    if (idade[i] < menor || i == 0){
      menor = idade[i];
      nomeMenor = nome[i];
    }
    soma += idade[i];
  }
  cout << "\nMaior: " << nomeMaior << " - " << maior << " Anos.";
  cout << "\nMenor: " << nomeMenor << " - " << menor << " Anos.";
  cout << "\nMédia: " << soma/tot;
  cout << "\nSaldo: " << soma << endl;
  int c = getchar();
  return;
}

int main(){
  setlocale(LC_ALL, "Portuguese");
  int tecla;
  MENU:
    cout << "* Menu *\n1 - Ler\n2 - Calcular e Exibir os resultados.\n3 - Sair\nItem: ";
    cin >> tecla;
    system("clear");
    switch(tecla){
      case 1:
        lerDados();
        cout << "Dados lidos com sucesso!\n" << endl;
        break;
      case 2:
        calcular();
        break;
      case 3: exit(0); break;
    }
  goto MENU;
  
return 0; }
