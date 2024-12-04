import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.DecimalFormat;
import java.util.Enumeration;
import java.util.Hashtable;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.SwingConstants;

public class CopyOfDisplay extends JFrame implements ActionListener
{
    private static final long serialVersionUID = 1L;
    /*
     * CopyOfDisplay by J M Bishop July 1999********* is a simple class that provides     
     * facilities for input and output on a window. The data values are entered     
     * in boxes in the input section. Different data choices can be entered if     
     * the driving program asks for them. There is an optional integration with     
     * the Graph class Interface ========= new CopyOfDisplay (title) - sets up a new     
     * CopyOfDisplay object with a title println (string) - prints a string in the     
     * output section prompt (label, value) - sets a box in the input section     
     * with the given label ready (message) - prints a message then enables     
     * reading from the boxes getDouble (label) - reads the double value that     
     * was set with that label getInt (label) - gets the int value that was set     
     * with that label getString (label) - reads the string value that was set     
     * with that label reposition (graph) - takes a graph and places it on the     
     * bottom of the input section     */    
    /*
     * 2014 - berarbeitet von Uwe Mller<br>
     * entkoppelt von Text und Graph<br>
     * umgestellt auf Swing<br>     */
    private String title;
    private CopyOfMamaMiaPizzaria mainProgram; // Referenz zum Hauptprogramm
    public CopyOfDisplay(String t, CopyOfMamaMiaPizzaria mainProgram) {
        this.title = t;             // Titel setzen
        this.mainProgram = mainProgram; // Hauptprogramm-Referenz speichern
        initializeDisplay();        // Fenster initialisieren
    }

    
    private Hashtable<String, Data> table = new Hashtable<String, Data>(10);
    private int xwidth, yheight;
    private JButton okButton, closeButton, loginButton, speisekarteButton, bezahlenButton;
    private JTextArea outDisplay;
    private JPanel inDisplay;
    private JScrollPane inPane, outPane;
    private Watcher okWatcher = new Watcher();
    
    
    private void initializeDisplay()
    {
        xwidth = 1024;
        yheight = 600;        // Groesse
        setSize(xwidth, yheight);        // Fenstertitel
        setTitle(title);        // BorderLayout
        setLayout(new BorderLayout());        // Zeichenflueche einfuegen
        getContentPane().add(new Zeichenflaeche());        // Arbeiten bei Beendigung des Programms
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
    
    public void actionPerformed(ActionEvent e)
    {
        if (e.getSource() == okButton)
        { // Monitor fuer den Beobachter kann verlassen werden.
            okWatcher.ready();
        }
        else if (e.getSource() == closeButton)
        {
            System.exit(0);
        }
        else if (e.getSource() == loginButton)
        {
            mainProgram.login(); // Methode aus dem Hauptprogramm aufrufen
        }
        else if (e.getSource() == speisekarteButton)
        {
            mainProgram.speisekarte(); // Methode aus dem Hauptprogramm aufrufen
        }
        else if (e.getSource() == bezahlenButton)
        {
            mainProgram.bezahlen(); // Methode aus dem Hauptprogramm aufrufen
        }
    }
    /*     * Data<br>     * Einfache Klasse (Kapsel) fuer ein Textfeld und dessen Wert     */
    private class Data
    {
        TextField field;
        String value;
    }
    
    private Data getEntry(String s)
    {
        if (table.containsKey(s))
            return (Data) table.get(s);
        else
        {
            outDisplay.append("\nERROR: No such input label: " + s + "\n");
            return null;
        }
    }
    
    public int getInt(String s)
    {
        Data d = getEntry(s);
        return Integer.valueOf(d.value).intValue();
    }
    
    public double getDouble(String s)
    {
        Data d = getEntry(s);
        return Double.valueOf(d.value).doubleValue();
    }
    
    public String getString(String s)
    {
        Data d = getEntry(s);
        return d.value;
    }
    
    /*     * Eingabefeld einfuegen und initialisieren
     *      * @param d     * @param s     * @param t
    */
    private void insertPrompt(Data d, String s, TextField t)
    {        // Panel fuer Label und Textfeld
        JPanel p;        // Beschriftung rechtsbuendig
        p = new JPanel(new BorderLayout());
        p.add("North", new JLabel(s, SwingConstants.LEFT));
        inDisplay.add(p);        // Textfield reagiert auf Entertaste
        t.addActionListener(this);
        t.setEditable(true);        // Textfeld linksbuendig
        p = new JPanel(new BorderLayout());
        p.add("North", t);
        inDisplay.add(p);        // Data setzen
        d.field = t;
    }
        
    public void prompt(String s, int n)
    {
        Data d = new Data();
        TextField t = new TextField(10);
        insertPrompt(d, s, t);
        d.value = formatInt(n, 0);
        t.setText(d.value);
        table.put(s, d);
    }
    
    public void prompt(String s, double n)
    {
        Data d = new Data();
        TextField t = new TextField(10);
        insertPrompt(d, s, t);
        d.value = Double.toString(n);
        t.setText(d.value);
        table.put(s, d);
    }    
    
    public void prompt(String s, String n)
    {
        Data d = new Data();
        TextField t = new TextField(n.length() + 2);
        insertPrompt(d, s, t);
        d.value = n;
        t.setText(d.value);
        table.put(s, d);
    }
    
    /*     * Beendet das Warten auf die Benutzereingaben<br>
    * Gibt zunaechst eine Meldung aus.<br>     * Ansonsten identisch mir ready()
    *      * @param s     */
    public void ready(String s)
    {
        // Meldung in das Fenster
        outDisplay.append(s + "\n");        // Aktivierung des Button
        okButton.setEnabled(true);        // Fenster wird sichtbar
        setVisible(true);        // Warten auf die Benutzereingaben
        okWatcher.watch();        // Iteration ueber alle Eingabefelder
        // kann man anders schreiben
        for (Enumeration<String> e = table.keys(); e.hasMoreElements();)
        {
            // Name des Feldes
            String name = e.nextElement();
            // Wert zuordnen
            Data d = table.get(name);
            d.value = d.field.getText();
            // in die Hashtabelle schreiben
            table.put(name, d);
        }
    }
    
    /*     * Beendet das Warten auf die Benutzereingaben<br>
     * siehe ready (String)
     */
    public void ready() {
        okButton.setEnabled(true);
        speisekarteButton.setEnabled(true);
        bezahlenButton.setEnabled(true);
        setVisible(true);
        okWatcher.watch();        // copy all the values from the boxes to the table
        for (Enumeration<String> e = table.keys(); e.hasMoreElements();)
        {
            String name = e.nextElement();
            Data d = table.get(name);
            d.value = d.field.getText();
            table.put(name, d);
        }
    }
    
    /* Ausgabe mit Zeilenumbruch
     * @param s
     */
    public void println(String s)
    {
        outDisplay.append(s + "\n");
    }
    
    /* Ausgaben ohne Zeilenumbruch
     * @param s     */
    public void print(String s)
    {
        outDisplay.append(s);
    }
    
    private String formatInt(int zahl, int laenge)
    {
        DecimalFormat format = new DecimalFormat(); // keine Gruppierung
        format.setGroupingUsed(false); // keine Nachkommastellen
        format.setMaximumFractionDigits(0); // Rueckgabe als String
        String wert = format.format(zahl); // Wenn kleiner als gewuenscht, dann fuehrende Leerzeichen
        while (wert.length() < laenge)
        wert = " " + wert;
        return wert;
    }
    
    private class Watcher
    {
        private boolean ok;
        Watcher()
        {
            ok = false;
        }
        
        synchronized void watch()
        {
            while (!ok)
            {
                try
                {
                    // Thread aus dem Monitor verbannt
                    wait(500);
                }
                catch (InterruptedException e)
                {
                }
            }    // Sollte er irgendwann hier ankommen, wird ok wieder false
            ok = false;
        }
        
        synchronized void ready()        
        {    // ok setzen            
            ok = true;    // Benachrichtigung, dass Monitor frei            
            notify();        
        }    
    }    
        
    private class Zeichenflaeche extends JPanel {
        private static final long serialVersionUID = 1L;
    
        Zeichenflaeche() {
            setLayout(new BorderLayout());
    
            // Panel für die Beschriftungen Eingabe und Ausgabe
            JPanel p = new JPanel();
            p.add(new JLabel("EINGABE"));
            p.add(new JLabel("AUSGABE"));
            add(p, "North");
    
            // Neues Panel mit FlowLayout
            p = new JPanel(new GridLayout(1, 2, 10, 10));
    
            // Panel mit zwei Spalten
            // 0 bedeutet, irgendeine Anzahl von Zeilen
            inDisplay = new JPanel(new GridLayout(0, 2, 10, 10));
    
            // Eingabefenster als ScrollPane
            // Dieses passt sich der Größe nicht an.
            inPane = new JScrollPane(inDisplay);
            p.add(inPane);
    
            // Ausgabebereich als TextArea
            outDisplay = new JTextArea();
            outPane = new JScrollPane(outDisplay);
            p.add(outPane);
    
            // Ein- und Ausgabe in die Mitte
            add(p, "Center");
    
            // Panel für die Knöpfe
            p = new JPanel(new BorderLayout());
    
            // Bestellen-Knopf
            okButton = new JButton("Bestellen");
            okButton.addActionListener(CopyOfDisplay.this);
            okButton.setEnabled(false);
            p.add("Center", okButton);
            
            // login-Knopf
            loginButton = new JButton("LogIn");
            loginButton.addActionListener(CopyOfDisplay.this);
            loginButton.setEnabled(true);
            p.add("West", loginButton);

            // Speisekarte-Knopf
            speisekarteButton = new JButton("Speisekarte");
            speisekarteButton.addActionListener(CopyOfDisplay.this);
            speisekarteButton.setEnabled(true);
            p.add("West", speisekarteButton);
    
            // Bezahlen-Knopf
            bezahlenButton = new JButton("Bezahlen");
            bezahlenButton.addActionListener(CopyOfDisplay.this);
            bezahlenButton.setEnabled(true);
            p.add("East", bezahlenButton);
    
            // Ende-Knopf
            closeButton = new JButton("Ende");
            closeButton.addActionListener(CopyOfDisplay.this);
            closeButton.setEnabled(true);
            p.add("South", closeButton);
    
            // Panel unten einfügen
            add("South", p);
        }
    }

}
