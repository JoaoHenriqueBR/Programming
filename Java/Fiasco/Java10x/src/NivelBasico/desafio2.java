package Fiasco.Java10x.src.NivelBasico;

import java.util.Scanner;

public class desafio2 {
    public static void main(String[] args) {
//        Contadores
        int opcao = 0;
        int c = 0;
        int max = 5;

//        Iniciar o Scanner
        Scanner entrada = new Scanner(System.in);

//        Iniciar o Array
        String[] ninjas = new String[max];


//        Loop do Menu
        while (opcao != 3){
            System.out.println("\n===== Menu Ninja =====");
            System.out.println("1. Cadastrar Ninja");
            System.out.println("2. Listar Ninjas");
            System.out.println("3. Sair");
            System.out.print("Escolha uma opção: ");

            opcao = entrada.nextInt();
            entrada.nextLine(); // Corrige a quebra de linha que fica no buffer

            switch (opcao) {
                case 1:
                    if (c == max){
                        System.out.println("Limite alcançado, sem vagas para novos ninjas!");
                    } else {
                        System.out.println("Digite o nome do ninja: ");
                        ninjas[c] = entrada.nextLine();
                        System.out.println("Ninja " + ninjas[c] + " cadastrado.");
                        c++;
                    }
                    break;
                case 2:
                    if (c == 0){
                        System.out.println("Nenhum ninja encontrado.");
                    } else {
                        System.out.println("===== Ninjas da Vila da Folha =====");
                        for (int i = 0; i < c; i++) {
                            System.out.println(ninjas[i]);
                        }
                    }
                    break;
                case 3:
                    System.out.println("Saindo do sistema...");
                    break;
                default:
                    System.out.println("Opção inválida! Tente novamente.");
                    break;
            }

        }

        entrada.close();




    }
}
