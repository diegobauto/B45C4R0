package Ejercicios;

public class Autobus{
    //Inserte acá los atributos
    private String nombreConductor;
    private int nPasajeros = 0;
    private double cantidadDinero = 0;
    private int nMaximoPasajeros;
    private double localizacionX = 0;
    private double localizacionY = 0;
    private boolean puertaAbierta;
    private boolean aireAcondicionadoActivado = false;
    private boolean motorEncendido = false;
    private boolean wifiEncendido = false;
    private boolean enMarcha = false;

    
    //Inserte acá el método constructor
    public Autobus(String nombreConductor, int nMaximoPasajeros, boolean puertaAbierta){
        this.nombreConductor = nombreConductor;
        this.nMaximoPasajeros = nMaximoPasajeros;
        this.puertaAbierta = puertaAbierta;
    }
    

    //Inserte acá los métodos (NO LOS GETTER Y SETTERS)
    public void recogerPasajero(int estrato){
        int costoPasaje = 0;
        if (estrato <= 2){
            costoPasaje = 1500;
        }
        else if(estrato <= 4){
            costoPasaje = 2600;
        }
        else{
            costoPasaje = 3000;
        }
        cantidadDinero += costoPasaje; 
    }
    
    public void dejarPasajero(){
        //nPasajeros = nPasajeros - 1;
        nPasajeros -= 1;
    }
    
    public double calcularDistanciaAcopio(){
        double distancia = Math.sqrt(Math.pow(localizacionX,2) + Math.pow(localizacionY,2));
        return distancia;
    }
    
    
    
    
    
    //Inserte acá los SETTERS Y GETTERS
    //GETTERS
    public String getNombreConductor(){
        return nombreConductor;
    }
    public int getnPasajeros(){
        return nPasajeros;
    }
    public double getCantidadDinero(){
        return cantidadDinero;
    }
    public int getnMaximoPasajeros(){
        return nMaximoPasajeros;
    }
    public double getLocalizaxionX(){
        return localizacionX;
    }
    public double getLocalizacionY(){
        return localizacionY;
    }
    public boolean isPuertaAbierta(){
        return puertaAbierta;
    }
    public boolean isAireAcondicionadoActivado(){
        return aireAcondicionadoActivado;
    }
    public boolean isMotorEncendido(){
        return motorEncendido;
    }
    public boolean isWifiEncendido(){
        return wifiEncendido;
    }
    public boolean isEnMarcha(){
        return enMarcha;
    }

    //SETTERS
    public void setNombreConductor(String nombreConductor) {
        this.nombreConductor = nombreConductor;
    }
    public void setnPasajeros(int nPasajeros) {
        this.nPasajeros = nPasajeros;
    }
    public void setCantidadDinero(double cantidadDinero) {
        this.cantidadDinero = cantidadDinero;
    }
     public void setnMaximoPasajeros(int nMaximoPasajeros){
        this.nMaximoPasajeros = nMaximoPasajeros;
    }
    public void setLocalizacionX(double localizacionX){
        this.localizacionX = localizacionX;
    }
    public void setLocalizacionY(double localizacionY){
        this.localizacionY = localizacionY;
    }
    public void setPuertaAbierta(boolean puertaAbierta){
        this.puertaAbierta = puertaAbierta;
    }
    public void setAireAcondicionadoActivado(boolean aireAcondicionadoActivado){
        this.aireAcondicionadoActivado = aireAcondicionadoActivado;
    }
      public void setMotorEncendido(boolean motorEncendido){
        this.motorEncendido = motorEncendido;
    }
    public void setWifiEncendido(boolean wifiEncendido){
        this.wifiEncendido = wifiEncendido;
    }
    public void setEnMarcha(boolean enMarcha){
        this.enMarcha = enMarcha;
    }

    @Override
    public String toString() {
        return "Autobus{" + "nombreConductor=" + nombreConductor + ", nPasajeros=" + nPasajeros + ", cantidadDinero=" + cantidadDinero + ", nMaximoPasajeros=" + nMaximoPasajeros + ", localizacionX=" + localizacionX + ", localizacionY=" + localizacionY + ", puertaAbierta=" + puertaAbierta + ", aireAcondicionadoActivado=" + aireAcondicionadoActivado + ", motorEncendido=" + motorEncendido + ", wifiEncendido=" + wifiEncendido + ", enMarcha=" + enMarcha + '}';
    }
    
    public static void main(String[] args) {
        // Vas a hacer el ejmeplo
    }
}