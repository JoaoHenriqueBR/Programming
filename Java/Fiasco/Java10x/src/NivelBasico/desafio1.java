package Fiasco.Java10x.src.NivelBasico;

public class desafio1 {
    public static void main(String[] args) {
        // Criar Ninja 1
        String nomeNinja1 = "Naruto Uzumaki";
        int idadeNinja1 = 11;
        String missaoNinja1 = "Capturar um ninja";
        char dificuldadeMissaoNinja1 = 'B';
        String statusMissaoNinja1;

        // Criar Ninja 2
        String nomeNinja2 = "Sasuke Uchiha";
        int idadeNinja2 = 12;
        String missaoNinja2 = "Espionar a Vila";
        char dificuldadeMissaoNinja2 = 'C';
        String statusMissaoNinja2;

        // Criar Ninja 3
        String nomeNinja3 = "Rock Lee";
        int idadeNinja3 = 15;
        String missaoNinja3 = "Vencer o Gaara";
        char dificuldadeMissaoNinja3 = 'S';
        String statusMissaoNinja3;


        // Saída: Dados do Ninja 1
        System.out.println("----- Ninja 1 -----");
        System.out.println("Nome: " + nomeNinja1);
        System.out.println("Idade: " + idadeNinja1);
        System.out.println("Missão: " + missaoNinja1);
        System.out.println("Nivel: " + dificuldadeMissaoNinja1);

        // Verificar Dificuldade da Missão com a idade do Ninja
        if (idadeNinja1 < 15) {
            if (dificuldadeMissaoNinja1 == 'C' || dificuldadeMissaoNinja1 == 'D'){
                statusMissaoNinja1 = "Concluída";
            } else {
                statusMissaoNinja1 = "Não Concluída";
            }
        } else {
            statusMissaoNinja1 = "Concluída";
        }

        System.out.println("Status: " + statusMissaoNinja1);


        // Saída: Dados do Ninja 2
        System.out.println("\n----- Ninja 2 -----");
        System.out.println("Nome: " + nomeNinja2);
        System.out.println("Idade: " + idadeNinja2);
        System.out.println("Missão: " + missaoNinja2);
        System.out.println("Nivel: " + dificuldadeMissaoNinja2);

        // Verificar Dificuldade da Missão com a idade do Ninja
        if (idadeNinja2 < 15) {
            if (dificuldadeMissaoNinja2 == 'C' || dificuldadeMissaoNinja2 == 'D'){
                statusMissaoNinja2 = "Concluída";
            } else {
                statusMissaoNinja2 = "Não Concluída";
            }
        } else {
            statusMissaoNinja2 = "Concluída";
        }

        System.out.println("Status: " + statusMissaoNinja2);


        // Saída: Dados do Ninja 3
        System.out.println("\n----- Ninja 3 -----");
        System.out.println("Nome: " + nomeNinja3);
        System.out.println("Idade: " + idadeNinja3);
        System.out.println("Missão: " + missaoNinja3);
        System.out.println("Nivel: " + dificuldadeMissaoNinja3);

        // Verificar Dificuldade da Missão com a idade do Ninja
        if (idadeNinja3 < 15) {
            if (dificuldadeMissaoNinja3 == 'C' || dificuldadeMissaoNinja3 == 'D'){
                statusMissaoNinja3 = "Concluída";
            } else {
                statusMissaoNinja3 = "Não Concluída";
            }
        } else {
            statusMissaoNinja3 = "Concluída";
        }

        System.out.println("Status: " + statusMissaoNinja3);
    }
}
