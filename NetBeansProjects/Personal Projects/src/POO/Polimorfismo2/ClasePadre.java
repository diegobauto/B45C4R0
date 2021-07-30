package POO.Polimorfismo2;

import java.util.Scanner;

public abstract class ClasePadre {
    protected int numero1, numero2, resultado;
    
    public void pedirDatos(){
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite primer número:");
        numero1 = entrada.nextInt();
        
        System.out.print("Digite el segundo número:");
        numero2 = entrada.nextInt();
    }
    
    //Metodo abstracto
    public abstract void Operacion();
    
    public void MostrarDatos(){
        System.out.println("Resultado: "+ resultado);
    }
}
