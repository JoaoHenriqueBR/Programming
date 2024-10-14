package NivelIntermediario;

public class Main {
    public static void main(String[] args) {
        BolsaNinja<Object> bolsaNinja = new BolsaNinja<>();
        bolsaNinja.adicionarFerramenta(new Kunai("Kunai Explosiva"));
        bolsaNinja.adicionarFerramenta(new Shuriken(3));
        bolsaNinja.adicionarFerramenta(new Pergaminho("Invocação do Sapo"));
        bolsaNinja.adicionarFerramenta(new Pergaminho("Invocação da Águia"));
        bolsaNinja.adicionarFerramenta(new CompanheiroNinja("Mamaru"));

        System.out.println("Itens da nossa bolsa ninja");
        bolsaNinja.mostrarFerramenta();
    }
}
