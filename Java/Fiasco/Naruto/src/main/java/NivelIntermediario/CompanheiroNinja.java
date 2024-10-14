package NivelIntermediario;

public class CompanheiroNinja {
    private String nomeDoAnimal;

    public CompanheiroNinja(String nomeDoAnimal) {
        this.nomeDoAnimal = nomeDoAnimal;
    }

    @Override
    public String toString() {
        return "Esse é meu companheiro: " + nomeDoAnimal;
    }
}
