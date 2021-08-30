package Nomina;

import java.util.ArrayList;

public class Nomina {
    private ArrayList<Trabajador> trabajadores;

    public Nomina() {
        trabajadores = new ArrayList<>();
    }
    
    public void agregarTrabajador(Trabajador t){
        if(!trabajadores.contains(t)){
            trabajadores.add(t);
        }
    }
    
    public void imprimir(){
        for (int i=0; i<trabajadores.size(); i++) {
            System.out.println(trabajadores.get(i));
        }
    }
    
    public void eliminarTrabajador(String ID){
        for (int i=0; i<trabajadores.size(); i++) {
            if(trabajadores.get(i).getCC().equals(ID)){
                trabajadores.remove(trabajadores.get(i));
            }
        }
    }
    
    public double calcularSalarioQuincenalNomina(){
        double sumaTotal = 0;
        for (int i=0; i<trabajadores.size(); i++) {
            sumaTotal += trabajadores.get(i).salarioQuincenal();
        }
        return sumaTotal;
    }
    
    public double promedioEdadNomina(){
        double sumaEdades = 0;
        for (int i=0; i<trabajadores.size(); i++) {
            sumaEdades += trabajadores.get(i).calcularEdad();
        }
        return sumaEdades/trabajadores.size();
    }
    
    public double desviacionEstandarEdadNomina(){
        double desviacion = 0;
        int n = trabajadores.size();
        for (int i=0; i<n; i++) {
            desviacion += Math.pow(trabajadores.get(i).calcularEdad()- promedioEdadNomina(), 2);
        }
        return Math.sqrt(desviacion/n);
    }
    
    public double salarioQuincenalTrabajador(String ID){
        double salario = 0;
        for (int i=0; i<trabajadores.size(); i++) {
            if(trabajadores.get(i).getCC().equals(ID)){
                salario = trabajadores.get(i).salarioQuincenal();
            }
        }
        return salario;
    }
    //
    
    public ArrayList<Trabajador> getTrabajadores() {
        return trabajadores;
    }

    public void setTrabajadores(ArrayList<Trabajador> trabajadores) {
        this.trabajadores = trabajadores;
    }
}