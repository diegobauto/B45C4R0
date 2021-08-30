package Condominio;

public class main {

    public static void main(String[] args) {
        Inmueble ob1 = new Inmueble("1", "1234", 500000, 6);
        System.out.println(ob1);
        
        Condominio c1 = new Condominio();
        c1.agregarInmueble(ob1);
        c1.imprimirInmuebles();
        
        c1.eliminarInmueble("1");
        c1.imprimirInmuebles();
    }
}