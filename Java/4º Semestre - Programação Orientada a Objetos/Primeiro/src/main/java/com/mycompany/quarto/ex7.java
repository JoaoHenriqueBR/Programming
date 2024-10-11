package com.mycompany.quarto;
import javax.swing.JOptionPane;

/*
EX7:
    Crie um programa que retorne o fatorial de um número, usando um método que retorne um valor e retorne o fatorial desse valor.
 */


public class ex7 {
    public static void main(String[] args) {
        int n;

        // Solicita ao usuário que insira um número
        n = Integer.parseInt(JOptionPane.showInputDialog("Digite um número para calcular o fatorial: "));

        // Chama o método fatorial e exibe o resultado
        long resultado = fatorial(n);
        JOptionPane.showMessageDialog(null, "O fatorial de " + n + " é: " + resultado);
    }

    // Método que calcula o fatorial de um número
    private static long fatorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Número deve ser não negativo.");
        }
        long fatorial = 1;
        for (int i = 1; i <= n; i++) {
            fatorial *= i;
        }
        return fatorial;
    }
}
