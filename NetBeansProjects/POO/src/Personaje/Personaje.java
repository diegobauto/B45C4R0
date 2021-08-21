package Personaje;
public class Personaje{
    
    private String nombre;
    private char sexo;
    private double posicionX;
    private double posicionY;
    private double damage;
    private double vida;

    public Personaje(String nombre, char sexo, double posicionX, double posicionY, double damage) {
        this.nombre = nombre;
        this.sexo = sexo;
        this.posicionX = posicionX;
        this.posicionY = posicionY;
        this.damage = damage;
        this.vida = 100;
    }
    
    public void golpear(Personaje p){
        p.setVida(p.getVida()-(damage/calcularDistanciaRespectoPersonaje(p)));
    }
    
    public void recibirImpacto(double d){
        vida -= d;
    }
    
    public double calcularDistanciaRespectoPersonaje(Personaje p){
        return Math.sqrt(Math.pow(p.posicionX-posicionX,2) + Math.pow(p.posicionY-posicionY,2));
    }
    
    //GETTERS Y SETTERS
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getSexo() {
        return sexo;
    }

    public void setSexo(char sexo) {
        this.sexo = sexo;
    }

    public double getPosicionX() {
        return posicionX;
    }

    public void setPosicionX(double posicionX) {
        this.posicionX = posicionX;
    }

    public double getPosicionY() {
        return posicionY;
    }

    public void setPosicionY(double posicionY) {
        this.posicionY = posicionY;
    }

    public double getDamage() {
        return damage;
    }

    public void setDamage(double damage) {
        this.damage = damage;
    }

    public double getVida() {
        return vida;
    }

    public void setVida(double vida) {
        if(vida<0){
            this.vida = 0;
        }
        else if(vida>100){
            this.vida = 100;
        }
        else{
            this.vida = vida;
        }
    }

    @Override
    public String toString() {
        return "nombre=" + nombre + ", sexo=" + sexo + ", posicionX=" + posicionX + ", posicionY=" + posicionY + ", damage=" + damage + ", vida=" + vida ;
    }
}

