/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.primeiro;
import java.util.Scanner;

/**
 *
 * @author live
 */
public class Exercicio2 {
    public static void main(String[] args){
        float salarioMinimo, salario, resultado;
        Scanner input = new Scanner(System.in);
        
        System.out.println("Digite o salario Minimo: ");
        salarioMinimo = input.nextFloat();
        System.out.println("Digite o seu salário: ");
        salario = input.nextFloat();
        
        resultado = salario/salarioMinimo;
        
        System.out.print("Você recebe " + resultado + " salarios minimos");
        
    }
}

