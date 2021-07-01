package Basico;

public class zzz {
    public static void main(String[] args) {
        System.out.println(calcularPorcentajeBono(10, 500000));
    }
    
    public static double calcularPorcentajeBono(int anios,float bono) {
        double porcentaje = 0;
        if (anios >= 10){
            porcentaje = 0.3;
        }
        else if (anios >=5 && anios<10 ){
            porcentaje = 0.2;
        }
        else if (anios >=3 && anios<5 ){
            porcentaje = 0.1;
        }
        else if (anios <3){
            porcentaje = 0.05;
        }
        return porcentaje*bono;
    }
}