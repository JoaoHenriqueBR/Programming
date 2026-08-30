package Java10x.src.NivelIntermediario;

public class Uchiha extends Ninja {


    /*
     * Método >VOID< não retorna valor nenhum!
     * */
    public void SharinganAtivado(){
        System.out.println("Meu nome é " + nome + ". Sharingan Ativado!");
    }


    @Override
    public void habilidadeEspecial(){
        System.out.println("Meu nome é " + nome + " e esse é meu ataque Uchiha, um ataque de fogo");
    }
}
