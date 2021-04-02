package SENA2.Actividad3;

import java.util.Scanner;

public class Triangulo {
    static double A;
    static double B;
    static double C;
    
    public static void calcularAngulos(int a, int b, int c){
        double dA = (2*b*c);
        double dB = (2*a*c);
        double dC = (2*a*b);
        A = Math.acos(((b*b)+(c*c)-(a*a))/dA)*(180/Math.PI);
        System.out.println("El angulo en A es de: "+A+"°");
        B = Math.acos(((a*a)+(c*c)-(b*b))/dB)*(180/Math.PI);
        System.out.println("El angulo en B es de: "+B+"°");
        C = Math.acos(((a*a)+(b*b)-(c*c))/dC)*(180/Math.PI);
        System.out.println("El angulo en C es de: "+C+"°");
        System.out.println("Suma de los ángulos: "+(A+B+C)+"°");
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int a, b, c, altura;
        double area =0, s;
        String tipo=null;

        System.out.print("Digite el valor del lado 1: ");
        a = entrada.nextInt();
        System.out.print("Digite el valor del lado 2 (base): ");
        b = entrada.nextInt();
        System.out.print("Digite el valor del lado 3: ");
        c = entrada.nextInt();
        System.out.print("Digite el valor de la altura: ");
        altura = entrada.nextInt();

        //Identificar que tipo de Triangulo es
        if (a!=b && b!=c && a!=c) {
            tipo = "escaleno";
        }
        else if(a==b && b==c){
            tipo = "equilatero";
        }
        else if(a==b || b==c || a==c){
            tipo = "isósceles";
        }
        System.out.println("El Triangulo es "+tipo);

        switch (tipo) {
            case "escaleno":
                calcularAngulos(a,b,c);
                area = (b*altura)/2;
                break;
            case "equilatero":
                s = Math.sqrt(3)/4;
                area = s*(a*a);
                calcularAngulos(a,b,c);
                break;
            case "isósceles":
                calcularAngulos(a,b,c);
                area=0.5*b*altura;
            default:
                break;
        }
        System.out.println("Area: "+area+" m^2");
    }   
}