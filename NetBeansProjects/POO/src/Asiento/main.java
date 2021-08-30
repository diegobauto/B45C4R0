package Asiento;

public class main {

    public static void main(String[] args) {
        Bronce b = new Bronce("K19", 'b');
        
        b.gestionarPantalla();
        b.gestionarLuzLectura();
        b.aumentarInclinacion(100);
        b.disminuirInclinacion(135);
        
        System.out.println(b);
    }
}