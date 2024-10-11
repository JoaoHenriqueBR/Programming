package com.mycompany.quarto;
import javax.swing.JOptionPane;

/*
EX6:
    Criar um programa que receba um número que corresponda a um mês do 1º tremestre e escreva o mês correspondente;
        caso o usuário digite o número fora do intervalo deverá aparecer inválido, mas utilizando um método do tipo void.
 */

public class ex6 {
    public static void main(String[] args) {
        int n;

        n = Integer.parseInt(JOptionPane.showInputDialog("Digite o número do mês (1º trimestre): "));

        if (n < 4){
            mesExtenso(n);
        } else {
            JOptionPane.showMessageDialog(null, "Número inválido. Digite um número entre 1 e 3.");
        }

    }

    private static void mesExtenso(int n) {
        String mes = "";
        switch (n) {
            case 1:
                mes = "Janeiro";
                break;
            case 2:
                mes = "Fevereiro";
                break;
            case 3:
                mes = "Março";
                break;
        }
        JOptionPane.showMessageDialog(null, "O mês correspondente é: " + mes);
    }
}
