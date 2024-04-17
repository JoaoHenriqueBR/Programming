#include "iostream"
#include "cstdlib"
using namespace std;

/*
Crie um algoritmo que armazene dois valores e faça a troca de valores, entretanto, utilize ponteiros como parâmetros das sub-rotinas envolvidas.
*/

double a = 10;
double *pta; // declarando um ponteiro do tipo double.

double media (double *x, double *y)
{
  return (*x + *y) / 2;
}

void trocar(double *a, double *b)
{
  double aux;
  aux = *a;
  *a = *b;
  *b = aux;
}

int main()
{
  pta = &a; // inicializando o ponteiro e apontá-lo para alguma coisa.

  cout << "O endereço de A: " << &a << endl;
  cout << "O valor de A: " << a << endl;
  cout << "O endereço de A: " << pta << endl;
  cout << "O valor de A: " << *pta << endl;
  cout << "O endereço de memória de pta: " << &pta << endl;

  double x1 = 10.5;
  double x2 = 5.3;
  cout << "A média é: " << media(&x1, &x2) << endl;
  system("sleep 5");
  system("clear");

  cout << "O valor de x1: " << x1 << "e o valor de x2: " << x2 << endl;

  // a = &x1;
  // o valor de x1 é *a
  // o endereço de x1 é a
  trocar(&x1, &x2);
  
  cout << "O valor de x1: " << x1 << "e o valor de x2: " << x2 << endl;

  return 0;
}
