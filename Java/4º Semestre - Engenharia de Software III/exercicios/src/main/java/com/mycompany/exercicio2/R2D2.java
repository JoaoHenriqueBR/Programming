package com.mycompany.exercicio2;
import java.util.Scanner;

public class R2D2 extends Robo {
    public static void main(String[] args){
        int a, b;

        // Scanner
        Scanner input = new Scanner(System.in);

        // Obj R1
        Robo R2D2 = new Robo();
        R2D2.setNome("R2D2");
        R2D2.setData("28/08/24");
        R2D2.setBateria(10);

        // Obj C1
        Calculadora calc = new Calculadora();

        // Apresentação
        System.out.println("Olá, sou um robô e me chamo " + R2D2.getNome());
        System.out.println("Fui fabricado em " + R2D2.getData());

        // Funcionamento
        for (int i = 0; i < R2D2.getBateria(); i++){
            System.out.println("Tenho " + (R2D2.getBateria() - i) + "% de bateria restando");

            System.out.print("Digite um número (0 > Parar): ");
            a = input.nextInt();

            if (a == 0) break;


            System.out.print("Digite outro (0 > Parar): ");
            b = input.nextInt();

            if (b == 0) break;

            System.out.println("\nSoma: " + calc.Soma(a, b));
            System.out.println("Subtração: " + calc.Subtrair(a, b));
            System.out.println("Multiplicação: " + calc.Multiplicar(a, b));
            System.out.println("Divisão: " + calc.Dividir(a, b));


        }

        // Finalização
        System.out.println("\nDesligando R2D2...");
    }
}
