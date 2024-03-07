#include "iostream"
#include "cstdlib"
#include "math.h"
#include "string"
#include <stdio.h>
using namespace std;

// Exercício A: Ler 10 elementos de uma matriz tipo vetor e apresentá-los.
void exercA(){
  string vetor[] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};
  int n = sizeof(vetor)/sizeof(string);
  cout << "--------------------" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << vetor[i] << endl;
  }
  cout << "--------------------\n" << endl;
  return;
}

/*
Ler 8 elementos em uma matriz A tipo vetor. 
Construir uma matriz B de mesma dimensão com os elementos da matriz A multiplicados por 3. 
O elemento B[i] deverá ser implicado pelo elemento A[i]*3, 
o elemento B[2] implicado pelo elemento A[2]*3 e assim por diante, até 8. Apresentar o vetor B.
*/
void exercB(){
  int A[] = {1, 2, 3, 4, 5, 6, 7, 8};
  int n = sizeof(A)/sizeof(int);
  int B[n];
  int aux = 0;
  cout << "--------------------" << endl;
  for (int i = 0; i < n; i++){
    aux = A[i] * 3;
    B[i] = aux;
    cout << B[i] << " - ";
  }
  cout << "FIM!" << endl;
  cout << "--------------------\n" << endl;
  return;
}

// Menu de Exercícios - A -> G
int main(){
  setlocale(LC_ALL,"Portuguese");
  char tecla;
  while (tecla != 27){
    cout << "MENU - EXERCÍCIOS\n\n- A;\n- B;\n- C;\n- D;\n- E;\n- F;\n- G;\nESC - Sair\nItem: ";
    tecla = getchar();
    switch(tecla)
    {
      case 'A':
        exercA();
        break;
      case 'B':
        exercB();
        break;
      case 27:
        cout << "\nSaindo do programa..." << endl;
        break;
      default:
        cout << "\nOpção inválida!\n" << endl;
        break;
    }
  int c = getchar();
  }
return 0;}

