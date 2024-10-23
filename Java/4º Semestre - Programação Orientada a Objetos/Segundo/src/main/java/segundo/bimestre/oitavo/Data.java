package segundo.bimestre.oitavo;

/*
EX4:
    Crie uma classe em Java chamada Data que inclui três informações como variáveis de instância:
     - mês (int mes),
     - dia (int dia),
     - ano (int ano).
    A classe deve ter métodos get e set para cada variável e um construtor que inicializa as variáveis e assume que os valores fornecidos são corretos.
    Forneça um método displayData que exibe o dia, o mês e o ano separados por barras normais (/).

    Escreva um aplicativo de teste que demonstra as capacidades da classe Data. (Main > Case 3)
 */

public class Data {
    private int mes, dia, ano;

    // Construtor
    public Data(int dia, int mes, int ano) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
    }

    public int getMes() {
        return mes;
    }

    public void setMes(int mes) {
        this.mes = mes;
    }

    public int getDia() {
        return dia;
    }

    public void setDia(int dia) {
        this.dia = dia;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String displayData(){
        return dia + "/" + mes + "/" + ano;
    }
}
