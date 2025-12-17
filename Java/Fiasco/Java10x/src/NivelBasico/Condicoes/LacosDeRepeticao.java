package Fiasco.Java10x.src.NivelBasico.Condicoes;

public class LacosDeRepeticao {
    public static void main(String[] args) {
        /*
        Laços de Repetição: Vão se repetir infinitamente ou até atingir o parâmetro desejado.
        WHILE E FOR
         */

//        While
//        Enquanto a condição for verdadeira, tudo aqui vai se repetir
        int numeroDeClones = 0;
        int numeroMaxClones = 40;

        while (numeroDeClones <= numeroMaxClones){
            numeroDeClones++;
            System.out.println("WHILE: O naruto fez um clone das sombras " + numeroDeClones);
        }

//        FOR
//        Repete uma açõo de forma controlada, já definindo o incremento e a condição.
        for (int i = 0; i <= numeroMaxClones; i++) {
            System.out.println("FOR: O naruta está se clonando e ja se clonou " + i + " vezes.");
        }

    }
}
