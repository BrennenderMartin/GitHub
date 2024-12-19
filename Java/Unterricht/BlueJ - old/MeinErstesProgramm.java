/**Das aller erste Java Programm**/

public class MeinErstesProgramm { //Kopf der Klasse
    
    public static void main(String[] args) { //Methode main()
        
        System.out.println("Hello World");
        
        int meinErsterInteger;
        meinErsterInteger = 5;
        System.out.println( meinErsterInteger ); //print: 5
        
        double meinErsterDouble;
        meinErsterDouble = 5.0;
        System.out.println( meinErsterDouble); //print: 5.0
        
        int e = 6;
        System.out.println(5 * 3 + ( e / 2 ) );
        //gibt die Zahl 18 aus.
        
        int i = 0; //Wir addieren nun immer i um eins auf 3 unterschiedliche Wege.
        i = i + 1; // i wird zu 1.
        i += 1; // i wird zu 2.
        i++; // i wird zu 3.
        System.out.println("i = " + i );
        
        String text = "Das merke ich mir";
        System.out.println( text );
        text += " hoffentlich";
        System.out.println( text );
        
        boolean stimmts = 5 > 3;
        System.out.println( "Ist 5 kleiner als 3? " + stimmts );
        
    }
    
}