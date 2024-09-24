package com.mycompany.terceiro;

import java.util.Scanner;

/*
Um programa capaz de imprimir todos os números primos em um intervalo de números informado pelo usuário;
 */


public class ex3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
 
        try {
            // Solicita ao usuário o intervalo de números
            System.out.print("Digite o início do intervalo: ");
            int inicio = scanner.nextInt();
            System.out.print("Digite o fim do intervalo: ");
            int fim = scanner.nextInt();
 
            // Verifica se o intervalo é válido
            if (inicio > fim) {
                System.out.println("O início do intervalo deve ser menor ou igual ao fim.");
                return;
            }
 
            // Imprime todos os números primos no intervalo
            System.out.println("Números primos no intervalo de " + inicio + " a " + fim + ":");
            for (int i = inicio; i <= fim; i++) {
                if (isPrimo(i)) {
                    System.out.print(i + " ");
                }
            }
            System.out.println();
 
        } catch (Exception e) {
            // Captura qualquer exceção e exibe uma mensagem de erro
            System.out.println("Entrada inválida. Por favor, digite números inteiros.");
        } finally {
            // Fecha o scanner
            scanner.close();
        }
    }
 
    // Função para verificar se um número é primo
    private static boolean isPrimo(int numero) {
        if (numero <= 1) {
            return false;
        }
        if (numero <= 3) {
            return true;
        }
        if (numero % 2 == 0 || numero % 3 == 0 || numero % 5 == 0) {
            return false;
        }
        return true;
    }
}
