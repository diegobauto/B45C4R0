package Polimorfismo2;

public class ClaseHija_Suma extends ClasePadre{
    
    //Sobreescritura del metodo Operacion del metodo abstracto de la clase Padre
    @Override
    public void Operacion() {
        resultado = numero1 + numero2;
    }
    
}
