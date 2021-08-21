package Personaje;

public class Jugador extends Personaje{
    
    private int numeroBotiquines;

    public Jugador(String nombre, char sexo, double posicionX, double posicionY, double damage) {
        super(nombre, sexo, posicionX, posicionY, damage);
        this.numeroBotiquines = 0;
    }
    
    //METODOS
    public void usarBotiquin(){
        if( numeroBotiquines > 0){
            numeroBotiquines -= 1;
            setVida(getVida()+5);
        }
    }

    public void recogerBotiquin(){
        numeroBotiquines += 1;
    }
    
    public void moverDerecha(double d){
        setPosicionX(getPosicionX()+d);
    }
    
    public void moverIzquierda(double d){
        setPosicionX(getPosicionX()-d);
    }
    
    public void moverArriba(double d){
        setPosicionY(getPosicionY()+d);
    }
    
    public void moverAbajo(double d){
        setPosicionY(getPosicionY()-d);
    }
    
    public void golpear(Enemigo p){
        super.golpear(p);
        p.evolucionar();
    }

    //GETTERS Y SETTERS
    public int getNumeroBotiquines() {
        return numeroBotiquines;
    }

    public void setNumeroBotiquines(int numeroBotiquines) {
        this.numeroBotiquines = numeroBotiquines;
    }

    @Override
    public String toString() {
        return "Jugador{" + super.toString() + ", numeroBotiquines=" + numeroBotiquines + '}';
    }
}