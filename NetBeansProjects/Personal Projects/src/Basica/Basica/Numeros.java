package Basica;

public class Numeros {
    public static void main(String[] args) {
        for (int i=1; i<=1000; i++) {
            if(i>500){
                System.out.println(i*2+","+i*3);
            }
            else{
                System.out.println(i*2+","+i*3+","+i*4);
            }
        }
    }
}
