package Basico;

public class ordenarArreglo {
    public static void main(String[] args) {
        int numeros[] = new int[10];
        
        for (int i = 0; i < 10; i++) {
            numeros[i] = (int) (Math.random()*10);
            System.out.println(numeros[i]);
        }
        
        System.out.println("------------------------");
        

        for(int i=0; i<numeros.length-1;i++){
            if(numeros[i]>numeros[i+1] ){
                int temp = numeros[i];
                numeros[i] = numeros[i+1];
                numeros[i+1] = temp;
                i = -1;
            }
        }
        
        for (int i = 0; i < numeros.length; i++) {
            System.out.println(numeros[i]);
        }
        
    }
}
