package segundo.bimestre.oitavo;

/*
EX1:
    Crie uma classe chamada Faturar que possa ser utilizada por uma de suprimentos de informática para representar uma fatura de um item vendido na loja.
    Uma fatura deve incluir as seguintes informações como atributos:
     - O número do item faturado (id),
     - a descrição do item (descricao),
     - a quatidade comprada do item (quantidade) e
     - o preço unitário do item (preco).
    Sua classe deve ter um método construtor que inicialize os quatro atributos.
    Forneça um método set e um método get para cada variável de instância.
    Além disso, forneça um método chamado getFaturarTotal que calcula o valor da fatura
                              (Isso é, multiplica a quantidade pelo preço por item) e depois retorna o valor como double.
    Escreva um aplicativo de teste que demonstra as capacidades da classe Faturar. (Main > Case 0)
 */

public class Faturar {
    private int id, quantidade;
    private String descricao;
    private double preco;

    //Construtor
    public Faturar(int id, String descricao, int quantidade, double preco) {
        this.id = id;
        this.descricao = descricao;
        this.quantidade = quantidade;
        this.preco = preco;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public double getFaturarTotal(int quantidade, double preco) {
        return quantidade * preco;
    }
}
