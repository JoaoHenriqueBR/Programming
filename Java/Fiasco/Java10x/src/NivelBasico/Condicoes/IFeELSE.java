package Fiasco.Java10x.src.NivelBasico.Condicoes;

public class IFeELSE {
    public static void main(String[] args) {

        /*
        * IF e ELSE - Condições
        * else if
        * Objetivo: Passar o ninja de nível de acordo com o número de missões.
        * */

        // Ninja Naruto
        String nome = "Naruto Uzumaki";
        int idade = 10;
        boolean hokage = false;
        short numeroDeMissoes = 14;

        String rank; // Inicia uma variável sem valor

        // se (condição) {faça isso}
        if (numeroDeMissoes < 10){
            rank = "Gennim";
        } else if (numeroDeMissoes >= 20) {
            rank = "Jounin";
        } else {
            rank = "Chunnin";
        }
        System.out.println("Rank: " + rank);
    }
}
