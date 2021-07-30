package POO.Polimorfismo2;
//El polimorfismo toma la forma de la cual yo cree la instancia

public class main {
    public static void main(String[] args) {
        
        //Utilizando polimorfismo
        //El objeto se comporta tal como la clase padre
        //NO puedo utilizar metodos propios de la clase Hija
        ClasePadre objeto1 = new ClaseHija_Resta();
        objeto1.pedirDatos();
        objeto1.Operacion(); //No puedo utilizar metodos de la clase hija
        objeto1.MostrarDatos();
        
        //El objeto se comporta tal como la clase Hija
        //En este caso si puedo utilizar metodos propios de la clase Hija
        ClaseHija_Resta objeto2 = new ClaseHija_Resta();
        objeto2.pedirDatos();
        objeto1.Operacion(); //Puedo utilizar los metodos de la clase padre ya que hereda
        objeto1.MostrarDatos();
        objeto2.clasePropiaResta();
    }
}
