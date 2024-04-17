#include "iostream"
#include "math.h"
#include "cstdlib"
#include <stdio.h> // getchar (Linux)
using namespace std;

/*
  Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
  A fórmula de conversão é F ← (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
*/

int main()
{
  setlocale(LC_ALL, "Portuguese");

  double celsius, fahrenheit; // Variáveis locais

  cout << "Digite a temperatura em Celsius: ";
  cin >> celsius;

  fahrenheit = (9 * celsius + 160) / 5;

  cout << "A temperatura em Fahrenheit é: " << fahrenheit << endl;

  int c = getchar(); // No Windows: system("pause");

return 0; }
