package com.mycompany.segundo;
import java.util.Scanner;

/*
Depois da liberação do governo para as mensalidades dos planos de saúde,
as pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito caro.
Um vendedor de um plano de saúde apresentou a tabela a seguir. Criar um programa
que entre com o nome e a idade de uma pessoa e mostre o valor que ela deverá pagar.

    - Até 10 anos - R$ 30
    - Acima de 10 até 29 anos - R$ 60
    - Acima de 29 até 45 anos - R$ 120
    - Acima de 45 até 59 anos - R$ 150
    - Acima de 59 até 65 anos - R$ 250
    - Maior que 65 anos - R$ 400
 */
public class ex5 {
    public static void main (String[] args){
        String nome;
        int idade;

        Scanner input = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        nome = input.next();
        System.out.println("Digite sua idade: ");
        idade = input.nextInt();

        if (idade <= 10) {
            System.out.println("Pagar: R$30.");
        }
        else if (idade <=29) {
            System.out.println("Pagar: R$60.");
        }
        else if (idade <=45) {
            System.out.println("Pagar: R$120.");
        }
        else if (idade <=59) {
            System.out.println("Pagar: R$150.");
        }
        else if (idade <=65) {
            System.out.println("Pagar: R$250.");
        }
        else {
            System.out.println("Pagar: R$400.");
        }

        System.out.println("Consulta finalizada, tenha uma ótima semana " + nome + "!");
    }
}