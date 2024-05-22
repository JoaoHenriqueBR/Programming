#include "iostream"
#include "cstdlib"
#include <stdio.h>
using namespace std;


// Representação de um NÓ com STRUCT


typedef struct nopilha pilha;

/*
Para representar um NÓ da LIFO, utilizaremos um STRUCT com um
ponteiro interior chamado ANT que sempre irá armazenar o endereço
do nó anterior até chegar no primeiro que irá apontar para NULL.
*/

struct nopilha{
  int valor;
  pilha *ant;
};

int cont; // para contar os nós
pilha *topo;

// O código construtor de uma LIFO terá o objetivo de inicializar o ponteiro topo com NULL

void construtor(){
  topo = NULL;
  cont = 0;
}

// Código para Inserir Elementos na LIFO

bool push(int valor){
  pilha *newpilha = (pilha*) malloc(sizeof(pilha)); // cria um novo Nó chamado newpilha do tipo pilha.
  if (newpilha == NULL) return false; // devolve false caso não seja possível a alocação de memória.

  newpilha->valor = valor;
  newpilha->ant = topo;
  topo = newpilha;

  cont ++; // Incrementa quantidade de nós
  return true;
}

// Código para remover elementos da LIFO

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

// Código para exibir a LIFO

void exibirpilha(){
  pilha *temp;
  temp = topo;
  while (temp->ant != NULL){
    cout << "\n" << temp->valor << endl;
    temp = temp->ant;
  }
  cout << "\n" << temp->valor << endl;
}

// Código para verificar se a LIFO está vazia

bool vazia(){
  if (topo == NULL) return true;
  else return false;
}

// Código para destruir uma LIFO dinâmica

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

// Código que retorna o total de elementos da FIFO

int total(){
  pilha *temp;
  temp = topo;
  int cont = 0;
  while (temp != NULL){
    cont ++;
    temp = temp->ant;
  }
  return cont;
}

// Menu Principal

int main(){
  setlocale(LC_ALL, "Portuguese");
  int tecla, valor;
  MENU:
    cout << "\n1 - Push\n2 - Pop\n3 - Exibir\n4 - Total\n5 - Sair e destruir\nItem: ";
    cin >> tecla;
    switch (tecla){
      case 1:
        cout << "\nDigite o valor a ser empilhado: ";
        cin >> valor;
        push(valor);
        break;
      case 2:
        if (vazia() == false)
        {
          pop();
        }
        else
        {
          cout << "A LIFO está vazia" << endl;
        }
        break;
      case 3:
        if (vazia() == false)
        {
          exibirpilha();
        }
        else
        {
          cout << "A LIFO está vazia" << endl;
        }
        break;
      case 4:
        cout << "LIFO de " << total() << " elementos." << endl;
        break;
      case 5:
        cout << "Destruindo LIFO..." << endl;
        destrutor();
        exit(0);
        break;
      default:
        cout << "\nOpção Inválida!" << endl;
        break;
    }
  goto MENU;
  return 0;
}