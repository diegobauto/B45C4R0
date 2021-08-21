package Inter_Abst;

public class Main {
    
    public static void main(String[] arg){
    
        Validacion doc1 = new DocumentoPDF("Aprender Java", true);
        DocumentoWord doc2 = new DocumentoWord("Java 2010", "V2010");
        Video v1 = new Video();
        
        ServicioValidacion sv = new ServicioValidacion();
        sv.addDocumento(doc1);
        sv.addDocumento(doc2);
        sv.addDocumento(v1);
        
        sv.validar();  
    } 
}
