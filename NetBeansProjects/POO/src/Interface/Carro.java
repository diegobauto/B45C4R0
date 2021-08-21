package Interface;

//Puedo utilizar el concepto de herencia multiple
public class Carro implements Rueda, Silla{

    @Override
    public void avanzar() {
        System.out.println("El carro esta avanzado");
    }

    @Override
    public void frenar() {
        System.out.println("El carro esta frenando");
    }

    @Override
    public void sentarse() {
        System.out.println("El carro tiene "+sillas+" sillas");
    }

}