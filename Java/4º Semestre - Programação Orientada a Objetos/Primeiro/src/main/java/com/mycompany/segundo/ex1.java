package com.mycompany.segundo;
import java.util.Scanner;

// Ler um valor e informar se ele é ou não múltiplo de 3.
public class ex1 {
    public static void main (String[] args){
        int numero, resultado;

        Scanner input = new Scanner(System.in);
        System.out.println("Digite um número: ");
        numero = input.nextInt();

        resultado = numero % 3;

        if (resultado == 0) {
            System.out.print("O número é divisivel por 3.");
        }else {
            System.out.print("O número não é divisivel por 3.");
        }
    }
}
