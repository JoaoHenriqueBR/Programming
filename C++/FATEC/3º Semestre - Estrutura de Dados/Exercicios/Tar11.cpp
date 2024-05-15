#include "iostream"
#include "cstdlib"
#include <stdio.h>
#include "string"
using namespace std;

/*
Faça um algoritmo que leia uma quantidade indeterminada de números e também 
de nomes (nome completos). Crie funções para classificar os números de forma 
crescente e decrescente e também para classificar os nomes por ordem alfabética 
usando bubble sort. Crie uma opção de menu para buscar um número qualquer 
dentro do vetor de números e outra opção para buscar um nome qualquer dentro do 
vetor de nomes. Para fazer a classificação dos nomes, use a biblioteca do c, 
string.h e as funções strcmp() para comparar vetores e strcpy() para copiar strings e 
fazer o swap. Caso utilize o C++, então utilize o tipo string gerado pela biblioteca 
"string" para armazenar os strings, assim não irá precisar utilizar vetores do tipo 
char se for o C++ . 
*/

int cont = -1;
int c = -1;
string *nomes = nullptr;
double *numeros = NULL;

void lerValor() {
  int tecla;
  cout << "\n1 - Número\n2 - Nome\nItem: ";
  cin >> tecla;
  switch (tecla){
    case 1:
      c++;
      numeros = (double *) realloc(numeros, sizeof(double) * (c + 1));
      cout << "Digite o valor: ";
      cin >> numeros[c];
      break;
    case 2:
      cont++;
      if (cont == 0) {
        nomes = new string[1];
      } else {
        string* temp = new string[cont + 1];
        for (int i = 0; i < cont; i++) {
            temp[i] = nomes[i];
        }
        delete[] nomes;
        nomes = temp;
      }
      cout << "Digite o nome: ";
      cin >> nomes[cont];
      break;
    default:
      cout << "Opção inválida!" << endl;
      break;
  }
  return;
}

void classificarNumerosCrescente(double *numeros, int tamanho){
  for (int i = 0; i < tamanho-1; i++){
    for (int j = 0; j < tamanho-i-1; j++){
      if (numeros[j] > numeros[j+1]){
        double temp = numeros[j];
        numeros[j] = numeros[j+1];
        numeros[j+1] = temp;
      }
    }
  }
}

void classificarNumerosDecrescente(double *numeros, int tamanho){
  for (int i = 0; i < tamanho-1; i++){
    for (int j = 0; j < tamanho-i-1; j++){
      if (numeros[j] < numeros[j+1]){
        double temp = numeros[j];
        numeros[j] = numeros[j+1];
        numeros[j+1] = temp;
      }
    }
  }
}

void classificarNomes(string *nomes, int tamanho){
  for (int i = 0; i < tamanho-1; i++){
    for (int j = 0; j < tamanho-i-1; j++){
      if(nomes[j].compare(nomes[j+1]) > 0){
        string temp = nomes[j];
        nomes[j] = nomes[j+1];
        nomes[j+1] = temp;
      }
    }
  }
}

int buscarNumero(double *numeros, int tamanho, double n){
  for (int i = 0; i < tamanho; i++){
    if (numeros[i] == n){
      return i;
    }
  }
  return -1;
}

int buscarNome(string *nomes, int tamanho, string nome){
  for (int i = 0; i < tamanho; i++){
    if (nomes[i] == nome){
      return i;
    }
  }
  return -1;
}

void exibir(){
  cout << "\n--- Números ---\n";
  for (int i = 0; i <= c; i++){
    cout << numeros[i] << " | ";
  }
  cout << "\n--- Nomes ---\n";
  for (int i = 0; i <= cont; i++){
    cout << nomes[i] << " | ";
  }
  cout << endl;
}

int main()
{
  setlocale(LC_ALL, "Portuguese");
  int tecla;
  double n;
  string nome;
  MENU:
    cout << "\n--- MENU ---\n1 - Adicione um valor \n2 - Classificar números\n3 - Classificar nomes\n4 - Buscar número\n5 - Buscar nome\n6 - Exibir\n7 - Sair\nItem: ";
    cin >> tecla;
    switch(tecla){
      case 1:
        lerValor();
        break;
      case 2:
        cout << "\n1 - Crescente\n2 - Decrescente\nItem: ";
        cin >> tecla;
        switch(tecla){
          case 1:
            classificarNumerosCrescente(numeros, c+1);
            break;
          case 2:
            classificarNumerosDecrescente(numeros, c+1);
            break;
          default:
            cout << "Opção inválida!" << endl;
            break;
        }
        break;
      case 3:
        classificarNomes(nomes, cont+1);
        break;
      case 4:
        cout << "\nDigite o número: ";
        cin >> n;
        cout << "Posição: " << buscarNumero(numeros, c+1, n) << endl;
        break;
      case 5:
        cout << "\nDigite o nome: ";
        cin >> nome;
        cout << "Posição: " << buscarNome(nomes, cont+1, nome) << endl;
        break;
      case 6:
        exibir();
        break;
      case 7:
        cout << "\nSaindo do programa..." << endl;
        delete[] nomes;
        free(numeros);
        exit(0);
        break;
      default:
        cout << "\nOpção inválida!" << endl;
        break;
    }
  goto MENU;
  return 0;
}
