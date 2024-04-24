#include"iostream"
#include"cstdlib"
using namespace std;

int main () 
{  
  setlocale (LC_ALL, "Portuguese");
  int * ptx = (int *)  malloc( sizeof ( int ) ); // aloca 4 bytes para um inteiro
  if (ptx == NULL) cout << "\nNão foi possível a alocação de memória!";
  else  
  { 
    *ptx = 10;
    cout << "O valor " << *ptx << " será armazenado na memória " << ptx << endl; 
  }
  free (ptx);  // liberar a memória
  return 0; 
}
