package Java10x.src.NivelIntermediario;

public class Boruto extends Uzumaki implements HyugaUzumaki {
    // Toda vez que implementa uma interface, você >DEVE< usar o que está dentro dela

    @Override
    public void AtivarOKarma() {
        System.out.println("O Karma foi ativado! Eu sou um Hyuga Uzumaki!");
    }

    @Override
    public void AtivarJougan() {
        System.out.println("Jougan Ativado! Eu sou um Hyuga Uzumaki!");
    }
}
