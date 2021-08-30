package Nomina;

public class main {

    public static void main(String[] args) {
        Trabajador t1 = new Trabajador("Daniel", "72023394", 70000.0, 96, 31, 8, 1981);                  
        Trabajador t2 = new Trabajador("Mat", "1037681391", 67000.0, 80, 23, 1, 2000);                   
        Trabajador t3 = new Trabajador("Johan", "33277591", 20000.0, 96, 24, 5, 1970);                   
        Trabajador t4 = new Trabajador("Paulo", "33277591", 40000.0, 96, 7, 3, 2001);
        
        Nomina n = new Nomina();
        n.agregarTrabajador(t1);
        n.agregarTrabajador(t2);
        n.agregarTrabajador(t3);
        
        n.eliminarTrabajador("123456789");
        n.salarioQuincenalTrabajador("72023394");
        n.agregarTrabajador(t4);
        
        n.eliminarTrabajador("72023394");
        
        n.imprimir();
        
        System.out.println(n.calcularSalarioQuincenalNomina());
        System.out.println(n.promedioEdadNomina());
        System.out.println(n.desviacionEstandarEdadNomina());
        System.out.println(n.salarioQuincenalTrabajador("1037681391"));
    }
}