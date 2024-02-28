#include "iostream"
#include "math.h"
#include "cstdlib"
#include <stdio.h> // getchar (Linux)
#include <iomanip> // setprecision (Limitar casas decimais)
using namespace std;

/*
  Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
  Para obter o cálculo, o usuário deve fornecer o tempo gasto (TEMPO) e a velocidade média (VELOCIDADE) durante a viagem. 
  Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA ← TEMPO * VELOCIDADE. 
  Possuindo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a fórmula LITROS_USADOS ← DISTANCIA / 12. 
  Ao final, o programa deve apresentar os valores da velocidade média (VELOCIDADE), tempo gasto na viagem (TEMPO), a distância percorrida (DISTANCIA)
  e a quantidade de litros (LITROS_USADOS) utilizada na viagem.
*/

int main()
{
  setlocale(LC_ALL, "Portuguese");

  double tempo, velocidade, distancia, litros_usados; // variáveis locais

  cout << "Digite o tempo gasto na viagem (em horas): ";
  cin >> tempo;

  cout << "Digite a velocidade média durante a viagem (em km/h): ";
  cin >> velocidade;

  distancia = tempo * velocidade;
  litros_usados = distancia / 12;

  cout << "\nA velocidade média foi de " << velocidade << " km/h.";
  cout << "\nForam gastos " << tempo << " horas na viagem.";
  cout << "\nFoi percorrido uma distância de " << distancia << " km.";

  cout << fixed << setprecision(1); // Limita a casa decimal do próximo cout, assim o arredondando.

  cout << "\nA quantidade de litros utilizada na viagem foi de " << litros_usados << " litros" << endl;

  int c = getchar(); // No Windows: system("pause");
  
return 0; }
