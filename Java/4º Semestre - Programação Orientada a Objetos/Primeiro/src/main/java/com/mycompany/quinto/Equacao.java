package com.mycompany.quinto;
import javax.swing.JOptionPane;


public class Equacao {

    float A, B, C;
    
    public void calcRaizes() {
        float delta = (B * B) + (- 4 * A * C);
        JOptionPane.showMessageDialog(null, delta);
        
        JOptionPane.showMessageDialog(null, Math.sqrt(delta));
        
        if (delta == 0) {
            double R1 = ((-B)+ Math.sqrt(delta)) / (2 * A);
            
            double R2 = ((-B)- Math.sqrt(delta)) / (2 * A);
            
            JOptionPane.showMessageDialog(null, "As raízes são iguais!\n\nRaíz 1 = " + R1 + "\nRaíz 2 = " + R2);
            
        } else if (delta > 0 ) {
            double R1 = ((-B)+ Math.sqrt(delta)) / (2 * A);
            double R2 = ((-B) - Math.sqrt(delta))/ (2 * A);
            
            JOptionPane.showMessageDialog(null, "As raízes são diferentes!\n\nRaíz 1 = " + R1 + "\nRaíz 2 = " + R2);
        } else {
            JOptionPane.showMessageDialog(null, "Não há raízes!");
        }
    }
    
    public void SetDados(float varA, float varB, float varC) {
        A = varA;
        B = varB;
        C = varC;
    }
    
    Equacao() {
        A = 0;
        B = 0;
        C = 0;
    }
}
