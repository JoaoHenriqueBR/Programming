package NivelIntermediario;

import java.util.ArrayList;
import java.util.List;

public class BolsaNinja<T> {
    // Inicializar o Array
    private List<T> ferramentas;

    // Construtor
    public BolsaNinja(){
        this.ferramentas = new ArrayList<>();
    }

    // Colocar Ferramentas no nosso Array
    public void adicionarFerramenta (T ferramenta) {
        ferramentas.add(ferramenta);
    }

    // Mostrar a nossa lista de ferramentas
    public void mostrarFerramenta(){
        for (T ferramenta : ferramentas) {
            System.out.println(ferramenta);
        }
    }
}
