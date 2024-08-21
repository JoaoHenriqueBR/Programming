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
public class Exercicio4 {
    public static void main(String[] args){
        float c, f;
        
        Scanner input = new Scanner(System.in);
        
        System.out.print("Informe uma temporatura em Celsius: ");
        c = input.nextFloat();
        
        f = (9 * c + 160)/5;
        
        System.out.print("Em fahrenheit, a temperatura fica em "+ f + "ºF");
    }
}
