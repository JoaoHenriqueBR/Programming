package Java10x.src.NivelIntermediario;

public class Hokages {
    String nome;
    int idade;
    boolean vivoOuNao;
    String aldeia;
    int missoes;
    double saldoBancario;
    double altura;

    // NoArgs Constructor
    public Hokages(){
        // Construtor vazio, sem argumentos
    }

    // Criar um construtor com argumento
    public Hokages(String nome){
        this.nome = nome;
    }

    public Hokages(int idade){
        this.idade = idade;
    }

    // All Args Constructor = Construtor com todos os argumentos
    public Hokages(String nome, int idade, boolean vivoOuNao){
        this.nome = nome;
        this.idade = idade;
        this.vivoOuNao = vivoOuNao;
    }

    // Você consegue criar automaticamente os construtores com o IntelliJ (Atalho Generate...)
    public Hokages(String nome, int idade, boolean vivoOuNao, String aldeia, int missoes, double saldoBancario, double altura) {
        this.nome = nome;
        this.idade = idade;
        this.vivoOuNao = vivoOuNao;
        this.aldeia = aldeia;
        this.missoes = missoes;
        this.saldoBancario = saldoBancario;
        this.altura = altura;
    }
}
