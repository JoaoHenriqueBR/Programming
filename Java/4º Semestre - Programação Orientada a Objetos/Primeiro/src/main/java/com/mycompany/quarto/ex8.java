package com.mycompany.quarto;
import javax.swing.JOptionPane;

/*
EX8:
    Crie um programa que verifique se um número é primo ou não, através de um método.
        Número primo é divisível somente por 1 e ele mesmo.
 */

public class ex8 {
    public static void main(String[] args) {
        int n;

        // Solicita ao usuário que insira um número
        n = Integer.parseInt(JOptionPane.showInputDialog("Digite um número para verificar se é primo: "));

        // Chama o método isPrimo e exibe o resultado
        if (isPrimo(n)) {
            JOptionPane.showMessageDialog(null, n + " é um número primo.");
        } else {
            JOptionPane.showMessageDialog(null, n + " não é um número primo.");
        }
    }

    // Método que verifica se um número é primo
    private static boolean isPrimo(int n) {
        if (n <= 1) {
            return false; // Números menores ou iguais a 1 não são primos
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false; // Se n é divisível por i, não é primo
            }
        }
        return true; // Se não encontrou divisores, é primo
    }
}
