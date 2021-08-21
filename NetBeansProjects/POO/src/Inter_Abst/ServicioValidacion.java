package Inter_Abst;

import java.util.ArrayList;
import java.util.List;

public class ServicioValidacion {
    
    private List<Validacion> listaDocumento = new ArrayList<Validacion>();
    
    public void addDocumento(Validacion documento){
        listaDocumento.add(documento);
    }
    
    public void validar(){
        for (Validacion documento : listaDocumento) {
            documento.validar();
        }
    }
}
