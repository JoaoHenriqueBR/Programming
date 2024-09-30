package com.mycompany.quarto;
import javax.swing.JOptionPane;

/*
EX2:
    Criar um programa que receba 4 notas e calcule a média aritmética, através de um método.
 */

public class ex2 {
    public static void main(String[] args){
        double n1, n2, n3, n4;

        n1 = Double.parseDouble(JOptionPane.showInputDialog("Digite a primeira nota (1/4): "));
        n2 = Double.parseDouble(JOptionPane.showInputDialog("Digite a segunda nota (2/4): "));
        n3 = Double.parseDouble(JOptionPane.showInputDialog("Digite a terceira nota (3/4): "));
        n4 = Double.parseDouble(JOptionPane.showInputDialog("Digite a última nota (4/4): "));

        calcMedia(n1, n2, n3, n4);

    }

    private static void calcMedia(double n1, double n2, double n3, double n4){
        double media = (n1+n2+n3+n4) / 4;

        JOptionPane.showMessageDialog(null, "Médial Final: " + media);
    }

}
