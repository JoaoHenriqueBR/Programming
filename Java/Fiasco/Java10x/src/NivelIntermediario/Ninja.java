package Java10x.src.NivelIntermediario;

public class Ninja {
    String nome;
    String aldeia;
    int idade;

    // Criar um método público personalizável

    /*
    * Método >VOID< não retorna valor nenhum!
    * */
    public void SharinganAtivado(){
        System.out.println("Sharingan Ativado!");
    }

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
