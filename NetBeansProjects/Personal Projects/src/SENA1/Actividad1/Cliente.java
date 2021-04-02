package SENA1.Actividad1;

public class Cliente extends Persona{
    private Ahorro cuentaA = null;
    private Inversion cuentaI = new Inversion();

    public Cliente() {
        super();
    }

    public Ahorro getCuentaAhorro(){
        if(cuentaA == null){
            cuentaA = new Ahorro();
        }
        return cuentaA;
    }

    public Inversion getCuentaInversion(){
        return cuentaI;
    }
}
