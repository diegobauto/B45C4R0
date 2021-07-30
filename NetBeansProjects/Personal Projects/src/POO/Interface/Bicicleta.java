package POO.Interface;

public class Bicicleta implements Rueda{

    @Override
    public void avanzar() {
        System.out.println("La biclicleta esta avanzando");
    }

    @Override
    public void frenar() {
        System.out.println("La biclicleta esta frenando");
    }
    
}