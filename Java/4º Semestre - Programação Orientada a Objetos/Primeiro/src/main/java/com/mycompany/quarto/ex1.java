package com.mycompany.quarto;
import javax.swing.JOptionPane;


public class ex1 {
    public static void main(String[] args){
        int n, dobro;

        n = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite um número inteiro: "));

        dobro = n * 2;

        JOptionPane.showMessageDialog(null, "Dobro: " + dobro);
    }
}
