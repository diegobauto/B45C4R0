package Condominio;

public class Inmueble {
    private String nCasa;
    private String IDArrendador;
    private double costoMensual;
    private int cantidadMesesArrendado;

    public Inmueble(String nCasa, String IDArrendador, double costoMensual, int cantidadMesesArrendado) {
        this.nCasa = nCasa;
        this.IDArrendador = IDArrendador;
        this.costoMensual = costoMensual;
        this.cantidadMesesArrendado = cantidadMesesArrendado;
    }

    public String getnCasa() {
        return nCasa;
    }

    public void setnCasa(String nCasa) {
        this.nCasa = nCasa;
    }

    public String getIDArrendador() {
        return IDArrendador;
    }

    public void setIDArrendador(String IDArrendador) {
        this.IDArrendador = IDArrendador;
    }

    public double getCostoMensual() {
        return costoMensual;
    }

    public void setCostoMensual(double costoMensual) {
        this.costoMensual = costoMensual;
    }

    public int getCantidadMesesArrendado() {
        return cantidadMesesArrendado;
    }

    public void setCantidadMesesArrendado(int cantidadMesesArrendado) {
        this.cantidadMesesArrendado = cantidadMesesArrendado;
    }

    @Override
    public String toString() {
        return "Inmueble{" + "nCasa=" + nCasa + ", IDArrendador=" + IDArrendador + ", costoMensual=" + costoMensual + ", cantidadMesesArrendado=" + cantidadMesesArrendado + '}';
    }
    
    
}