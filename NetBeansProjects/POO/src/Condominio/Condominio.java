package Condominio;

import java.util.ArrayList;

public class Condominio {
    private ArrayList<Inmueble> inmuebles;

    public Condominio() {
        inmuebles = new ArrayList<>();
    }
    
    public void agregarInmueble(Inmueble i){
        inmuebles.add(i);
    }
    
    public void eliminarInmueble(String ID){
        for (int i=0; i<inmuebles.size(); i++) {
            if(inmuebles.get(i).getnCasa().equals(ID)){
                inmuebles.remove(i);
            }
        }
    }
    
    public double calcularArriendoMensualCondominio(){
        double sumaTotal = 0;
        for (int i=0; i<inmuebles.size(); i++) {
            sumaTotal += inmuebles.get(i).getCostoMensual();
        }
        return sumaTotal;
    }
    
    public double promedioCostoInmueble(){
        return calcularArriendoMensualCondominio()/inmuebles.size();
    }
    
    public double desviacionEstandarCostoInmueble(){
        double desviacion = 0;
        int n = inmuebles.size();
        for (int i=0; i<n; i++) {
            desviacion += Math.pow( inmuebles.get(i).getCostoMensual() - promedioCostoInmueble(), 2 );
        }
        return Math.sqrt(desviacion/n);
    }

    public ArrayList<Inmueble> getInmuebles() {
        return inmuebles;
    }

    public void setInmuebles(ArrayList<Inmueble> inmuebles) {
        this.inmuebles = inmuebles;
    }
    
    public void imprimirInmuebles(){
        System.out.println(inmuebles);
    }
}