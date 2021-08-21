package Persona_Estudiante;

public abstract class Persona {
    private String id, nombre, email, idioma, url;

    public Persona(String id, String nombre, String email, String idioma) {
        this.id = id;
        this.nombre = nombre;
        this.email = email;
        this.idioma = idioma;
        this.url = "educursos.com";
    }
    
    public abstract void dirigir();

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getEmail() {
        return email;
    }

    public String getIdioma() {
        return idioma;
    }

    public void setIdioma(String idioma) {
        this.idioma = idioma;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
}