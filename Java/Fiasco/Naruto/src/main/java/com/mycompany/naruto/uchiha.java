/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.naruto;

/**
 *
 * @author joao
 */
public class uchiha extends ninja {
    
    @Override
    public void ataqueBase(){
        System.out.println("Eu sou um ninja e taquei uma kunai de tipo FOGO");
    }
    
    
    public void ataqueBase(int nivelDeChacra){
        if (nivelDeChacra > 2){
            System.out.println("Susano ativado");
        } else if (nivelDeChacra == 2){
            System.out.println("Eu só consegui ativar o Sharingan");
        }
        else {
            System.out.println("Eu to sem Chacra");
        }
    }
}
