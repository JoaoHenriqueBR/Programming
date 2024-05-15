#include "stdio.h"
#include "math.h"
#include "stdlib.h"

int const n = 6;
int x[] = {1, -1, 5, 4, 5, -10};

void bolha()
{
    int aux;
    for (int i=0; i<=n-2; i++)
        for (int j=i; j<=n-1;j++)
            if ( x[i] > x[j] )
            {
                aux = x[i];
                x[i] = x[j];
                x[j] = aux;
            }
}

void exibir()
{
    printf("\n\n\n\n");
    for (int i = 0; i<=n-1; i++)
    {
        printf("[%i]:[%i] \n",i, x[i]);
    }
    printf("\n\n");
    system("sleep 5");
}

int main()
{
    exibir();
    bolha();
    exibir();
    return 0;
}