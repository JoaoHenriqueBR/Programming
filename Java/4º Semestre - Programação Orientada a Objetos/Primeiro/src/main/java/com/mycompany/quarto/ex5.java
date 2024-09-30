package com.mycompany.quarto;
import javax.swing.JOptionPane;

/*
EX5:
    Criar um programa que mostre qual o valor maior entre dois números, utilizando um método do tipo void (que não retorna valores).
 */

public class ex5 {
    public static void main(String[] args){
        int n1, n2;

        n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite um número: "));
        n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite outro: "));

        maior(n1, n2);
    }

    private static void maior(int n1, int n2){
        if (n1 > n2){
            JOptionPane.showMessageDialog(null, n1 + " é o maior.");
        } else if (n2 > n1) {
            JOptionPane.showMessageDialog(null, n2 + " é o maior.");
        } else {
            JOptionPane.showMessageDialog(null, "Ambos são iguais.");
        }
    }
}
