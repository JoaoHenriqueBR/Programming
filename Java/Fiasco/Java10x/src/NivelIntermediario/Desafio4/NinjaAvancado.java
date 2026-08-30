package Java10x.src.NivelIntermediario.Desafio4;

public class NinjaAvancado extends NinjaBasico implements Ninja {

    String especialidade;

    public NinjaAvancado() {
    }

    public NinjaAvancado(String especialidade) {
        this.especialidade = especialidade;
    }

    @Override
    public void mostrarInformacoes() {
        System.out.println("Nome: " + nome + "| idade: " + idade + "| habilidade: " + habilidade + "| especialidade: " + especialidade);
    }

    @Override
    public void executarHabilidade() {
        System.out.println("Eu sou o " + nome + ". ativei o " + habilidade + " e minha especialidade é: " + especialidade);
    }
}
