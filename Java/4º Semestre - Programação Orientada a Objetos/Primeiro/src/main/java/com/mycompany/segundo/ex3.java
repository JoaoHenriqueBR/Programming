package com.mycompany.segundo;
import java.util.Scanner;

/*
Um comerciante comprou um produto e quer vendê-lo com um lucro de 45%
se o valor da compra for menor que R$20,00;
Caso contrário, o lucro será de 30%.
Entrar com o valor do produto e imprimir o valor da venda.
 */
public class ex3 {
    public static void main (String[] args){
        double valor, produto;

        Scanner input = new Scanner(System.in);
        System.out.println("Digite o valor do produto: ");
        produto = input.nextFloat();

        if (produto < 20) {
            valor =  produto + (produto*0.45);
            System.out.print("O valor do produto será: R$"+ valor);
        }else {
            valor =  produto + (produto*0.3);
            System.out.print("O valor do produto será: R$"+ valor);
        }
    }
}
