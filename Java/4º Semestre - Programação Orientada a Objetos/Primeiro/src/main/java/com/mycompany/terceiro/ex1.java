package com.mycompany.terceiro;

import javax.swing.JOptionPane;
import java.util.ArrayList;

/*
Um programa capaz de imprimir todos os números pares em um intervalo de números informado pelo usuário;
 */

public class ex1 {
    public static void main(String[] args) {
 
        int valor01 = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite o primeiro valor: "));
        int valor02 = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite o segundo valor: "));
 
        ArrayList<Integer> pares = new ArrayList<>();
 
        for (int i = valor01; i <= valor02; i++) {
           if (i % 2 == 0) {
               pares.add(i);
           }
        }
        JOptionPane.showMessageDialog(null, "Os valores pares do intervalo digitado sao: " + pares);
    }
}
