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

/* Exercício B:
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

/* Exercício C:
Ler duas matrizes A e B do tipo vetor com 20 elementos.
Construir uma matriz C, onde cada elemento da C é a subtração do elemento correspondente de A com B.
Apresentar a matriz C.
*/
void exercC(){
  int A[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
  int B[] = {20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  int n = sizeof(A)/sizeof(int);
  int C[n];
  int aux = 0;
  cout << "--------------------" << endl;
  for (int i = 0; i < n; i++){
    aux = A[i] - B[i];
    C[i] = aux;
    cout << C[i] << " >> ";
  }
  cout << "FIM!" << endl;
  cout << "--------------------\n" << endl;
  return;
}

/* Exercício D:
Ler 15 elementos de uma matriz tipo vetor.
Construir uma matriz B de mesmo tipo, observando a seguinte lei de formação:
"Todo elemento de B deverá ser o quadrado do elemento de A correspondente".
Apresentar as matrizes A e B.
*/

void exercD(){
  int A[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
  int n = sizeof(A)/sizeof(int);
  int B[n];
  int aux = 0;
  cout << "--------------------" << endl;
  cout << "Vetor A: ";
  for (int i = 0; i < n; i++){
    cout << A[i] << " - ";
  }
  cout << "FIM!" << endl;
  cout << "\nVetor B: ";
  for (int i = 0; i < n; i++){
    aux = A[i] * A[i];
    B[i] = aux;
    cout << B[i] << " - ";
  }
  cout << "FIM!" << endl;
  cout << "--------------------\n" << endl;
  return;
}

/* Exercício E:
Ler duas matrizes A e B do tipo vetor com 15 elementos cada.
Construir uma matriz C, sendo esta a junção das duas outras matrizes.
Desta forma, C deverá ter o dobro de elementos, ou seja, 30.
Apresentar a matriz C.
*/

void exercE(){
  int A[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
  int B[] = {16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30};
  int n = sizeof(A)/sizeof(int);
  int C[n*2];
  int aux = 0;
  cout << "--------------------" << endl;
  for (int i = 0; i < n; i++){
    C[i] = A[i];
    cout << C[i] << " - ";
  }
  for (int i = 0; i < n; i++){
    C[i+n] = B[i];
    cout << C[i+n] << " - ";
  }
  cout << "FIM!" << endl;
  cout << "--------------------\n" << endl;
  return;
}

/* Exercício F:
Ler duas matrizes do tipo vetor, sendo A com 20 elementos e B com 30 elementos.
Construir uma matriz C, sendo esta a junção das duas outras matrizes.
Desta forma, C deverá ter a capacidade de armazenar 50 elementos.
Apresentar a matriz C.
*/

void exercF(){
  int A[20];
  int B[30];
  int C[50];
  cout << "--------------------" << endl;
  for (int i = 0; i < 20; i++){
    A[i] = i + 1;
    C[i] = A[i];
    cout << C[i] << " - ";
  }
  for (int i = 0; i < 30; i++){
    B[i] = 21 + i;
    C[i+20] = B[i];
    cout << C[i+20] << " - ";
  }
  cout << "FIM!" << endl;
  cout << "--------------------\n" << endl;
  return;
}

/* Exercício G:
Ler 20 elementos de uma matriz A tipo vetor.
Construir uma matriz B de mesma dimensão com os mesmos elementos da matriz A, sendo que deverão estar invertidos.
Ou seja, o primeiro elemento de A passa a ser o último de B, o segundo elemento de A passa a ser o penúltimo elemento de B e assim por diante.
Apresentar as matrizes A e B lado a lado.
*/

void exercG(){
  cout << "--------------------" << endl;
  int n = 20;
  int A[n];
  cout << "Vetor A: ";
  for (int i = 0; i < 20; i++){
    A[i] = i + 1;
    cout << A[i] << " - ";
  }
  cout << "FIM!" << endl;
  int B[n];
  int aux = 0;
  cout << "\nVetor B: ";
  for (int i = 0; i < n; i++){
    B[i] = A[n-i-1];
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
      case 'C':
        exercC();
        break;
      case 'D':
        exercD();
        break;
      case 'E':
        exercE();
        break;
      case 'F':
        exercF();
        break;
      case 'G':
        exercG();
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

