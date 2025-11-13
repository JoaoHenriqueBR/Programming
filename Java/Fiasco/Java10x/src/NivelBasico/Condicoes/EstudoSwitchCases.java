package Fiasco.Java10x.src.NivelBasico.Condicoes;

import java.util.Scanner;

public class EstudoSwitchCases {
    static void main(String[] args) {
        /*
        * SwitchCases: Servem para gerar casos específicos
        * Objetivo: Pedir pro usuario escolher entre os Ninjas
        * switchCase
        * */

//        Pedir para o usuário
        Scanner input = new Scanner(System.in);

//        Mostrar opções para o usuário
        System.out.println("1 - Naruto Uzumaki");
        System.out.println("2 - Sasuke Uchiha");
        System.out.println("3 - Sakura Haruno");
        System.out.println("Escolha um personagem: ");


//        Pedir para o usuário escolher uma das opções
        int escolha = input.nextInt();

        System.out.println("Você digitou o número: " + escolha);

//        Reação ao escolher um usuário
        switch (escolha){
            case 1:
                System.out.println("Você escolheu o Naruto Uzumaki");
                break;
            case 2:
                System.out.println("Você escolheu o Sasuke Uchiha");
                break;
            case 3:
                System.out.println("Você escolheu a Sakura Haruno");
                break;
            default:
                System.out.println("Valor inválido! Tente novamente.");
                break;
        }

//        Fecha o Scanner
        input.close();
    }
}
