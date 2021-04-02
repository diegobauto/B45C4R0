package SENA1.Actividad4;

public class Cuenta {
    private int numero;
    private String nombre;
    private int Saldo;

    public Cuenta(){
    }
        
    public Cuenta(int numero, String nombre, int Saldo) {
        this.numero = numero;
        this.nombre = nombre;
        this.Saldo = Saldo;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getSaldo() {
        return Saldo;
    }

    public void setSaldo(int Saldo) {
        this.Saldo = Saldo;
    }

    @Override
    public String toString() {
        return  numero + " " + nombre + " " + Saldo;
    }
}
