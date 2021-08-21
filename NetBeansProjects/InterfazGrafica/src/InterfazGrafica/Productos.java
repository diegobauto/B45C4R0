package InterfazGrafica;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Font;


public final class Productos extends JFrame{
    
    JPanel panel;
    JLabel orden = null,nombreCliente = null, producto = null,vUnitario = null, cantidad = null;
    JTextField cajaCliente = null, 
        producto1 = null,producto2 = null,producto3 = null,
        valor1= null,valor2= null,valor3= null,
        cantidad1= null,cantidad2= null,cantidad3= null,
        vtotal1 = null,vtotal2 = null,vtotal3 = null, total = null ;

    public Productos(){
        setTitle("PRODUCTOS");
        setBounds(10,10,525,470);
        setLocationRelativeTo(null);
        setResizable(false);
        iniciarComponentes();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private void crearPanel() {
        panel = new JPanel();
        panel.setLayout(null);
        getContentPane().add(panel);
    }

    private void iniciarComponentes(){
        crearPanel();
        crearEtiquetas();
        Cliente();
        crearCajasProductos();
        crearCajasTexto();
        crearBoton();
    }

    private void Cliente(){
        nombreCliente = new JLabel();
        nombreCliente.setText("Cliente: ");
        nombreCliente.setBounds(30, 60, 180, 20);
        nombreCliente.setFont(new Font("ARIAL",Font.BOLD, 15));
        panel.add(nombreCliente);

        cajaCliente = new JTextField();
        cajaCliente.setBounds(100, 60, 130, 20);
        panel.add(cajaCliente);
    }

    private void Etiquetas(JLabel nombreElemento, String titulo, int x, int y){
        nombreElemento = new JLabel();
        nombreElemento.setText(titulo);
        nombreElemento.setBounds(x, y, 150, 20);
        nombreElemento.setFont(new Font("ARIAL",Font.BOLD, 15));
        panel.add(nombreElemento);
    }

    private void crearEtiquetas(){
        Etiquetas(orden, "ORDEN DE COMPRA", 20, 20);
        Etiquetas(producto, "Producto", 50,140);
        Etiquetas(vUnitario, "Vlr.Unitario", 185,140);
        Etiquetas(cantidad, "Cantidad", 303,140);
        Etiquetas(cantidad, "Vlr.Total", 385,140);
        Etiquetas(cantidad, "Valor Total:", 290,280);
    }

    private void CajasTexto(JTextField nombreElemento, int x, int y){
        nombreElemento = new JTextField();
        nombreElemento.setBounds(x, y, 120, 20);
        panel.add(nombreElemento);
    }

    private void crearCajasProductos(){
        CajasTexto(producto1,30,180);
        CajasTexto(producto2,30,210);
        CajasTexto(producto3,30,240);
    }

    private void crearCajasTexto(){
        valor1 = new JTextField();
        valor1.setBounds(160, 180, 130, 20);
        panel.add(valor1);
        valor2 = new JTextField();
        valor2.setBounds(160, 210, 130, 20);
        panel.add(valor2);
        valor3 = new JTextField();
        valor3.setBounds(160, 240, 130, 20);
        panel.add(valor3);

        cantidad1 = new JTextField();
        cantidad1.setBounds(300, 180, 70, 20);
        panel.add(cantidad1);
        cantidad2 = new JTextField();
        cantidad2.setBounds(300, 210, 70, 20);
        panel.add(cantidad2);
        cantidad3 = new JTextField();
        cantidad3.setBounds(300, 240, 70, 20);
        panel.add(cantidad3);

        vtotal1 = new JTextField();
        vtotal1.setBounds(380, 180, 100, 20);
        vtotal1.setEditable(false);
        panel.add(vtotal1);
        vtotal2 = new JTextField();
        vtotal2.setBounds(380, 210, 100, 20);
        vtotal2.setEditable(false);
        panel.add(vtotal2);
        vtotal3 = new JTextField();
        vtotal3.setBounds(380, 240, 100, 20);
        vtotal3.setEditable(false);
        panel.add(vtotal3);

        total = new JTextField();
        total.setBounds(380, 280, 100, 20);
        total.setEditable(false);
        panel.add(total);
    }

    private void crearBoton(){
        JButton boton = new JButton();
        boton.setBounds(380,380,100,30);
        boton.setText("Calcular");
        panel.add(boton);

        JLabel info = new JLabel();
        info.setBounds(30,340,400,20);
        info.setFont(new Font("ARIAL",Font.BOLD,15));
        panel.add(info);

        //Agregando un evento para el boton
        ActionListener oyente = new ActionListener() {
            public void actionPerformed(ActionEvent e){
                try{
                    int v1 = Integer.parseInt(valor1.getText())*Integer.parseInt(cantidad1.getText());
                    int v2 = Integer.parseInt(valor2.getText())*Integer.parseInt(cantidad2.getText());
                    int v3 = Integer.parseInt(valor3.getText())*Integer.parseInt(cantidad3.getText());
                    vtotal1.setText(String.valueOf(v1));
                    vtotal2.setText(String.valueOf(v2));
                    vtotal3.setText(String.valueOf(v3));
                    int calcularTotal = v1+v2+v3;
                    total.setText(String.valueOf(calcularTotal)); 
                    info.setText("Señor@ "+cajaCliente.getText()+" el total de su compra es $"+total.getText());
                }catch(Exception z){
                    info.setText("Falta algun campo por llenar");
                }
            }
        };
        boton.addActionListener(oyente);
    }

    public static void main(String[] args) {
        Productos productos = new Productos();
        productos.setVisible(true);
    }
}