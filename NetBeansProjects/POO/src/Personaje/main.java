package Personaje;

public class main {

    public static void main(String[] args) {
        Jugador j = new Jugador("Explorador", 'f', -1, -1, 130);
        Enemigo e = new Enemigo("Bitter", 'f', 0, 0, 80);
        
        j.golpear(e);
        j.golpear(e);
        j.moverDerecha(10);
        j.moverAbajo(5);
        
        e.golpear(j);
        e.golpear(j);
        j.recogerBotiquin();
        
        j.usarBotiquin();
        j.usarBotiquin();
        j.golpear(e);
        j.golpear(e);
        j.golpear(e);

        e.golpear(j);
        e.golpear(j);
        
        j.golpear(e);
        j.golpear(e);
        
        j.golpear(e);
        j.golpear(e);
        j.golpear(e);
        
        System.out.println(j);
        System.out.println(e);
    }
}