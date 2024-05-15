#include "stdio.h"

// Exemplo1 de algoritmo com complexidade Big O (1)

double mediaExtremos(int v[], int n)
{
    return ((v[0] + v[n])/2);
}

int main()
{
    int n = 10;
    int x[] =  { 1, 2, 3, 3, 4, 56, 6, 6, 6, 6, 6 };
    printf("%d \n", mediaExtremos (x, n));
    n = 15;
    int y []={-1,2,-5,-6,1, 2, 3, 3, 4, 56, 6, 6, 6, 6, 6 };
    printf("%d \n", mediaExtremos (y, n));
    return 0;
}
