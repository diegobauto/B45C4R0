package Asiento;

public abstract class Asiento {
    private char tipo;
    private String ID;
    private boolean pantallaEncendida;
    private double inclinacionSilla;
    private boolean luzLecturaEncendida;
    private boolean luzAsistenciaEncendida;
    private boolean aireAcondicionadoEncendido;

    public Asiento(String ID, char tipo) {
        this.ID = ID;
        this.tipo = tipo;
        this.pantallaEncendida = false;
        this.inclinacionSilla = 90;
        this.luzLecturaEncendida = false;
        this.luzAsistenciaEncendida = false;
        this.aireAcondicionadoEncendido = false;
    }
    
    public void gestionarAireAcondicionado(){
        aireAcondicionadoEncendido = aireAcondicionadoEncendido == false;
    }

    public void gestionarPantalla(){
        if(pantallaEncendida == false){
            pantallaEncendida = true;
        }else{
            pantallaEncendida = false;
        }
    }
    
    public void gestionarLuzLectura(){
        if(luzLecturaEncendida == false){
            luzLecturaEncendida = true;
        }else{
            luzLecturaEncendida = false;
        }
    }
    
    public void gestionarLuzAsistencia(){
        if(luzAsistenciaEncendida == false){
            luzAsistenciaEncendida = true;
        }else{
            luzAsistenciaEncendida = false;
        }
    }
    
    public void aumentarInclinacion(double d){
        inclinacionSilla += d;
        if(inclinacionSilla > 135){
            inclinacionSilla = 135;
        }
    }
    
    public void disminuirInclinacion(double d){
        inclinacionSilla -= d;
        if(inclinacionSilla < 0){
            inclinacionSilla = 0;
        }
    }

    public abstract String imprimirMenuPantalla();

    public char getTipo() {
        return tipo;
    }

    public void setTipo(char tipo) {
        this.tipo = tipo;
    }

    public String getID() {
        return ID;
    }

    public void setID(String ID) {
        this.ID = ID;
    }

    public boolean isPantallaEncendida() {
        return pantallaEncendida;
    }

    public void setPantallaEncendida(boolean pantallaEncendida) {
        this.pantallaEncendida = pantallaEncendida;
    }

    public double getInclinacionSilla() {
        return inclinacionSilla;
    }

    public void setInclinacionSilla(double inclinacionSilla) {
        this.inclinacionSilla = inclinacionSilla;
    }

    public boolean isLuzLecturaEncendida() {
        return luzLecturaEncendida;
    }

    public void setLuzLecturaEncendida(boolean luzLecturaEncendida) {
        this.luzLecturaEncendida = luzLecturaEncendida;
    }

    public boolean isLuzAsistenciaEncendida() {
        return luzAsistenciaEncendida;
    }

    public void setLuzAsistenciaEncendida(boolean luzAsistenciaEncendida) {
        this.luzAsistenciaEncendida = luzAsistenciaEncendida;
    }

    public boolean isAireAcondicionadoEncendido() {
        return aireAcondicionadoEncendido;
    }

    public void setAireAcondicionadoEncendido(boolean aireAcondicionadoEncendido) {
        this.aireAcondicionadoEncendido = aireAcondicionadoEncendido;
    }

    @Override
    public String toString() {
        return "Asiento{" + "tipo=" + tipo + ", ID=" + ID + ", pantallaEncendida=" + pantallaEncendida + ", inclinacionSilla=" + inclinacionSilla + ", luzLecturaEncendida=" + luzLecturaEncendida + ", luzAsistenciaEncendida=" + luzAsistenciaEncendida + ", aireAcondicionadoEncendido=" + aireAcondicionadoEncendido + '}';
    }
    
    
}