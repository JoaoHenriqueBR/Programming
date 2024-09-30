package com.mycompany.quarto;
import javax.swing.JOptionPane;

/*
EX3:
    Criar um programa que receba 2 valores e calcule o produto através de um método que retorna valores.
 */

public class ex3 {
    public static void main(String[] args){
        int n1, n2;

        n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite um número: "));
        n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite outro: "));

        JOptionPane.showMessageDialog(null, "Produto entre " + n1 + " * " + n2 + " = " + calcProduto(n1, n2));

    }

    private static int calcProduto(int n1, int n2){
        int produto = n1 * n2;

        return produto;
    }
}
