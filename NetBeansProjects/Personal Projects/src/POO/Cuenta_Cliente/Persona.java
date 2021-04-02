package POO.Cuenta_Cliente;

public class Persona {
    private static int disponible = 1;
    private int id;
    private String nombre;

    public Persona(){
        System.out.print("Digite su nombre: ");
        this.id = disponible;
        this.nombre = Main.entrada.nextLine();
        this.nombre = Main.entrada.nextLine();
        disponible++;
    }

    public int getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }
}

// 1, Diego, cAhorro: 500, cInversion:0
// 2, Jean, cAhora 1000, CInversion:500