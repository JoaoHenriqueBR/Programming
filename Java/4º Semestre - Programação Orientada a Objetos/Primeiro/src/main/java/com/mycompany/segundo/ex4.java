package com.mycompany.segundo;
import java.util.Scanner;

/*
Ler a idade de uma pessoa e informar a sua classe eleitoral:

    - Não-eleitor (abaixo de 16 anos)
    - Eleitor obrigatório (entre 18 e 65 anos)
    - Eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)
 */
public class ex4 {
    public static void main (String[] args){
        int idade;

        Scanner input = new Scanner(System.in);
        System.out.println("Digite sua idade: ");
        idade = input.nextInt();

        if (idade < 16) {
            System.out.print("Não eleitor.");
        }
        else if (idade >= 18 && idade <= 65){
            System.out.print("Eleitor obrigatório. ");
        }
        else {
            System.out.print("Eleitor facultativo.");
        }
    }
}
