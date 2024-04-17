#include "iostream"
#include "cstdlib"
#include <stdio.h>
using namespace std;

int xy[] = {1, 5, 10, -1};



void maiorMenor(){
  int maior, menor;
  int tot = sizeof(xy)/sizeof(int);
  for (int i = 0; i<tot; i++){
    if (xy[i] > maior || i == 0) maior = xy[i];
    if (xy[i] < menor || i == 0) menor = xy[i];
  }
  cout << "\nMaior: " << maior;
  cout << "\nMenor: " << menor << endl;
  int c = getchar();
  return;
}

int linha = -1;
string nome[4]; int idade[4]; double salario[4];

string lerNome(){
  string nome;
  cout << "\nNome: ";
  cin.ignore(); // necessário para ignorar o ENTER do cin anterior
  getline(cin, nome);
  return nome;
}

int lerIdade(){
  int idade;
  cout << "\nIdade: ";
  cin >> idade;
  return idade;
}

double lerSalario(){
  double salario;
  cout << "\nSalário: ";
  cin >> salario;
  return salario;
}

void guardarDados(string nom, int ida, double sal){
  linha++;
  nome[linha] = nom;
  idade[linha] = ida;
  salario[linha] = sal;
  int c = getchar();
  return;
}

void listar(){
  for (int i=0; i<=linha; i++){
    cout << nome[i] << " - " << idade[i] << " - " << salario[i] << endl;
  }
  int c = getchar();
  return;
}

int main(){
  string nome_; int idade_; double salario_;
  int tecla;
  MENU:
    cout << "* Menu *\n1 - Maior e Menor\n2 - Ler\n3 - Exibir\n4 - Sair\nItem: ";
    cin >> tecla;
    switch (tecla){
      case 1: 
        maiorMenor();
        break;
      case 2: nome_ = lerNome();
        idade_ = lerIdade();
        salario_ = lerSalario();
        guardarDados(nome_, idade_, salario_);
        system("clear");
        break;
      case 3: listar();
        break;
      case 4: exit(0); break;
    }

   goto MENU;
  
return 0; }
