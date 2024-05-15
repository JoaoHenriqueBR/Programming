#include "stdio.h"
#include "math.h"
#include "stdlib.h"
const int n = 6;
double lista[] = {1, 2, 4, 5, -1, 0}; // Vetor desorganizado

int BuscaSeq (double x)
{   // função Busca linear
    for (int i = 0; i <= n-1; i++)
    {
        if(x == lista[i]) return i;
    }
    return -1;
}

int main()
{
    int indice; double v;
    printf("\nLista:\n"); // imprime a lista de valores do vetor
    for (int i = 0; i < n; i++)
    {
        printf("x%d %.2lf \n", i, lista[i]);
    }
    printf("\nBuscar a posição do valor:"); scanf("%lf", &v);
    indice = BuscaSeq ( v ); // Chama a função por referência
    if (indice == -1) 
        printf("\nValor não encontrado na lista acima!");
    else
        printf("\nValor encontrado na posição %d. \n", indice );
    return 0; 
}
