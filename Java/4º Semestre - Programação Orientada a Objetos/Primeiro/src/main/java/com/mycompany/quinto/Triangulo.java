
package com.mycompany.quinto;

public class Triangulo {
    float base;
    float altura;
    
    // Função: Calcular Área do Triângulo
    public float calcArea() {
        
        return (base * altura)/2;
    }
    
    // Leitura da Base e Altura
    public void setDados(float varBase, float varAltura) {
        base = varBase;
        altura = varAltura;
    }
    
    // Constructor Triângulo
    Triangulo() {
        base = 0;
        altura = 0;
    }
}
