package Fiasco.Java10x.src.NivelBasico.Condicoes;

import java.util.Scanner;

public class ScannerDoUsuario {
    static void main(String[] args) {
        /*
         * Scanner = É um jeito de trazer o usuário para dentro da aplicação.
         * Objetivo: O usuário vai trazer um ninja e vamos validar os dados.
         * */

//    Abrir o Scanner
        Scanner caixaDeTexto = new Scanner(System.in);

//        Receber o nome do Ninja
        System.out.println("Escreva aqui o nome do seu ninja: ");
        String nomeDoNinja = caixaDeTexto.nextLine();
        System.out.println("O nome do ninja é: " + nomeDoNinja);

//        Receber a idade do Ninja
        System.out.println("Escreva aqui a idade do seu ninja: ");
        int idadeDoNinja = caixaDeTexto.nextInt();
        System.out.println("A idade do Ninja é: " + idadeDoNinja);

//      Tratamento de dados
        if (idadeDoNinja >= 18){
            System.out.println("Esse ninja já tá velho e pode sair da vila para ser CLT.");
        } else {
            System.out.println("Muito novo meu camarada, vai brincar de bola que você ganhar mais.");
        }

//    Fechar sempre o Scanner
        caixaDeTexto.close();
    }
}