/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.naruto;

/**
 *
 * @author joao
 */
public class ninja {
    private String nome;
    private String aldeia;
    private int idade;

    public String getAldeia() {
        return aldeia;
    }

    public void setAldeia(String aldeia) {
        this.aldeia = aldeia;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    // Getter - Criar Getter para mostrar pro usuário
    public String getNome(){
        return nome;
    }
    
    // Setter - Settar o valor da variável
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public void ataqueBase(){
        System.out.print("Eu sou um ninja e taquei uma kunai.");
    }
}
