package Fiasco.Java10x.src.NivelBasico.Condicoes;

public class Ternarios {
    public static void main(String[] args) {
        /*
        Ternarios: São maneiras de reduzir o código.
        variavel = (condição) ? valorSeVerdadeiro : valorSeFalso;
         */

        short numeroDeMissoes = 1;

        String nivel = (numeroDeMissoes >= 10) ? "Este ninja está com mais de 10 missões" : "Esse ninja tem menos de 10 missões";
        System.out.println(nivel);
    }
}
