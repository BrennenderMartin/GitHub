
public class Aufgabe2
{
    public static void main(String[] args) { //Methode main()
        int a = 5; //Wechsle hier auch mal 5 und 3 aus.
        int b= 3;
        
        if (a > b) {
        System.out.println("a ist größer als b");
        } else {
        System.out.println("a ist nicht größer als b");
        }
        
        for (int j = 0; j < 5; j++) {
        System.out.println("j ist: " + j);
        }
        
        int ergebnis = 1;
        for (int j = 1; j <= 5; j++) {
        ergebnis *= j;
        }
        System.out.println("Das Produkt der Zahlen von 1 bis 5 ist: " + ergebnis);
    }
}
