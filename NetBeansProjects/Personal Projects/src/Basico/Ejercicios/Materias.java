package Basico.Ejercicios;

import java.util.Scanner;

public class Materias {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        String materia = null;
        int nNotas = 0;
        double nota = 0;
        double valor = 0;
        int i = 0;

        System.out.print("\nDigite el nombre de la matería: ");
        materia = entrada.nextLine();
        materia = materia.toLowerCase();

        System.out.print("Digite el numero de notas: ");
        nNotas = entrada.nextInt();

        switch (materia) {
            case "matematicas":
                for (i=0; i<nNotas; i++) {
                    System.out.print("Valor de Nota "+(i+1)+" :");
                    nota = entrada.nextDouble();
                    valor += nota;
                }
                System.out.println("\nSu promedio es de: "+valor/nNotas);
                break;
            case "espanol":
                while (i<nNotas) {
                    System.out.print("Valor de Nota "+(i+1)+" :");
                    nota = entrada.nextDouble();
                    valor += nota;
                    i++;
                }
                System.out.println("\nSu promedio es de: "+valor/nNotas);
                break;
            case "ingles":
                do {
                    System.out.print("Valor de Nota "+(i+1)+" :");
                    nota = entrada.nextDouble();
                    valor += nota;
                    i++;
                } while (i<nNotas);   
                System.out.println("\nSu promedio es de: "+valor/nNotas);             
                break;
            default:
                System.out.println("La materia digitada no corresponde");
                break;
        }
    }
}
