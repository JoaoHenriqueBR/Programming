/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.primeiro;
import java.util.Scanner;

/**
 *
 * @author live
 */
public class Exercicio1 {

    public static void main(String[] args) {
        String nome;
        double valor, resultado;
        
        Scanner input = new Scanner(System.in);
        
        System.out.print("Nome do seu produto: ");
        nome = input.next();
        System.out.print("Seu valor: R$ ");
        valor = input.nextDouble();
        
        resultado = valor*0.91;
        
        System.out.printf("Produto: %s", nome);
        System.out.printf("\nValor com desconto: R$ %s", resultado);
    }
}
