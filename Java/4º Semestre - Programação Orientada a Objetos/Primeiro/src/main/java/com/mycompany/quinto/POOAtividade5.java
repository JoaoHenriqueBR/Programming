/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package com.mycompany.quinto;

import javax.swing.JOptionPane;

public class POOAtividade5 {

    public static void main(String[] args) {
        
        boolean boot = true;
        
        // Exercício 1:
        
        /*
        while (boot) {
            try {
                String input = JOptionPane.showInputDialog("Área de um Triângulo!\n\nDigite a base(cm): ");
                float varBase = Float.parseFloat(input);

                if (varBase <= 0) {
                    throw new Exception("valor_invalido");
                }

                input = JOptionPane.showInputDialog("Área de um Triângulo!\n\nDigite a altura(cm): ");
                float varAltura = Float.parseFloat(input);
                
                if (varAltura <= 0) {
                    throw new Exception("valor_invalido");
                }

                Triangulo exercicio = new Triangulo();

                exercicio.setDados(varBase, varAltura);

                JOptionPane.showMessageDialog(null, "A área do Triângulo é: " + exercicio.calcArea() + " cm^2");
                
                boot = false;
            }
            catch(NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "ERRO: Digite um valor válido!");
            }

            catch(Exception valor_invalido) {
                JOptionPane.showMessageDialog(null, "ERRO: Digite um valor acima de 0!");
            }
        }
        */
        
        // Exercício 2:
        while (boot) {
            try {
                String input = JOptionPane.showInputDialog("Equação de Segundo Grau!\n\nDigite o valor A: ");
                float A = Float.parseFloat(input);
                
                input = JOptionPane.showInputDialog("Equação de Segundo Grau!\n\nDigite o valor B: ");
                float B = Float.parseFloat(input);
                
                input = JOptionPane.showInputDialog("Equação de Segundo Grau!\n\nDigite o valor C: ");
                float C = Float.parseFloat(input);
                
                Equacao exercicio = new Equacao();
                
                exercicio.SetDados(A, B, C);
                
                exercicio.calcRaizes();
            }
            
            catch(NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "ERRO: Digite um valor válido!");
            }
        }
        
    }
    
}
