package InterfazGrafica;

import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;


public class appletEtiqueta extends JFrame{

    JPanel panel;
    public appletEtiqueta(){
        setTitle("Botón Y Etiqueta");
        setBounds(10,10,400,200);
        setLocationRelativeTo(null);
        setResizable(false);
        iniciarComponentes();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private void crearPanel(){
        panel = new JPanel();
        panel.setLayout(null);
        getContentPane().add(panel);
    }

    private void crearBoton(){
        JButton boton = new JButton();
        boton.setBounds(150,20,80,40);
        boton.setText("Enviar");
        panel.add(boton);

        JLabel saludo = new JLabel();
        saludo.setBounds(30,80,400,40);
        saludo.setFont(new Font("arial",Font.ITALIC,25));
        panel.add(saludo);


        //Agregando un evento para el boton
        ActionListener oyente = new ActionListener() {
            public void actionPerformed(ActionEvent e){
                saludo.setText("El botón ha sido presionado");
            }
        };
        boton.addActionListener(oyente);
    }

    private void iniciarComponentes(){
        crearPanel();
        crearBoton();
    }

    public static void main(String[] args) {
        appletEtiqueta v1 = new appletEtiqueta();
        v1.setVisible(true); //Hacemos visible la ventana
    }
}