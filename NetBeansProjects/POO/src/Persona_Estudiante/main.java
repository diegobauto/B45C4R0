package Persona_Estudiante;

public class main {

    public static void main(String[] args) {
        Estudiante e1 = new Estudiante("45", "Juan", "juan@mail.com", "español");
        
        e1.dirigir();
        System.out.println(e1.getUrl());
    }
}