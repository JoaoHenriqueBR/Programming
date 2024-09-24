package com.mycompany.terceiro;

import javax.swing.JOptionPane;

/*
Um programa que imprima até o "n" termo a sequência de Fibonacci.
 */


public class ex2 {
    public static void main(String[] args) {
        int n = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite o termo inicial: "));
 
        int termo1 = 0;
        int termo2 = 1;
 
        StringBuilder resultado = new StringBuilder("Sequencia até o " + n + "º termo:\n");
        resultado.append(termo2).append(" ");
        if (n>1){
            for(int i = 3; i <= n+1; i++){
                int nextTerm = termo1 + termo2;

                resultado.append (nextTerm).append(" ");
                termo1  = termo2;
                termo2  = nextTerm;
            }
        }

    
    JOptionPane.showMessageDialog(null, resultado.toString()); 
    }
}
