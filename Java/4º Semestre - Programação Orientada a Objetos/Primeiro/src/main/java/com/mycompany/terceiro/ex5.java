package com.mycompany.terceiro;

import java.util.Scanner;

/*
Criar um programa que leia um número que será o limite superior de um intervalo e o incremento.
Exibir todos os números naturais no intervalo de 0 até esse número.
Suponha que os dois números lidos são maiores que zero.
 */

public class ex5 {

    public static void main(String[] args) {
        int lim_sup, inc, resultado = 0;
        
        Scanner input = new Scanner(System.in);

        try {
            System.out.println("Digite o limite superior do intervalo:");
            lim_sup = input.nextInt();

            System.out.println("Digite o incremento do intervalo:");
            inc = input.nextInt();

            if (inc > lim_sup){
                System.out.printf("Entrada inválida. O incremento deve ser menor que o limite superior.");
                System.exit(0);
            }

            System.out.println("\nResultado:");
            for (int i = 0; lim_sup >= resultado; i++) {
                System.out.println(resultado);
                resultado = resultado + inc;
            }
        } catch (Exception e){
            System.out.printf("Entrada inválida. Por favor, digite um número inteiro e tente novamente.");
        } finally {
            input.close();
        }

    }
}
