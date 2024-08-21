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
public class Exercicio3 {
    public static void main(String [] args){
        float a, b, media;
        Scanner input = new Scanner(System.in);

        System.out.print("Digite o primeiro valor: ");
        a = input.nextFloat();
        
        System.out.print("Digite o segundo valor: ");
        b = input.nextFloat();
        
        media = (a + b) / 2;
        
        System.out.printf("Media: %s", media);
    }

    
    
}
