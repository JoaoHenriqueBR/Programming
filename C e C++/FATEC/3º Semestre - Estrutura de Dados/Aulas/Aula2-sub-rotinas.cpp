#include "iostream"
#include "math.h"
#include "cstdlib"
using namespace std;

/*
  Simulação 1 - Tipo Void


double const pi = 3.14; // constante
double altura = 5.55; // variável global

void verVolume (double raio); // declaração

int main()
{
  double raio = 10.5;
  verVolume(raio); // chamada por referência (Variável raio)
  verVolume(13.4); // chamada por valor (raio = 13.4)
  system("sleep 5");
}

// código do void
void verVolume (double raio)
{ double volume = raio * raio * pi * altura;
  cout << "O volume é: " << volume << cendl;
  system("sleep 5"); return;}

*/

/*
  Simulação 2 - Fuction (Não void) "incluir um menu interativo"
*/

int lern1 ();
int modulo (int numero);

int main()
{
  int num, modu;
  num = lern1();
  modu = modulo(num);
  cout << modu << endl;
  system("sleep 5");
}

int lern1 (){
  int n1;
  cout << "Digite um número: ";
  cin >> n1; return n1; }

int modulo (int numero) {
  int modu;
  if (numero < 0) modu = numero * -1;
  else modu = numero;
  return modu;
}