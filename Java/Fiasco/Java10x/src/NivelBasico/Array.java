package Java10x.src.NivelBasico;

import java.util.Arrays;

public class Array {
    public static void main(String[] args) {
        // Arrays são tipo referencia!
        String[] ninja = new String[6];
        ninja[0] = "Naruto Uzumaki";
        ninja[1] = "Sasuke Uchiha";
        ninja[2] = "Sakura Haruno";
        ninja[3] = "Hinata Hyuga";
        ninja[4] = "Kakashi Hatake";

        System.out.println(ninja); // Mostra o espaço na memória do Array (tipo@Espaço -> LJava.lang.String;@xxxxxx)
        System.out.println(ninja[5]); // Posso reservar um espaço vazia no meu Array (mostra null)
        System.out.println(Arrays.toString(ninja));

        // Array idade (int)
        int[] idade = new int[2];
        idade[0] = 16;
        System.out.println(idade); // Mostra o tipo@Espaço na memória do Array -> I@xxxxx
        System.out.println(idade[1]); // Espaço vazio como Int é 0, mostra 0 invés de null.

        // Array vF (boolean)
        boolean[] vF = new boolean[1];
        System.out.println(vF[0]); // Espaço vazio como Boolean é tratado como False.

        // Array flutuante (double ou float)
        double[] flutuante = new double[1];
        System.out.println(flutuante[0]); // Espaço vazio como Float é 0.0

        String nomeDoNinja1 = "Gaara"; // Espaço na memória só para o Gaara
        String nomeDoNinja2 = "Rock Lee"; // Espaço na memória só para o Rock Lee
        // Consome mais memória e é menos prático

        /*
        String ninja1 = "Naruto Uzumaki";
        String ninja2 = "Sasuke Uchiha";
        String ninja3 = "Sakura Haruno";
        System.out.println(ninja1);
        System.out.println(ninja2);
        System.out.println(ninja3);
         */
    }
}
