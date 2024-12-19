
public class Aufgabe1 { //Kopf der Klasse
    
    public static void main(String[] args) { //Methode main()
        String name = "Max";
        System.out.println("Der Name ist: " + name);
        int age = 20;
        System.out.println(name + " ist "+ age + " Jahre alt.");
        
        int a = 8;
        int b = 3;
        int c = a + b;
        int d = a - b;
        int e = a * b;
        System.out.println("a + b = " + c);
        System.out.println("a - b = " + d);
        System.out.println("a * b = " + e);
        
        double x = 10;
        double y = 3.5;
        double xpy = x + y;
        double xty = x * y;
        System.out.println("Das Ergebnis von x + y ist: " + xpy);
        System.out.println("Das Ergebnis von x * y ist: " + xty);
        
        String eins = "Java ist";
        String zwei = "easy!";
        System.out.println(eins + " " + zwei);
    }

}