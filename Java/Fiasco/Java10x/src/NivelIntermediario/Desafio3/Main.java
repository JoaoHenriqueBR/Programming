package Java10x.src.NivelIntermediario.Desafio3;

import java.util.Scanner;

public class Main {
    static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int i = 1;
        int c = -1;

        Uchiha[] ninjas = new Uchiha[5];

        while (i > 0){
            System.out.println("CRIADOR DE NINJAS UCHIHAS");
            System.out.println("1 - Exibir todos os ninjas");
            System.out.println("2 - Adicionar novos ninjas [max: 5]");
            System.out.println("3 - Atualizar habilidades especiais");
            System.out.println();
            System.out.println("0 - Sair do programa");

            System.out.println("Escolha uma opção: ");
            i = input.nextInt();
            input.nextLine();

            switch (i){
                case 1:
                    if (c >= 0) {
                        System.out.println("Ninjas: ");
                        for (int j = 0; j <= c; j++) {
                            ninjas[j].mostrarInformacoes();
                            ninjas[j].mostrarHabilidadeEspecial();
                        }
                    } else {
                        System.out.println("Adicione mais ninjas");
                    }

                    break;
                case 2:
                    if (c >= 4) {
                        System.out.println("Número máximo de ninjas atingido");
                        break;
                    } else {
                        Uchiha ninja = new Uchiha();
                        System.out.println("Nome do ninja: ");
                        ninja.nome = input.nextLine();

                        System.out.println("Idade do ninja: ");
                        ninja.idade = input.nextInt();
                        input.nextLine();


                        System.out.println("Missão do ninja: ");
                        ninja.missao = input.nextLine();

                        System.out.println("Nivel de Dificuldade: ");
                        ninja.nivelDificuldade = input.nextLine();

                        System.out.println("Status da missão: ");
                        ninja.statusMissao = input.nextLine();

                        System.out.println("Habilidade Especial: ");
                        ninja.habilidadeEspecial = input.nextLine();

                        System.out.println("Ninja criado com sucesso.");
                        c = c + 1;
                        ninjas[c] = ninja;
                        break;
                    }
                case 3:
                    System.out.println("Alterar habilidade especial do " + ninjas[c].nome + " para: ");
                    ninjas[c].habilidadeEspecial = input.nextLine();

                    System.out.println("Habilidade alterada com sucesso!");
                    ninjas[c].mostrarHabilidadeEspecial();
                    break;
                case 0:
                    System.out.println("Saindo do sistema...");
                    input.close();
                    break;
                default:
                    System.out.println("Valor inválido! Tente novamente.");
                    break;
            }

        }
    }

}
