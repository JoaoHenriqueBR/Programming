package com.mycompany.terceiro;

import java.util.Scanner;

/*
Um programa que calcule a média de um aluno nos moldes da FATEC Zona SUL.
 */


public class ex4 {

    public static void main(String[] args) {
        double P1, P2, T, media;
        
        Scanner input = new Scanner(System.in);

        try {
            System.out.println("Digite a nota da P1:");
            P1 = input.nextDouble();

            System.out.println("Digite a nota da P2:");
            P2 = input.nextDouble();

            System.out.println("Digite a nota de T:");
            T = input.nextDouble();

            media = (P1*0.35 + P2*0.50 + T*0.15);

            System.out.println("A média das notas é: " + media);
        } catch (Exception e) {
            // Captura qualquer exceção e exibe uma mensagem de erro
            System.out.println("Entrada inválida. Por favor, digite um número válido e tente novamente.");
        } finally {
            input.close();
        }

        

    }
}
