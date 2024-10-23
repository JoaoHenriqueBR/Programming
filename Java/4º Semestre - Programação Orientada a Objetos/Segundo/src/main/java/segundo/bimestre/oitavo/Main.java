package segundo.bimestre.oitavo;

import javax.swing.JOptionPane;

public class Main {
    public static void main(String[] args) {
        String[] opcoes = {"1 - Faturar", "2 - Empregado", "3 - Calculadora", "4 - Data",  "Sair"};
        int escolha;
        // Inicializa o id (Caso 0)
        int id = 0;

        do {
            escolha = JOptionPane.showOptionDialog(null,
                    "Escolha uma opção:",
                    "Tarefa 08",
                    JOptionPane.DEFAULT_OPTION,
                    JOptionPane.QUESTION_MESSAGE,
                    null,
                    opcoes,
                    opcoes[0]);

            switch (escolha) {
                case 0:
                    // Incrementa o id (+1 para cada novo item)
                    id = id + 1;

                    String descricao = JOptionPane.showInputDialog("Descrição do item: ");
                    int quantidade = Integer.parseInt(JOptionPane.showInputDialog(null, "Quantidade comprada: "));
                    double preco = Double.parseDouble(JOptionPane.showInputDialog(null, "Preço: "));

                    Faturar faturar = new Faturar(id, descricao, quantidade, preco);

                    JOptionPane.showMessageDialog(null, "Id: " + faturar.getId() +
                                                                                "\nDescrição: " + faturar.getDescricao() +
                                                                                "\nQuantidade: " + faturar.getQuantidade() + " Items." +
                                                                                "\nPreço unitário: R$ " + faturar.getPreco() +
                                                                                "\n\nPreço Total: R$ " + faturar.getFaturarTotal(faturar.getQuantidade(), faturar.getPreco()));
                    break;
                case 1:
                    // Valores vazios (Para inicializar as instâncias)
                    String nome = "", sobrenome = "";
                    double salario = 0;

                    // Instância 1 da classe Empregado
                    Empregado empregado1 = new Empregado(nome, sobrenome, salario);
                    empregado1.setNome(JOptionPane.showInputDialog(null, "Nome do Primeiro Empregado: ", "Primeiro", JOptionPane.QUESTION_MESSAGE));
                    empregado1.setSobrenome(JOptionPane.showInputDialog(null, "Sobrenome: ", "Primeiro", JOptionPane.QUESTION_MESSAGE));
                    try{
                        empregado1.setSalario(Double.parseDouble(JOptionPane.showInputDialog(null, "Salário: ", "Primeiro", JOptionPane.QUESTION_MESSAGE)));
                    } catch (NumberFormatException e) {
                        JOptionPane.showMessageDialog(null, "Sem valor definido. ", "AVISO", JOptionPane.WARNING_MESSAGE);
                    }

                    // Instância 2 da classe Empregado
                    Empregado empregado2 = new Empregado(nome, sobrenome, salario);
                    empregado2.setNome(JOptionPane.showInputDialog(null, "Nome do Segundo Empregado: ", "Segundo", JOptionPane.QUESTION_MESSAGE));
                    empregado2.setSobrenome(JOptionPane.showInputDialog(null, "Sobrenome: ", "Segundo", JOptionPane.QUESTION_MESSAGE));
                    try{
                        empregado2.setSalario(Double.parseDouble(JOptionPane.showInputDialog(null, "Salário: ", "Segundo", JOptionPane.QUESTION_MESSAGE)));
                    } catch (NumberFormatException e) {
                        JOptionPane.showMessageDialog(null, "Sem valor definido. ", "AVISO", JOptionPane.WARNING_MESSAGE);
                    }

                    JOptionPane.showMessageDialog(null, "Salário Anual do " + empregado1.getNome() + " " + empregado1.getSobrenome() + ": R$ " + empregado1.getSalario() * 12 +
                            "\nSálario Anual do " + empregado2.getNome() + " " + empregado2.getSobrenome() + ": R$ " + empregado2.getSalario() * 12);

                    //Aumento de 10%
                    empregado1.setSalario(empregado1.getSalario() + (empregado1.getSalario() * 0.1));
                    empregado2.setSalario(empregado2.getSalario() + (empregado2.getSalario() * 0.1));

                    JOptionPane.showMessageDialog(null, "Novo Salário Anual do " + empregado1.getNome() + " " + empregado1.getSobrenome() + ": R$ " + empregado1.getSalario() * 12 +
                            "\nNovo Sálario Anual do " + empregado2.getNome() + " " + empregado2.getSobrenome() + ": R$ " + empregado2.getSalario() * 12);

                    break;
                case 2:
                    double x = Double.parseDouble(JOptionPane.showInputDialog(null, "Digite o primeiro número: "));
                    double y = Double.parseDouble(JOptionPane.showInputDialog(null,"Digite o segundo número: "));
                    char operador = JOptionPane.showInputDialog(null, "Digite o operador (+, -, *, /): ").charAt(0);

                    Calculadora calc = new Calculadora(x, y, operador);
                    calc.imprimirResultado();
                    break;
                case 3:
                    // Insere a Data
                    int dia = Integer.parseInt(JOptionPane.showInputDialog(null, "Dia: "));
                    int mes = Integer.parseInt(JOptionPane.showInputDialog(null, "Mês: "));
                    int ano = (Integer.parseInt(JOptionPane.showInputDialog(null, "Ano: ")));

                    // Nova Instância
                    Data data = new Data(dia, mes, ano);

                    // Exibe a Data
                    JOptionPane.showMessageDialog(null, "Data: " + data.displayData());

                    // Altera a Data
                    data.setDia(Integer.parseInt(JOptionPane.showInputDialog(null, "Novo dia: ")));
                    data.setMes(Integer.parseInt(JOptionPane.showInputDialog(null, "Novo mês: ")));
                    data.setAno(Integer.parseInt(JOptionPane.showInputDialog(null, "Novo ano: ")));

                    // Exibe a nova Data
                    JOptionPane.showMessageDialog(null, "Nova Data: " + data.displayData());
                    break;
                case 4:
                    JOptionPane.showMessageDialog(null, "Saindo...");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Escolha inválida!", "Erro", JOptionPane.ERROR_MESSAGE);
            }
        } while (escolha != 4);
    }
}
