#include "iostream"
#include "cstdlib"
#include "math.h"
#include <stdio.h>
#define t 5
using namespace std;

/*
Faça o código fonte dos programas A, B da página 26 do livro Estudo dirigido de 
Algoritmos. a) Os dados de entrada e saída deverão ser armazenados em um struct com 
várias colunas; b) Deverá conter menu com switch case, funções para leitura dos dados 
de entrada e as respectivas funções para calcular os dados de saída; c) Tanto os dados 
de entrada quando os dados de saída deverão ser armazenados dentro de structs.
*/

/* PROGRAMA A:
Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
A fórmula de conversão é F ← (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
*/

/* PROGRAMA B:
Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é C ← (F - 32) * (5/9) , sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
*/

typedef struct lista tab;
struct lista{
  int pk[t];
  double cel[t];
  double fah[t];
};

tab tb1;

double lerCelsius(){
  double celsius;
  cout << "\nDigite a temperatura em Celsius: ";
  cin >> celsius;
  return celsius;
}

double lerFahrenheit(){
  double fahrenheit;
  cout << "\nDigite a temperatura em Fahrenheit: ";
  cin >> fahrenheit;
  return fahrenheit;
}

double convCelsius(double celsius){
  double fahrenheit;
  fahrenheit = (9 * celsius + 160) / 5;
  return fahrenheit;
}

double convFahrenheit(double fahrenheit){
  double celsius;
  celsius = (fahrenheit - 32) * 5 / 9;
  return celsius;
}

void newLinha(int linha, double celsius, double fahrenheit){
  tb1.pk[linha] = linha;
  tb1.cel[linha] = celsius;
  tb1.fah[linha] = fahrenheit;
}

void exibirTB1(int ultlin){
  system("clear");
  for(int pos = 0; pos <= ultlin; pos++){
    cout << tb1.pk[pos] << " | " << tb1.cel[pos] << "ºC | " << tb1.fah[pos] << "ºF" << endl;
  }
  cout << "\nDigite qualquer tecla para voltar ao menu: ";
  getchar();
}

int getCod(){
  int cod;
  cout << "\nDigite o código da conversão que deseja deletar: ";
  cin >> cod;
  return cod;
}

bool delLinha(int codpk, int ultlin)
{
  for (int i = 0; i <= ultlin; i++)
  {
    if (codpk == tb1.pk[i])
    {
      for (int j=i; j < ultlin; j++)
      {
        tb1.pk[j] = tb1.pk[j+1];
        tb1.cel[j] = tb1.cel[j+1];
        tb1.fah[j] = tb1.fah[j+1];
      } return true;
    } 
  } cout << "\n O campo " << codpk << " não foi encontrado!\n";
    int c = getchar();
    return false;
}

int main(void){
  setlocale(LC_ALL, "Portuguese");
  int linha = -1; bool deletar; int cod; double celsius_, fahrenheit_;
  int tecla;
  MENU:
    cout << "\n--- MENU ---\n1 - Conversão de Celsius para Fahrenheit\n2 - Conversão de Fahrenheit para Celsius\n3 - Exibir conversões\n4 - Deletar conversão\n5 - Sair\nItem: ";
    cin >> tecla;
    switch (tecla){
      case 1:
        linha ++;
        celsius_ = lerCelsius();
        newLinha(linha, celsius_, convCelsius(celsius_));
        break;
      case 2:
        linha ++;
        fahrenheit_ = lerFahrenheit();
        newLinha(linha, convFahrenheit(fahrenheit_), fahrenheit_);
        break;
      case 3:
        exibirTB1(linha);
        break;
      case 4:
        cod = getCod();
        deletar = delLinha(cod, linha);
        if (deletar){linha --; exibirTB1(linha);}
        break;
      case 5:
        cout << "\nSaindo do programa..." << endl;
        exit(0);
        break;
      default:
        cout << "\nOpção inválida!" << endl;
        break;
    }
  goto MENU;
  return 0;
}