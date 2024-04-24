#include "stdio.h"
#include "stdlib.h"
#include "time.h"

int gerarNumeros () 
{ 
  return rand() % 100;
}

int main() 
{ 
  int n;
  srand (time(NULL)); // zerar o tempo da função rand() para números diferentes
  printf("Digite a qtde de numeros:");
  scanf("%i", &n);
  int *ai = (int *) calloc (n, sizeof(int)); // memoria para n elementos int
  for (int i=0;i<n;i++) ai [i] = gerarNumeros ();
  for (int i=0;i<n;i++) printf( "%i \n", ai[i] );
  return 0; 
}
