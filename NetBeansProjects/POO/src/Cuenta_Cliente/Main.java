package Cuenta_Cliente;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static Scanner entrada= new Scanner(System.in);
    static ArrayList<Persona> personas = new ArrayList<>();

    public static void menuPersona() {
        int opcion = 0;
        while(opcion<1 || opcion>3){
            System.out.println("\nQue eres?: ");
            System.out.println("1) Cliente");
            System.out.println("2) Empleado");
            System.out.println("3) Salir");
            System.out.print("Opción: ");
            opcion = entrada.nextInt();
            switch (opcion) {
                case 1:
                    Cliente cliente = new Cliente();
                    menuCliente(cliente);
                    personas.add(cliente);
                    break;
                case 2:
                    Empleado empleado = new Empleado();
                    menuEmpleado(empleado);
                    personas.add(empleado);
                    break;
                case 3:
                    break;
            }
        }
    }

    public static void menuCliente(Cliente cliente) {
        int rta = 0;
        System.out.println("\n*** CLIENTE ***");
        while (rta<1 || rta>2){
            System.out.println("1) Cuenta de Ahorro");
            System.out.println("2) Cuenta de Inversión");
            System.out.print("Opción: ");
            rta = entrada.nextInt();
        }
        if(rta == 1){
            System.out.println("Ahorro");
            Cuenta cuenta = cliente.getCuentaAhorro();
            menuCuenta(cuenta);
        }
        else if(rta == 2){
            System.out.println("Inversión");
            Cuenta cuenta = cliente.getCuentaInversion();
            menuCuenta(cuenta);
        }
        menuPersona();
    }

    public static void menuCuenta(Cuenta cuenta) {
        int opcionC = 0;
        int dinero = 0;
        while(opcionC<1 || opcionC>3){
            System.out.println("\nQue desea hacer?: ");
            System.out.println("1) Depositar");
            System.out.println("2) Retirar");
            System.out.println("3) Salir");
            System.out.print("Opción: ");
            opcionC = entrada.nextInt();
            if(opcionC == 1) {
                System.out.print("Digite el valor a depositar: ");
                dinero = entrada.nextInt();
                cuenta.depositar(dinero);
            }
            else if(opcionC == 2){
                System.out.print("Digite el valor a retirar: ");
                dinero = entrada.nextInt();
                cuenta.retirar(dinero);
            }
            else if(opcionC == 3){
                break;
            }
            cuenta.mostrarValor();
            menuCuenta(cuenta);
        }
    }

    public static void menuEmpleado(Empleado empleado) {
        System.out.println("\n*** EMPLEADO ***");
        System.out.println(empleado.getNombre()+" su salario es de: $"+empleado.obtenerSalario());
    }

    public static void main(String[] args) {
        int menu=0;
        while(menu !=4){
            System.out.println("\n------ MENU ------");
            System.out.println("1.Ver Personas\n2.Añadir Personas\n3.Actualizar\n4.Salir");
            System.out.println("-------------------");
            System.out.print("Digite la opcion:");
            menu = entrada.nextInt();
            switch(menu){
                case 1:
                    mostrarPersonas();
                    break;
                case 2:
                    menuPersona();
                    break;
                case 3:
                    actualizar();
                    break;
                case 4:
                    break;
            }
        }
    }

    private static void actualizar() {
        System.out.print("Digite el id de la persona: ");
        int respuesta = entrada.nextInt();
        if(respuesta > 0 && respuesta <= personas.size()){
            Persona persona = personas.get(respuesta-1);
            if(persona instanceof Cliente){
                Cliente cliente = (Cliente) persona;
                menuCliente(cliente);
            }
        }
        else{
            System.out.println("\nNo hay registros");
        }
    }

    static public void mostrarPersonas() {
        if(personas.size() > 0){
            System.out.printf("\n%5s%15s%15s%15s\n","id","nombre","C.Ahorro", "C.Inversión");
            for (int i=0; i < personas.size(); i++) {
                Persona persona = personas.get(i);
                if(persona instanceof Cliente){
                    Cliente cliente = (Cliente) persona;
                    System.out.printf("%5d%15s%15s%15s\n",cliente.getId(), cliente.getNombre(),"$"+cliente.getCuentaAhorro().getValor(),"$"+cliente.getCuentaInversion().getValor());
                }
            }
        }
        else{
            System.out.println("\nNo hay registros");
        }
    }
}