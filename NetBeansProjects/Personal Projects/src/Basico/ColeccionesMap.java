package Basico;

import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;

public class ColeccionesMap {
    public static void HashMap(){
        Map<Integer, String> estudiantes = new HashMap<>();        
        
        estudiantes.put(3, "Pedro");
        estudiantes.put(2, "Ana");
        estudiantes.put(5, "Enrique");
        estudiantes.put(1, "Danna");
        
        Iterator it = estudiantes.keySet().iterator();
        
        System.out.println("\n---- HashMap ----\nNo le importa el orden, los pone como quiera");
        while (it.hasNext()){
            Integer key =(Integer) it.next();
            System.out.println("Key:"+key+" - Value:"+ estudiantes.get(key));
        }
    }
    
    public static void TreeMap(){
        Map<Integer, String> estudiantes = new TreeMap<>();
        
        estudiantes.put(3, "Pedro");
        estudiantes.put(2, "Ana");
        estudiantes.put(5, "Enrique");
        estudiantes.put(1, "Danna");
        
        Iterator it = estudiantes.keySet().iterator();
        
        System.out.println("\n---- TreeMap ----\nLos organiza de menor a mayor");
        while (it.hasNext()){
            Integer key =(Integer) it.next();
            System.out.println("Key:"+key+" - Value:"+ estudiantes.get(key));
        }
    }
    
    public static void LinkedHashMap(){
        Map<Integer, String> estudiantes = new LinkedHashMap<>();
        
        estudiantes.put(3, "Pedro");
        estudiantes.put(2, "Ana");
        estudiantes.put(5, "Enrique");
        estudiantes.put(1, "Danna");
        
        Iterator it = estudiantes.keySet().iterator();
        
        System.out.println("\n---- LinkedHashMap ----\nLos deja tal cúal como están");
        while (it.hasNext()){
            Integer key =(Integer) it.next();
            System.out.println("Key:"+key+" - Value:"+ estudiantes.get(key));
        }
    }

    public static void main(String[] args) {
        ColeccionesMap objeto = new ColeccionesMap();
        HashMap();
        
        //Puedo llamar a mi objeto directamente o a partir de una istancia
        //TreeMap();
        //Colecciones.TreeMap();
        objeto.TreeMap();
        
        LinkedHashMap();
    }
}
