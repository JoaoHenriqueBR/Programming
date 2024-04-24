#include "iostream"
#include "cstdlib"
#include <stdio.h>
using namespace std;

typedef struct nopilha pilha;

struct nopilha{
  int valor;
  pilha *ant;
};

int cont; // para contar os nós
pilha *topo;

void construtor(){
  topo = NULL;
  cont = 0;
}

bool push(int valor){
  pilha *newpilha = (pilha*) malloc(sizeof(pilha));
  if (newpilha == NULL) return false;
  newpilha->valor = valor;
  newpilha->ant = topo;
  topo = newpilha;

  cont ++; // Incrementa quantidade de nós
  return true;
}

bool pop(){
  int valor;
  pilha *temp;

  temp = topo;
  valor = topo->valor;
  topo = topo->ant;

  free(temp);
  cout << "\nO valor removido foi: " << valor << endl;
  int c = getchar();
  return true;
}

void exibirpilha(){
  pilha *temp;
  temp = topo;
  while (temp->ant != NULL){
    cout << "\n" << temp->valor << endl;
    temp = temp->ant;
  }
  int c = getchar();
}

bool vazia(){
  if (topo == NULL) return true;
  else return false;
}

void destrutor(){
  pilha *temp;
  while (topo != NULL){
    temp = topo;
    topo = topo->ant;
    free(temp);
    cont--;
  }
  free(topo);

  cout <<"\nA pilha foi destruída!\n";
  int c = getchar();
}

int total(){
  while (temp == NULL){
    cont ++;
    temp = temp->ant;
  }
  return cont;
}

int main(){
  setlanguage(LC_ALL, "Portuguese");
  int tecla, valor;
  MENU:
    cout << "\n1 - Push\n2 - Pop\n3 - Exibir\n4 - Vazia\n5 - Destrutor\n6 - Total\n7 - Sair e destruir\nItem: ";
    cin >> tecla;
    switch (tecla){
      case 1:
        cout << "\nDigite o valor a ser empilhado: ";
        cin >> valor;
        push(valor);
        break;
      case 2:
      
    }
}