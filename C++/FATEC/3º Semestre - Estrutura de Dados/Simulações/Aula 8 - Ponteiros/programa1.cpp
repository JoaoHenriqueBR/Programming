#include "iostream"
#include "cstdlib"
using namespace std;

/* PONTEIRO APONTANDO PARA UMA VARIÁVEL
Todo ponteiro deverá ser inicializado logo depois de criado, um ponteiro têm que ser 
exatamente do tipo da variável que ele irá armazenar o valor ou apontar.
No programa abaixo, a variável aux têm um endereço de memória chamado &aux e um 
ponteiro apontando para ela que é o *ptaux. Para apontar um ponteiro para o endereço de uma 
variável, o asterisco deve ser retirado: ptaux = &aux

*/

int main () { setlocale(LC_ALL, "Portuguese");
  int aux = 10; // cria uma variável inteira
  int *ptaux; // cria um ponteiro inteiro
  ptaux = &aux; // inicializa o ponteiro 
  cout<< "\nO valor de aux é:"<< aux;
  cout<< "\nO endereço de memória de aux é :"<< &aux;
  cout<< "\nO endereço de memória de aux é :"<< ptaux;
  cout<< "\nO endereço de memória ptaux é:" << &ptaux;
  cout<< "\nO valor de aux é:" << *ptaux << endl;
  system("sleep 5"); return 0; } 
