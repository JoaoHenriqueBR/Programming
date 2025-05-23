package TiposDeDados;

import java.util.Locale;

public class DadosNaoPrimitivos {
    public static void main(String[] args) {
//        Tudo que for digitado aqui dentro com o comando PSVM vai ser compilado pelo Java.

        /*
        * Dados nao primitivos: String, Array, Class, enum
        * Objetivo: Criar um ninja, e atribuir métodos a ele.
        * */

        String nome = "Naruto Uzumaki";
        String nomeUpperCase = nome.toUpperCase(); // ToUpperCase vai colocar tudo em CAPSLOCK

        System.out.println("Esse texto está em CAPS LOCK: " + nomeUpperCase);
        System.out.println("Esse texto está normal: " + nome);

        String aldeia = "Aldeia da Folha";
        String aldeiaLowerCase = aldeia.toLowerCase(); // ToLowerCase vai colocar tudo em caixa baixa/minuscula
        System.out.println("Esse texto está em minusculo: " + aldeiaLowerCase);

    }
}
