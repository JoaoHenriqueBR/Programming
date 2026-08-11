package Java10x.src.NivelIntermediario.Desafio3;

public class Ninja {
    String nome;
    int idade;
    String missao;
    String nivelDificuldade;
    String statusMissao;

    public void mostrarInformacoes(){
        System.out.println("Eu sou " + nome + ", Tenho " + idade + " anos e minha missão é " + missao + ". É uma missão " + nivelDificuldade + ". Que está " + statusMissao);
    }
}
