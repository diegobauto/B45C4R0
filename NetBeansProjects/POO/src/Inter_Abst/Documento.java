package Inter_Abst;

public abstract class Documento implements Validacion{
    
    private String titulo;
    private int numHojas;
    
    public Documento(String titulo) {
        this.titulo = titulo;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    
    public abstract void validar();
}
