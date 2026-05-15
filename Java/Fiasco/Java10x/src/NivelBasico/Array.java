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

        System.out.println("-------------");
        System.out.println(ninja); // Mostra o espaço na memória do Array (tipo@Espaço -> LJava.lang.String;@xxxxxx)
        System.out.println(ninja[5]); // Posso reservar um espaço vazia no meu Array (mostra null)
        System.out.println(Arrays.toString(ninja));
        System.out.println("-------------");


        // Redeclarar o ARRAY
        // Deleta o Array antigo pelo Garbage Collector (GC) e o sobrepõe por outro
        ninja = new String[7];
        System.out.println(ninja); // Mostra o novo espaço na memória
        System.out.println(ninja[0]); // Mostra Null porque o Array antigo foi removido pelo GC
        ninja[0] = "Hashirama Senju";
        ninja[1] = "Tobirama Senju";
        ninja[2] = "Hiruzen Sarutobi";
        ninja[3] = "Minato Namikaze";
        ninja[4] = "Tsunade";
        ninja[5] = "Kakashi Hatake";
        ninja[6] = "Naruto Uzumaki";
        System.out.println(ninja[2]); // Mostra o ninja hokage especifico do novo array
        System.out.println("-------------");

        // For para fazer um LOOP no array
        for (int i = 0; i < 7; i++) {
            System.out.println(ninja[i]);
        }
        System.out.println("-------------");


        // Array idade (int)
        int[] idade = new int[2];
        idade[0] = 16;
        System.out.println(idade); // Mostra o tipo@Espaço na memória do Array -> I@xxxxx
        System.out.println(idade[1]); // Espaço vazio como Int é 0, mostra 0 invés de null.
        System.out.println("-------------");

        // Array vF (boolean)
        boolean[] vF = new boolean[1];
        System.out.println(vF[0]); // Espaço vazio como Boolean é tratado como False.
        System.out.println("-------------");

        // Array flutuante (double ou float)
        double[] flutuante = new double[1];
        System.out.println(flutuante[0]); // Espaço vazio como Float é 0.0
        System.out.println("-------------");

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

        /*
        Arrays multidimensionais (Arrays 2D)

        - Arrays dentro de Arrays
        - Funciona como uma matriz, com linhas e colunas.
        */

        String[][] ninjasEAldeias = new String[3][3];

//        Linha 1
        ninjasEAldeias[0][0] = "Konaha"; // Coluna 1
        ninjasEAldeias[0][1] = "Naruto Uzumaki"; // Coluna 2
        ninjasEAldeias[0][2] = "Sasuke Uchiha"; // Coluna 3

//        Linha 2
        ninjasEAldeias[1][0] = "Nevoa"; // Coluna 1
        ninjasEAldeias[1][1] = "Zabuza"; // Coluna 2
        ninjasEAldeias[1][2] = "Haku"; // Coluna 3

//        Linha 3
        ninjasEAldeias[2][0] = "Deserto"; // Coluna 1
        ninjasEAldeias[2][1] = "Gaara"; // Coluna 2
        ninjasEAldeias[2][2] = "Temari"; // Coluna 3

//        Iterando sobre o Array
        for (int i = 0; i < ninjasEAldeias.length; i++) {
            System.out.println("Aldeia: " + ninjasEAldeias[i][0]);
            for (int j = 1; j < ninjasEAldeias[i].length; j++) {
                System.out.println("Ninja: " + ninjasEAldeias[i][j]);
            }
        }
    }
}
