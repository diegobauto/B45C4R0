package Personaje;

public class Enemigo extends Personaje{
    
    private int evolucionesAplicadas;
    private int resistencia;
    
    public Enemigo(String nombre, char sexo, double posicionX, double posicionY, double damage) {
        super(nombre, sexo, posicionX, posicionY, damage);
        this.evolucionesAplicadas = 0;
        this.resistencia = 1;
    }
     
    public void evolucionar(){
        if( getVida() <= 30 && evolucionesAplicadas == 0){
            setDamage(getDamage()+20);
            evolucionesAplicadas += 1;
        }
        if( getVida() <= 10 && evolucionesAplicadas == 1 ){
            resistencia += 1;
            evolucionesAplicadas += 1;
        } 
    }
    
    @Override
    public void recibirImpacto(double d){
        setVida(getVida()-(d/resistencia));
    }
    
    //GETTERS Y SETTERS
    public int getEvolucionesAplicadas() {
        return evolucionesAplicadas;
    }

    public void setEvolucionesAplicadas(int evolucionesAplicadas) {
        this.evolucionesAplicadas = evolucionesAplicadas;
    }

    public int getResistencia() {
        return resistencia;
    }

    public void setResistencia(int resistencia) {
        this.resistencia = resistencia;
    }

    @Override
    public String toString() {
        return "Enemigo{" + super.toString() + ", evolucionesAplicadas=" + evolucionesAplicadas + ", resistencia=" + resistencia + '}';
    }
}