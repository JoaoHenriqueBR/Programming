#include "iostream"
#include "cstdlib"
#include <stdio.h>
using namespace std;

/*
Faça  um  programa  contendo  menu  de  controle  para  gerar  uma  quantidade  indefinida  de valores diferentes e armazenar em um ponteiro/vetor. Ao final exiba a média de todos os números gerados, o somatório, o maior valor e o menor valor;
*/


typedef struct dados db;

struct dados{
  double media;
  double soma;
  double maior;
  double menor;
};

db tb;
db *ptb = &tb;

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


void calcular(){
  double media = 0, soma = 0, maior, menor;
  if (cont == -1){
    cout << "Nenhum valor foi inserido ainda." << endl;
    return;
  }

  maior = v[0];
  menor = v[0];
  for (int i = 0; i <= cont; i++){
    ptb->soma += v[i];
    if (v[i] > maior) maior = v[i];
    if (v[i] < menor) menor = v[i];
  }
  ptb->media = ptb->soma / (cont + 1);
  ptb->maior = maior;
  ptb->menor = menor;
  return;
}

void exibir(){
  cout << "Média: " << ptb->media << endl;
  cout << "Somatório: " << ptb->soma << endl;
  cout << "Maior: " << ptb->maior << endl;
  cout << "Menor: " << ptb->menor << endl;
  return;
}

int main(){
  setlocale(LC_ALL, "Portuguese");
  int tecla;
  MENU:
    cout << "\n--- MENU ---\n1 - Adicione um valor \n2 - Exibir dados\n3 - Sair\nItem: ";
    cin >> tecla;
    switch(tecla){
      case 1:
        lerValor();
        break;
      case 2:
        calcular();
        exibir();
        break;
      case 3:
        cout << "\nSaindo do programa..." << endl;
        free(v);
        exit(0);
        break;
      default:
        cout << "\nOpção inválida!" << endl;
        break;
    }
  goto MENU;
  return 0;
}