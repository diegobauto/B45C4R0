package SENA1.Actividad1;

public abstract class Cuenta {
    private final int depositoInicial;
    private final int vMinimo;
    protected int valor = 0;

    public Cuenta(int depositoInicial,int vMinimo){
        this.depositoInicial = depositoInicial;
        this.vMinimo = vMinimo;
    }

    public void depositar(int dinero) {
        if(valor == 0){
            if(dinero == depositoInicial){
                valor += dinero;
            }
            else{
                System.out.println("El deposito inicial debe ser de: $"+depositoInicial);
            }
        }
        else{
            valor += dinero;
        }
    }

    public void retirar(int dinero){
        if(valor-dinero >= vMinimo){
            valor -= dinero;
        }
        else{
            System.out.println("Deben quedar en la cuenta como minimo: $"+vMinimo);
        }
    }

    public void mostrarValor() {
        System.out.println("El valor en la cuenta es de:"+valor);
    }

    public int getValor() {
        return valor;
    }
}

