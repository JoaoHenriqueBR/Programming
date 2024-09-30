package com.mycompany.quarto;
import javax.swing.JOptionPane;

/*
EX1:
    Criar um programa que permita a entrada de um número inteiro e retorne o seu dobro, através de um método.
 */

public class ex1 {
    public static void main(String[] args){
        int n;

        n = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite um número inteiro: "));

        JOptionPane.showMessageDialog(null, "Dobro: " + calcDobro(n));


    }
    private static int calcDobro(int n){
        int dobro = n * 2;

        return dobro;
    }
}


