/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.naruto;

/**
 *
 * @author joao
 */
public class Main {

    public static void main(String[] args) {
        
        // obj 1
        uzumaki naruto = new uzumaki();
        naruto.setNome("Naruto Uzumaki");
        System.out.print("Meu nome é " + naruto.getNome());
        naruto.setIdade(16);
        System.out.println(" e tenho " + naruto.getIdade() + " anos!");
        naruto.setAldeia("Aldeia Oculta da Folha");
        System.out.println("Venho da "+ naruto.getAldeia());
        naruto.temBiju = true;
        naruto.ataqueBase();

        
        // obj 2
        uchiha sasuke = new uchiha();
        sasuke.setNome("Sasuke Uchiha");
        System.out.println("\nMeu nome é " + sasuke.getNome());
        sasuke.ataqueBase();
        sasuke.ataqueBase(3);
    }
}
