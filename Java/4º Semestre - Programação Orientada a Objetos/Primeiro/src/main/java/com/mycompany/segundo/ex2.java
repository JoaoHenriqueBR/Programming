package com.mycompany.segundo;
import java.util.Scanner;

// Ler três números e mostrá-los em ordem crescente.
public class ex2 {
    public static void main (String[] args){
        int n, maior = 0, menor = 0, meio = 0;

        Scanner input = new Scanner(System.in);

        for (int i = 0; i < 3; i++){
            System.out.println("Digite um número: ");
            n = input.nextInt();
            if (i == 0){
                maior = n;
                menor = n;
                meio = n;
            } else {
                if (n >= maior) {
                    meio = maior;
                    maior = n;
                }
                if (n <= menor){
                    meio = menor;
                    menor = n;
                }
            }


        }

        System.out.println(menor + " " + meio + " " + maior);
}
}
