package com.mycompany.quarto;
import javax.swing.JOptionPane;

public class ex2 {
    public static void main(String[] args){
        double n1, n2, n3, n4, media;

        n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite a primeira nota (1/4): "));
        n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite a segunda nota (2/4): "));
        n3 = Integer.parseInt(JOptionPane.showInputDialog("Digite a terceira nota (3/4): "));
        n4 = Integer.parseInt(JOptionPane.showInputDialog("Digite a última nota (4/4): "));

        media = (n1+n2+n3+n4) / 4;

        JOptionPane.showMessageDialog(null, "Médial Final: " + media);
    }


}
