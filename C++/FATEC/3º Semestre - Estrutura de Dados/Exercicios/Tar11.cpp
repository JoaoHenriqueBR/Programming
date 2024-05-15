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

double *v = NULL;
int cont = -1;

void lerValor(){
  cont++;
  v = (double *) realloc(v, sizeof(double) * (cont+1));
  if (v == NULL) {
    cout << "ERRO: Não foi possível alocar memória!" << endl;
    exit(1);
  } else {
    cout << "Digite o valor: "; 
    cin >> v[cont];
  }
  return;
}

int main()
{
    lerValor();
    return 0;
}
