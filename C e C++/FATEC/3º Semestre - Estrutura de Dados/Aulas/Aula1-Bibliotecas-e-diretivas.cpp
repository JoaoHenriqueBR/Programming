#include "iostream" // comandos cin e cout
#include "math.h" // Funções matemáticas
#include "cstdlib"
#include <stdio.h> // comado getchar, para um system("pause") no Linux
using namespace std; // diretiva using

int main()
{
    setlocale(LC_ALL, "Portuguese"); // configuração

    double base, expoente, potencia;

    cout << "\nDigite a base: ";
    cin >> base;

    cout << "\nDigite o expoente: ";
    cin >> expoente;

    potencia = pow(base, expoente);

    cout << base << " elevado a " << expoente << " é: ";
    cout << potencia << endl;

    int c = getchar();

return 0; }
