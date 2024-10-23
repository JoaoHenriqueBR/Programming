package segundo.bimestre.oitavo;

/*
EX2:
    A fim de representar empregados em uma firma,
    crie uma classe chamada Empregado que inclui as três informações a seguir como atributos:
     - Um primeiro nome,
     - um sobrenome, e
     - um salário mensal.
     Sua classe deve ter um construtor que inicializa os três atributos.
     Forneça um método set e get para cada atributo.

     Escreva um aplicativo de teste que demonstra as capacidades da classe. (Main > case 1)
      Crie duas instâncias da classe e exiba o salário anual de cada instância.

      Então dê a cada empregado um aumento de 10% e exiba novamente o salário anual de cada empregado.
 */


public class Empregado {
    private String nome, sobrenome;
    private double salario;

    public Empregado(String nome, String sobrenome, double salario) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.salario = salario;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }
}
