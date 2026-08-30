package Java10x.src.NivelIntermediario;

public class Uzumaki extends Ninja {
    public void ModoSabioAtivado() {
        System.out.println("Meu nome é " + nome + ". Modo Sábio Ativado!");
    }

    @Override
    public void habilidadeEspecial() {
        System.out.println("Meu nome é " + nome + " e esse é meu ataque Uzumaki, um ataque de ar");
    }
}
