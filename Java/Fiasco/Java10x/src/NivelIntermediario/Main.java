package Java10x.src.NivelIntermediario;

public class Main {
    public static void main(String[] args) {
//        Criar o ninja naruto (Objeto 1)
        Uzumaki Naruto = new Uzumaki();

        Naruto.nome = "Naruto Uzumaki";
        Naruto.idade = 17;
        Naruto.aldeia = "Aldeia da Folha";
        Naruto.ModoSabioAtivado();
        Naruto.habilidadeEspecial();

//        Criar ninja Sasuke (Objeto 2)
        Uchiha Sasuke = new Uchiha();

        Sasuke.nome = "Sasuke Uchiha";
        Sasuke.idade = 18;
        Sasuke.aldeia = "Aldeia da Folha";
        Sasuke.habilidadeEspecial();

//        Aplicando métodos ao meu objeto
        Sasuke.SharinganAtivado(); // Método tipo void
        String chamandoMetodo = Sasuke.EuSouUmNinja(); // Método tipo string
        System.out.println(chamandoMetodo);

        int quantoTempoFalta = Sasuke.anosParaSeTornarHokage(70);
        System.out.println("Você tem " + Sasuke.idade + ", entao falta no minimo " + quantoTempoFalta + " anos para se tornar Hokage");

//        Criar a Sakura (Objeto 3)
        Haruno Sakura = new Haruno();

        Sakura.nome = "Sakura Haruno";
        Sakura.idade = 18;
        Sakura.aldeia = "Aldeia da Folha";
        Sakura.AtivarCura();

//        Criar a Hinata (Objeto 4)
        Hyuga Hinata = new Hyuga();
        Hinata.nome = "Hinata Hyuga";
        Hinata.aldeia = "Aldeia da Folha";
        Hinata.idade = 16;
        Hinata.ByakuganAtivado();

//        Criar o Boruto (Objeto 5) - Estudos de interfaces e Polimorfismo
        Boruto Boruto = new Boruto();
        Boruto.nome = "Boruto Hyuga Uzumaki";
        Boruto.aldeia = "Aldeia da Folha";
        Boruto.idade = 9;

        Boruto.ModoSabioAtivado();
        Boruto.AtivarOKarma();
        Boruto.AtivarJougan();

        // Estudo de Construtores
        Hokages Hashirama = new Hokages();
        Hashirama.idade = 45;

        Hokages Tobirama = new Hokages("Tobirama Senju");
        System.out.println(Tobirama.nome);

        Hokages Hiruzen = new Hokages(40);
        System.out.println(Hiruzen.idade);

        Hokages Hinato = new Hokages("Minato Namikaze", 32, false);
        System.out.println("Nome: " + Hinato.nome + " Idade: " + Hinato.idade + " Vivo: " + Hinato.vivoOuNao);
    }
}
