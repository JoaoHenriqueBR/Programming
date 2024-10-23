package segundo.bimestre.oitavo;

import javax.swing.JOptionPane;

/*
EX3:
    Escreva uma classe em Java que simule uma calculadora bem simples. Essa classe deve ter como atributos duas variáveis double e um char.
    Deve possuir um construtor que recebe como parâmetro dois números e um caracter, correspondente a uma das operações básicas (+, -, *, /).
    Deve ter um método para calcular a operação desejada e um para imprimir o resultado.
    O programa deve considerar divisões por zero como sendo erros, e imprimir uma mensagem adequada. (Main > Case 2)
 */

public class Calculadora {
    private double x;
    private double y;
    private char operador;

    // Construtor
    public Calculadora(double x, double y, char operador) {
        this.x = x;
        this.y = y;
        this.operador = operador;
    }

    // Método para calcular a operação
    public double calcular() {
        switch (operador) {
            case '+':
                return x + y;
            case '-':
                return x - y;
            case '*':
                return x * y;
            case '/':
                if (y == 0) {
                    throw new ArithmeticException("Erro: Divisão por zero.");
                }
                return x / y;
            default:
                throw new IllegalArgumentException("Operador inválido.");
        }
    }

    // Método para imprimir o resultado
    public void imprimirResultado() {
        try {
            double resultado = calcular();
            JOptionPane.showMessageDialog(null, "O resultado de " + x + " " + operador + " " + y + " é: " + resultado);
        } catch (ArithmeticException e) {
            JOptionPane.showMessageDialog(null, e.getMessage());
        } catch (IllegalArgumentException e) {
            JOptionPane.showMessageDialog(null, e.getMessage());
        }
    }
}
