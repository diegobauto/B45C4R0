package SENA2.Actividad2;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSpinner;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.SwingConstants;

import java.awt.Font;

public class conversionDias extends JFrame{

    JPanel panel;
    JSpinner number;
    JLabel titulo, entrada, horas, minutos, segundos;

    public conversionDias(){
        setTitle("Conversión de Días");
        setBounds(10,10,500,320);
        setLocationRelativeTo(null);
        setResizable(false);
        iniciarComponentes();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private void crearSpinner(){
        number = new JSpinner();
        number.setBounds(310, 80, 60, 40);
        panel.add(number);
    }

    private void iniciarComponentes() {
        crearPanel();
        crearTitulo();
        crearEtiquetas();
        crearSpinner();
        crearBoton();
    }

    private void crearPanel() {
        panel = new JPanel();
        panel.setLayout(null);
        getContentPane().add(panel);
    }

    private void crearTitulo(){
        titulo = new JLabel();
        titulo.setText("Horas - Minutos y Segundos");
        titulo.setBounds(50, 20, 380, 40);
        titulo.setFont(new Font("MS Gothic",Font.BOLD, 25));
        titulo.setHorizontalAlignment(SwingConstants.CENTER);
        panel.add(titulo);
    }
    

    private void Etiquetas(JLabel nombreElemento, String titulo, int x, int y){
        nombreElemento = new JLabel();
        nombreElemento.setText(titulo);
        nombreElemento.setBounds(x, y, 280, 20);
        nombreElemento.setFont(new Font("ARIAL",Font.BOLD, 20));
        panel.add(nombreElemento);
    }

    private void crearEtiquetas(){
        Etiquetas(entrada, "Ingrese la cantidad de días: ",20,90);
        Etiquetas(horas, "Horas:", 30,180);
        Etiquetas(minutos, "Minutos:", 30,210);
        Etiquetas(segundos, "Segundos:", 30,240);
    }

    private void crearBoton(){
        JButton boton = new JButton();
        boton.setBounds(200,130,80,30);
        boton.setText("Enviar");
        panel.add(boton);

        JLabel horas = new JLabel();
        horas.setBounds(100,180,200,20);
        horas.setFont(new Font("arial",Font.ITALIC,20));
        panel.add(horas);

        JLabel minutos = new JLabel();
        minutos.setBounds(120,210,200,20);
        minutos.setFont(new Font("arial",Font.ITALIC,20));
        panel.add(minutos);

        JLabel segundos = new JLabel();
        segundos.setBounds(140,240,200,20);
        segundos.setFont(new Font("arial",Font.ITALIC,20));
        panel.add(segundos);

        //Agregando un evento para el boton
        ActionListener oyente = new ActionListener() {
            public void actionPerformed(ActionEvent e){
                int valor = (Integer) (number.getValue());
                horas.setText(String.valueOf(valor*24));
                minutos.setText(String.valueOf(valor*1440));
                segundos.setText(String.valueOf(valor*86400));
            }
        };
        boton.addActionListener(oyente);
    }

    public static void main(String[] args) {
        conversionDias HMS = new conversionDias();
        HMS.setVisible(true);
    }
}
