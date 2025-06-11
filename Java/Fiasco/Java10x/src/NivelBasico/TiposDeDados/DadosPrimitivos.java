package Fiasco.Java10x.src.NivelBasico.Condicoes.TiposDeDados;

public class DadosPrimitivos {
    public static void main(String[] args) {
        /*
        * Dados primitivos - int, double, float, char, boolean, short.
        * Objetivos da aula: Criar um ninja - Naruto -
        * */

        int idade = 16; // Valor máximo: 2 147 483 647
        double altura = 1.65;
        char inicial = 'N';
        boolean vivo = true;
        Long saldoBancario = 201472839281L; // Valor máximo: 9,223,372,036,854,775,807

        System.out.println(idade); // Comando para mostrar para o usuário
        System.out.println(saldoBancario);
        System.out.println(altura);
        System.out.println("saldoBancario é = " + saldoBancario);
        System.out.println("Minha idade é = " + idade);
    }
}
