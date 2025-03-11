package Unterricht;

public class Sudoku {
    // Objekte deklarieren
    Display fenster;
    Boolean spielEnde;
    
    int[][] array = { 
                    {0, 0, 0, 1, 9, 0, 0, 0, 7},
                    {9, 0, 8, 7, 0, 2, 0, 0, 0},
                    {2, 7, 0, 0, 0, 0, 0, 6, 9},
                    {0, 3, 5, 0, 7, 9, 0, 0, 4},
                    {8, 0, 0, 0, 0, 0, 0, 0, 5},
                    {7, 0, 6, 5, 0, 0, 0, 1, 0},
                    {0, 0, 0, 0, 0, 5, 0, 0, 0},
                    {0, 0, 0, 0, 0, 1, 4, 5, 0},
                    {5, 1, 4, 6, 2, 7, 0, 0, 0}
                    };
                    
    //ACHTUNG, untererste Zeile fehlt noch: 5, 1, 4, 6, 2, 7, 0, 0, 0
    

    public static void main(String[] args) {
        new Sudoku();
    }

    public Sudoku() {
        //Fenster wird erstellt durch Konstruktor-Aufruf von Display
        fenster = new Display("Sudoku-Spiel"); 
        
        //Hier werden die Eingabefelder generiert.
        fenster.prompt("Spalte", 1);
        fenster.prompt("Zeile", 1);
        fenster.prompt("Zahl", 5);
        
        //Die Methode starteSpiel wird geöffnet. 
        starteSpiel( ); 
    }
    
    /* Hier werden die Werte aus dem Display eingelesen 
     * und Arbeitsschritte aufgerufen */
    public void starteSpiel (  ) {
        //Erst wenn "Bestellen" gedrückt wird, werden die Textfelder eingelesen. 
        while(true) {
            //Lokale Variablen werden generiert
            int spalte, zeile, eingabe;
            
            //Liest die Werte der Eingabe ein
            fenster.ready("Drücke Button \"Eintragen\", wenn alle Werte eingegeben sind.");
            spalte = fenster.getInt("Spalte");
            zeile = fenster.getInt("Zeile");
            eingabe = fenster.getInt("Zahl");
            fenster.println("In Spalte " + spalte + " und Zeile " + zeile + " soll die Zahl " + eingabe + " eingegeben");
            
            //Nur wenn die Werte im Bereich von 1-9 sind, gehts weiter.
            if(pruefeEingabe( spalte-1 , zeile-1 , eingabe )) {
                fenster.println("ERROR! Nur Zahlen zwischen 1-9 eintragbar!");
            }
            
            //AB HIER MUSST DU RAN!
            else {
                setzeNeuenWert( spalte , zeile , eingabe ); //?
                gebeSudokuAus();
            }
            fenster.println(" ");
            fenster.println("---------------------------");
            fenster.println(" ");
        }
        
    }
    
    
    //Der eingegebene Wert muss an der richtigen Stelle gespeichert werden. 
    //Achtung: Eingaben von 1-9, Array Speicherung von 0-8!!! Lösung finden. 
    //Lösung kann auch beim Aufrufen der Funktion geschaffen werden (Zeile 60)
    public void setzeNeuenWert( int s, int z, int e ) {
        
    }
    
    
    //Hier soll das gesamte Sudoku ausgegeben werden.
    //Aktuell gibt die Methode nur die erste Zeile aus. 
    public void gebeSudokuAus() {
        //array[0].length gibt dir die Länge der Spalten (Vertikal)
        //array.length gibt dir die Länge der Zeilen (Horizontal)
        
        for(int i = 0; i<array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                fenster.print(array[i][j]+"   "); //Element schreiben
            }
            fenster.println(" "); //Neue Zeile
        }
        
    }
    
    
    public boolean pruefeEingabe( int s, int z, int e ) {
        if (s < 0 || s >= array.length || z < 0 || z >= array[0].length || e < 1 || e > 9)
            return true;
        else
            return false;
    }
}