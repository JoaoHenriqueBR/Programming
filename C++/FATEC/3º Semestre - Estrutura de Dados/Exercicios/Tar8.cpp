#include "iostream"
#include "cstdlib"
using namespace std;
#define t 5

/*
Faça um programa com menu de três opções (1-ler linha, 2- mostrar e 3- sair), contendo um STRUCT para 
cadastrar o nome, a idade, o sexo, salário e salarioNovo de pelo menos duas pessoas. Crie um ponteiro para 
manipular o STRUCT. O programa deverá conter as seguintes sub rotinas abaixo: (use switch case )
*/

typedef struct cadastro cad;
struct cadastro{
  string nome[t];
  int idade[t];
  string sexo[t];
  double salario[t];
  double salarioNovo[t];
};

cad tb;
cad *ptb = &tb;
int linha = -1;

int ler_idade(){
  int idade;
  cout << "Idade: "; cin >> idade; 
  return idade;
}

string ler_sexo(){
  string sexo;
  cout << "Sexo: "; cin >> sexo; 
  return sexo;
}

string ler_nome(){
  string nome;
  cout << "Nome: "; cin >> nome; 
  return nome;
}

double ler_salario(){
  double salario;
  cout << "Salário: R$ "; cin >> salario;
  return salario;
}

double getAumento(double *salario){ // Aumento de 10% sobre o salário digitado
  return ((*salario) + (*salario / 10));
}

void NovaLinhaStruct(){
  if (linha == t-1) return;
  linha ++;
  cout << "\n--- PESSOA " << linha + 1 << " ---" << endl;
  ptb->nome[linha] = ler_nome();
  ptb->sexo[linha] = ler_sexo();
  ptb->idade[linha] = ler_idade();
  
  double salario = ler_salario();
  ptb->salario[linha] = salario;
  ptb->salarioNovo[linha] = getAumento(&salario);
  return;
}

void listarLinhasStruct(){
  system("clear");
  cout << "*** Exibição de Dados ***\n";
  for (int i = 0; i <= linha; i++)
    cout << ptb->nome[i] << ", " << ptb->sexo[i] << " - " << ptb->idade[i] << " Anos. | Antigo: R$ " << ptb->salario[i] << " / Novo: R$ " << ptb->salarioNovo[i] << endl;
  system("sleep 4");
}



int main(){
  setlocale(LC_ALL, "Portuguese");
  int tecla;
  MENU:
    cout << "\n--- MENU ---\n1- Ler Linha\n2- Mostrar\n3- Sair\nItem: ";
    cin >> tecla;
    switch(tecla){
      case 1:
        NovaLinhaStruct();
        break;
      case 2:
        listarLinhasStruct();
        break;
      case 3:
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
