/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.exercicio1;
import java.util.Scanner;

/**
 *
 * @author joao
 */
public class Main {
    public static int soma(int a, int b){
        return a + b;
    }
    
    public static int subtracao(int a, int b){
        return a - b;
    }
    
    public static int multiplicacao(int a, int b){
        return a * b;
    }
    
    public static double divisao(int a, int b){
        return (double) a / (double) b;
    }
    
    public static void main(String[] args){
        int a, b;
        
            
        Scanner input = new Scanner(System.in);
        
        Robo R2D2 = new Robo();
        R2D2.setNome("R2D2");
        R2D2.setData("20/08/2024");
        R2D2.setBateria(10);
        
        System.out.println("Olá, sou um robô e me chamo " + R2D2.getNome());
        System.out.println("Fui fabricado em " + R2D2.getData());
        
        for (int i = 0; i < R2D2.getBateria(); i++){
            System.out.println("Tenho " + (R2D2.getBateria() - i) + "% de bateria restando");
            
            System.out.print("Digite um número (0 > Parar): ");
            a = input.nextInt();
            
            if (a == 0) break;

            
            System.out.print("Digite outro (0 > Parar): ");
            b = input.nextInt();
            
            if (b == 0) break;
            
            System.out.println("\nSoma: " + soma(a, b));
            System.out.println("Subtração: " + subtracao(a, b));
            System.out.println("Multiplicação: " + multiplicacao(a, b));
            System.out.println("Divisão: " + divisao(a, b));
            
            
        }
        
        System.out.println("\nDesligando R2D2...");
    }
}
