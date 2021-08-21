package Cuenta_Cliente;

public class Ahorro extends Cuenta{
    private int nMes = -1;
    private int porcentaje;

    public Ahorro() {
        super(1000, 500);
        while(nMes<1 || nMes>12){
            System.out.print("Digite la numero de Mes: ");
            nMes = Main.entrada.nextInt();
        }
        
        System.out.print("Digite el porcentaje: ");
        porcentaje = Main.entrada.nextInt();
    }

    public int ahorroAnual() {
        return valor+(valor*porcentaje*nMes)/100;
    }

    @Override
    public void depositar(int dinero) {
        super.depositar(dinero);
        if(ahorroAnual() > 0){
            System.out.println("El ahorro anual es: $"+ahorroAnual());
        }
    }
}
