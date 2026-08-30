package Java10x.src.NivelIntermediario.Desafio4;

public class Main {
    public static void main(String[] args) {
        NinjaAvancado Sasuke = new NinjaAvancado("Fogo");
        Sasuke.nome = "Sasuke Uchiha";
        Sasuke.idade = 18;
        Sasuke.habilidade = TipoHabilidade.RINNENGAN;
        Sasuke.mostrarInformacoes();
        Sasuke.executarHabilidade();

        NinjaBasico Rikudou = new NinjaBasico("Rikudou Sennin", 40, TipoHabilidade.NINJUTSU);
        Rikudou.mostrarInformacoes();
        Rikudou.executarHabilidade();
    }
}
