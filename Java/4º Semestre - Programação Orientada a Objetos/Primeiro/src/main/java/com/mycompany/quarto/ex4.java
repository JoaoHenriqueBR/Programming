package com.mycompany.quarto;
import javax.swing.JOptionPane;

/*
EX4:
    Criar um programa que receba um grau e o converta para radianos através de um método.
        Fórmula: radiano = grau * pi / 180
 */

public class ex4 {
    public static final float PI = 3.1416F;

    public static void main(String[] args){
        int grau;

        grau = Integer.parseInt(JOptionPane.showInputDialog("Digite um número: "));

        calcRadiano(grau);
    }

    private static void calcRadiano(int grau){
        double radiano = grau * PI / 180;

        JOptionPane.showMessageDialog(null, "Radiano de " + grau + "º = " + radiano);
    }
}
