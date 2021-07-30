package POO.Polimorfismo2;

public class ClaseHija_Resta extends ClasePadre{
    
    //Sobreescritura del metodo Operacion del metodo abstracto de la clase Padre
    @Override
    public void Operacion() {
        resultado = numero1 - numero2;
    }
    
    public void clasePropiaResta(){
        System.out.println("Este metodo es propio de la clase Hija - Resta");
    }
    
}
