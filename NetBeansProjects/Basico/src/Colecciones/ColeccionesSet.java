package Colecciones;

import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.Set;

public class ColeccionesSet {
    public static void main(String[] args) {
        //Los imprime como quiere
        Set<String> conjunto = new HashSet<>();
        conjunto.add("Juan");
        conjunto.add("Ana");
        conjunto.add("María");
        conjunto.add("Andres");
        
        System.out.println(conjunto);
        for (String i:conjunto) {
            System.out.println(i);
        }
        
        //Los imprime de la forma en que los agrega
        Set<String> conjunto2 = new LinkedHashSet<>();
        conjunto2.add("Perez");
        conjunto2.add("Rodriguez");
        conjunto2.add("Gonzales");
        System.out.println(conjunto2);
    }
}