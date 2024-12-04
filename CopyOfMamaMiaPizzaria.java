import java.util.ArrayList;
import java.util.List;
/**
 * Die Pizzeria
 * 
 * @author: base made by Fischi, edited by Luis and Mattis
 */
public class CopyOfMamaMiaPizzaria
{
    // Bezugsobjekte
    CopyOfDisplay fenster;
    //private CopyOfDisplay fenster;
    
    // Liste von Objekten erstellen
    List<MyObject> objectList = new ArrayList<>();
    
    MyObject inputObject;
    
    // Attribute
    String anschrift_name;
    String bestellungsname;
    String lieferadresse;
    
    int bestellung;
    
    // Konstruktor
    public CopyOfMamaMiaPizzaria()
    {
        fenster = new CopyOfDisplay("Pizzeria Traditore", this);
        fenster();
        fill_list();
        
        start();
    }

    // Dienste
    public static void main(String[] args)
    { 
        @SuppressWarnings("unused")
        CopyOfMamaMiaPizzaria main = new CopyOfMamaMiaPizzaria();
    }

    public void fenster()
    {
        fenster.prompt("Name", "HungrigerTörke da Firenze");
        fenster.prompt("Bestellung", "Deportare Zaino"); // Abschieberucksack
        fenster.prompt("Lieferadresse", "Florenz");
    }

    public void fill_list()
    {
        // Alle Objekte der Speisekarte
        objectList.add(new MyObject("Deportare Zaino", 69.69));
        objectList.add(new MyObject("Pizza", 12.90));
        objectList.add(new MyObject("Pasta", 8.90));
        objectList.add(new MyObject("Pommes", 3.90));
    }
    
    public void start()
    {
        bestellung = 0;
        while(bestellung < 10)
        {
            bestellung++;
            fenster.ready("Taste \"Bestellen\" drücken, wenn alle Werte eingeben. \n");
            anschrift_name = fenster.getString("Name");
            bestellungsname = fenster.getString("Bestellung");
            lieferadresse = fenster.getString("Lieferadresse");
            
            inputObject = new MyObject(bestellungsname);
            
            exe();
        }
    }

    public void exe()
    {
        fenster.println("Auftrag \"" + bestellungsname + 
                        "\" für \"" + anschrift_name + 
                        "\" in Bearbeitung nach \"" + lieferadresse + 
                        "\". \n");
        
        if (objectList.contains(inputObject)) {
            if(bestellungsname.equals("Deportare Zaino"))
            {
                fenster.println("Du kleiner Törke du! Tss tss tss...");
                fenster.println("Zu faul etwas einzugeben? Tss tss tss...\n");
            
            } else { // Lässt nun das essen kochen
                
                fenster.println("Wird zubereitet...\n");
                
                kochen(bestellungsname);
                
            }
        } else {fenster.println("Tippfehler oder nicht auf der Karte, bitte neu bestellen\n");}
    }
    
    public void kochen(String bestellungsname)
    {
        fenster.println("Am kochen (" + bestellungsname + ") ...");
        // An Koch weitergeben
        fenster.println("Das macht 35 € bitte! \n");
    }
    
    public void speisekarte()
    {
        fenster.println("Speisekarte:");
        int index = 1;
        for(MyObject myobject : objectList){fenster.println(index + ". " + myobject.getName() + ", Preis: " + myobject.getAttribute());}
        fenster.println(" ");
    }
    
    public void bezahlen()
    {
        bestellung--;
        fenster.println("Vielen Dank für Ihren Einkauf!");
        fenster.println("Der Bezahlvorgang ist abgeschlossen. \n");
    }

    @Override
    public String toString() {
        return "Hurensohn";
    }
}
