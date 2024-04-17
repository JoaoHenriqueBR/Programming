#include "iostream"
#include "cstdlib"
using namespace std;

/* PONTEIROS COMO ARGUMENTOS EM SUB ROTINAS
Neste Swap com ponteiros, o void trocar () possui dois ponteiros como 
argumentos, isso significa que teremos que enviar dois endereços de memória um para o 
ponteiro *x e outro para o ponteiro *y.
A variável aux recebe o conteúdo do ponteiro *x. o ponteiro *x recebe o conteúdo do 
ponteiro *y, o ponteiro *y recebe o conteúdo de aux que é um número qualquer. 
No main(), ao executar o void trocar ( ) os endereços de &a e &b são enviados para 
dentro dos argumentos *x e *y.
*/

void trocar (int *x, int *y) { int aux;
  aux = *x;
  *x = *y;
  *y = aux; }

int main() { int a = 10, b = 20;
  cout << "\nValor inicial de A:" << a ;
  cout << "\nValor inicial de B:" << b ; int c = getchar();
  trocar ( &a, &b );
  cout << "\nValor Final de A:" << a ; 
  cout << "\nValor Final de B:" << b ; c = getchar(); return 0; }
