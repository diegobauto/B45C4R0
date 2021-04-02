package SENA1.Actividad1;

public class Empleado extends Persona{
    private int antiguedad;
    private int dVacaciones;

    public Empleado(){
        super();
        System.out.print("Digite la antiguedad: ");
        antiguedad = Main.entrada.nextInt();

        System.out.print("Digite el número de días de Vacaciones: ");
        dVacaciones = Main.entrada.nextInt();
    }

    public int obtenerSalario() {
        return antiguedad*500000-dVacaciones*50000;
    }

}
