package Basico;
public class Tablas4
{
    static int a,b,c,res;
    static Tablas4 Tablita;
    public static void main(String args[])
    {
        Tablita=new Tablas4();
        for(a=4;a<7;a++)
        {
            for(b=1;b<=10;b++)
            {
                res=Tablita.Resultado();
                System.out.println(" "+a+" "+b+" "+res);
            }
        }
    }
    public Tablas4()
    {
        res=0;
    }
    public int Resultado()
    {
        c=a*b;
        return c;
    }
    
}