package Java10x.src.NivelIntermediario.Desafio4;

public class NinjaBasico implements Ninja {
    String nome;
    int idade;
    TipoHabilidade habilidade;

    public NinjaBasico() {
    }

    public NinjaBasico(String nome, int idade, TipoHabilidade habilidade) {
        this.nome = nome;
        this.idade = idade;
        this.habilidade = habilidade;
    }

    @Override
    public void mostrarInformacoes() {
        System.out.println("Nome: " + nome + "| idade: " + idade + "| habilidade: " + habilidade);
    }

    @Override
    public void executarHabilidade() {
        System.out.println("Eu sou o " + nome + ". Ativei o " + habilidade);
    }
}
