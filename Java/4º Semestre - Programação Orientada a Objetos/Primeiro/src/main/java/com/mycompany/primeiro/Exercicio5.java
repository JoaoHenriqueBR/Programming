/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.primeiro;
import java.util.Scanner;
/**
 *
 * @author lab04aluno
 */
public class Exercicio5 {
    public static final double pi = 3.14159;
    
    public static void main(String arg[]){
        double altura, raio, volume;
        
        Scanner input = new Scanner(System.in );
        
        System.out.print("Digite a altura do cilindro: ");
        altura = input.nextDouble();
        
        System.out.print("Digite o raio do cilindro: ");
        raio = input.nextDouble();
        
        volume = pi * Math.pow(raio, 2) * altura;
        
        System.out.print("O volume do cilindro é de "+ volume + " cm³");
    }
}
