#include "iostream"
#include "cstdlib"
#include <stdio.h>
#define t 5
using namespace std;

// cria uma estrutura e um alias (apelido) chamado tab para o mesma.
typedef struct lista tab;
struct lista
{
  int pk[t];
  string nom[t];
  double sal[t];  
};

tab tb1;

string getNome()
{
  string nome;
  cout << "Digite o nome: ";
  cin >> nome;
  return nome;
}

double getSalario()
{
  double sa;
  cout << "Digite o salário: ";
  cin >> sa;
  return sa;
}

void newlinha(int linha, string nome, double salario, int codpk)
{
  tb1.pk[linha] = codpk;
  tb1.nom[linha] = nome;
  tb1.sal[linha] = salario;
}

void exibirTB1(int ultlinha)
{
  system("clear");
  for (int pos=0; pos <= ultlinha; pos++)
  {
    cout << tb1.pk[pos] << " | " <<tb1.nom[pos] << " | " << tb1.sal[pos] << endl;
  }
  do {
     cout << '\n' << "Pressione Enter para continuar.";
  } while (cin.get() != '\n'); // Outra alternativa para o system("pause").
}

bool delLinha(int codpk, int ultlin)
{
  for (int i = 0; i <= ultlin; i++) // for de busca
  {
    if (codpk == tb1.pk[i])
    {
      for (int j=i; j < ultlin; j++) // for de atualização/deleta
      {
        tb1.pk[j] = tb1.pk[j+1];
        tb1.nom[j] = tb1.nom[j+1];
        tb1.sal[j] = tb1.sal[j+1];
      } return true;
    } 
  } cout << "\n O campo " << codpk << " não foi encontrado!\n";
    int c = getchar();
    return false;
}

int main(void)
{
  setlocale(LC_ALL, "Portuguese");
  string nome; double salario; int linha = -1; bool deletar;
  
  linha ++;
  newlinha(linha, "Eliseu", 100000, 001);
  linha ++;
  newlinha(linha, "Sara", 20000, 002);
  linha ++;
  newlinha(linha, "Leandra", 50000, 003);
  exibirTB1(linha);
  
  deletar = delLinha(002, linha);
  if (deletar){linha --; exibirTB1(linha);}
  
  deletar = delLinha(001, linha);
  if (deletar){linha --; exibirTB1(linha);}
  
  deletar = delLinha(004, linha);
  if (deletar){linha --; exibirTB1(linha);}
  /*
  nome = getNome(); // Leitura do nome
  salario = getSalario(); // Leitura do salario
  linha ++;
  newlinha(linha, nome, salario);
  */
  return 0;
}
