package Asiento;

public class Bronce extends Asiento{

    public Bronce(String ID , char tipo) {
        super(ID, tipo);
    }

    @Override
    public String imprimirMenuPantalla() {
        return "BRONCE";
    }
    
    
}