package Java10x.src.NivelIntermediario;

public class Ninja {
    String nome;
    String aldeia;
    int idade;

    // Criar um método público personalizável

    /*
    * Método >STRING< vai ter que retornar um string
    * */
    public String EuSouUmNinja(){
        return "Oi, eu sou um ninja";
    }

    /*
    * Método >INT< vai ter que retornar um int
    * */
    public int anosParaSeTornarHokage(int idadeMinimaParaSerHokage) {
        return idadeMinimaParaSerHokage - idade;
    }
}
