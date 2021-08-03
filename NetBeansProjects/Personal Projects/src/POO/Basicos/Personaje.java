package POO.Basicos;

import POO.Cuenta_Cliente.Persona;

public class Personaje {
    // --------------------------------------------------------
    private String nombre;
    private char sexo;
    private double posicionX, posicionY, distanciaTotal, vida;
    private int numeroBotiquines;

    public Personaje(String nombre, char sexo) {
        this.nombre = nombre;
        this.sexo = sexo;
        this.posicionX = 0;
        this.posicionY = 0;
        this.distanciaTotal = 0;
        this.vida = 100;
        this.numeroBotiquines = 0;
    }

    // --------------------------------------------------------
    public void usarBotiquin(){
        if(numeroBotiquines > 0){
            numeroBotiquines -= 1;
            vida += 5;
        }  
    }
    
    public void recogerBotiquin(){
        numeroBotiquines += 1;
    }
    
    public void moverDerecha(double d){
        posicionX += d;
        distanciaTotal += d;
    }
    
    public void moverIzquierda(double d){
        posicionX -= d;
        distanciaTotal += d;
    }
    
    public void moverArriba(double d){
        posicionY += d;
        distanciaTotal += d;
    }
    
    public void moverAbajo(double d){
        posicionY -= d;
        distanciaTotal += d;
    }
    
    public double calcularDistanciaRespectoOrigen(){
        return Math.sqrt(Math.pow(posicionX, 2)+Math.pow(posicionY, 2));
    }

    
    // **********************************************
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

    public double getDistanciaTotal() {
        return distanciaTotal;
    }

    public void setDistanciaTotal(double distanciaTotal) {
        this.distanciaTotal = distanciaTotal;
    }

    public double getVida() {
        return vida;
    }

    public void setVida(double vida) {
        this.vida = vida;
    }

    public int getNumeroBotiquines() {
        return numeroBotiquines;
    }

    public void setNumeroBotiquines(int numeroBotiquines) {
        this.numeroBotiquines = numeroBotiquines;
    }

    @Override
    public String toString() {
        return "Personaje {" + "nombre=" + nombre + ", sexo=" + sexo + ", posicionX=" + posicionX + ", posicionY=" + posicionY + ", distanciaTotal=" + distanciaTotal + ", numeroBotiquines=" + numeroBotiquines + ", vida=" + vida + "}";
    }
    
    public static void main(String[] args) {
        Personaje explorer = new Personaje("Explorador", 'm');
        explorer.moverDerecha(2);
        explorer.moverAbajo(5);
        explorer.moverIzquierda(1);
        System.out.println(explorer.calcularDistanciaRespectoOrigen());
        explorer.setVida(explorer.getVida()-40);
        System.out.println(explorer.getVida());
        explorer.recogerBotiquin();
        explorer.recogerBotiquin();
        explorer.recogerBotiquin();
        explorer.usarBotiquin();
        explorer.usarBotiquin();
        System.out.println(explorer);
    }
}