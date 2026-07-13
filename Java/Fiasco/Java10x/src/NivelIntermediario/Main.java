package Java10x.src.NivelIntermediario;

public class Main {
    public static void main(String[] args) {
//        Criar o ninja naruto (Objeto)
        Ninja Naruto = new Ninja();

        Naruto.nome = "Naruto Uzumaki";
        Naruto.idade = 17;
        Naruto.aldeia = "Aldeia da Folha";

//        Criar ninja Sasuke (Objeto)
        Ninja Sasuke = new Ninja();

        Sasuke.nome = "Sasuke Uchiha";
        Sasuke.idade = 18;
        Sasuke.aldeia = "Aldeia da Folha";

//        Aplicando métodos ao meu objeto
        Sasuke.SharinganAtivado(); // Método tipo void
        String chamandoMetodo = Sasuke.EuSouUmNinja(); // Método tipo string
        System.out.println(chamandoMetodo);

        int quantoTempoFalta = Sasuke.anosParaSeTornarHokage(70);
        System.out.println("Você tem " + Sasuke.idade + ", entao falta no minimo " + quantoTempoFalta + " anos para se tornar Hokage");

//        Criar a Sakura
        Ninja Sakura = new Ninja();

        Sakura.nome = "Sakura Haruno";
        Sakura.idade = 18;
        Sakura.aldeia = "Aldeia da Folha";
    }
}
