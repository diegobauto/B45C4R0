package Inter_Abst;

public class DocumentoWord extends Documento {
    
    private String version;

    public DocumentoWord(String titulo, String version) {
        super(titulo);
        this.version=version;
    }

    @Override
    public void validar() {
        System.out.println("el documento word con titulo :"+ getTitulo()+" ha sido validado");
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    } 
}
