package Basico;

import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

public class ColeccionesList {
    public static void main(String[] args) {
        List<String> lista = new ArrayList<>();
        
        lista.add("Uno");
        lista.add("Dos");
        lista.add("Tres");
        lista.add(null);
        
        System.out.println("POSICIÓN: "+lista.get(2)+"\n");
        
        //Imprimir - Opción 1
        lista.forEach((i) -> {
            System.out.println(i);
        });
        
        //lista.clear(); Eliminar toda la lista
        lista.remove(1);
        
        System.out.println("");
        //Imprimir - Opción 2
        for (int i=0; i<lista.size(); i++) {
            System.out.println(lista.get(i));
        }
        
        System.out.println("--------------------");
        LinkedList<Integer> lista2 = new LinkedList<>();
        lista2.add(4);
        lista2.add(5);
        lista2.add(2);
        lista2.addFirst(1); //Lo pongo de primeras en la lista  
        
        System.out.println("OBTENER ULTIMO: "+lista2.getLast());
        
        lista2.forEach((i) -> {
            System.out.println(i);
        });
        
    }
}