import java.util.ArrayList;
import java.util.List;
/**
 * Die Pizzeria
 *
 * @author: base made by Fischi, edited by Luis and Mattis
 */
public class CopyOfMamaMiaPizzaria {
    // Bezugsobjekte
    CopyOfDisplay fenster;
    
    // Liste von Objekten erstellen
    List<MyObject> objectList = new ArrayList<>();
    
    MyObject inputObject, outputObject;
    
    // Attribute
    String anschrift_name;
    String bestellungsname;
    String lieferadresse;
    
    int bestellung;
    boolean aktive_bestellung;
    
    public CopyOfMamaMiaPizzaria() { // Konstruktor
        fenster = new CopyOfDisplay("Pizzeria Traditore", this);
        start();
    }

    // Main
    public static void main(String[] args) { // Main used to launch an object
        @SuppressWarnings("unused")
        CopyOfMamaMiaPizzaria main = new CopyOfMamaMiaPizzaria();
    }

    // Private Methodes:
    private void start() { // Setup-main, so the constructor looks nicer
        fenster();
        fill_list();
        
        bestellung = 0;
        while(bestellung < 10) {
            bestellung++;
            fenster.ready("Taste \"Bestellen\" drücken, wenn alle Werte eingeben. \n");
            anschrift_name = fenster.getString("Name");
            bestellungsname = fenster.getString("Bestellung");
            lieferadresse = fenster.getString("Lieferadresse");
            
            inputObject = new MyObject(bestellungsname);
            
            bestellen();
        }
    }

    private void fenster() { // Setup for the prompt-window (alle Prompts)
        fenster.prompt("Name", "HungrigerTörke da Firenze");
        fenster.prompt("Passwort", "DeinPasswort");
        fenster.prompt("Bestellung", "Deportare Zaino"); // Abschieberucksack
        fenster.prompt("Lieferadresse", "Florenz");
    }

    private void fill_list() {// Setup for the Speisekarte (Alle Objekte der Speisekarte)
        objectList.add(new MyObject("Deportare Zaino", 420.69));
        objectList.add(new MyObject("Pizza", 12.90));
        objectList.add(new MyObject("Pasta", 8.90));
        objectList.add(new MyObject("Pommes", 3.90));
    }

    private void bestellen() { // used, as "main" after all the setup
        fenster.println("Auftrag \"" + bestellungsname +
                        "\" für \"" + anschrift_name +
                        "\" in Bearbeitung nach \"" + lieferadresse +
                        "\". \n");
        
        if(objectList.contains(inputObject)) {
            for(int i = 0; i < objectList.size(); i++) {
                if(inputObject.getName().equals(objectList.get(i).getName())) {
                    outputObject = objectList.get(i);
                }
            }
            if(bestellungsname.equals("Deportare Zaino")) {
                fenster.println("Du kleiner Törke du! Tss tss tss...\n" +
                                "Zu faul etwas einzugeben? Tss tss tss...\n");
            } else { // Lässt nun das essen kochen
                fenster.println("Wird zubereitet...\n");
                aktive_bestellung = true;
                kochen(bestellungsname);
            }
        } else {
            fenster.println("Tippfehler oder nicht auf der Karte, bitte neu bestellen\n");
        }
    }
    
    private void kochen(String bestellungsname) { // just gives outputs
        fenster.println("Am kochen (" + bestellungsname + ") ...");
        // An Koch weitergeben
        fenster.println("Das macht " + outputObject.getAttribute() + "0€ bitte! \n");
    }

    // Public Methodes:
    public static void setUsers() { // setup for all possible Users (Used in StartFrame)
        RegisterFrame.users.put("admin", "123");
        RegisterFrame.users.put("DrDoubleNo76", "hackermann123");
        RegisterFrame.users.put("Törke", "42069");
        RegisterFrame.users.put("user", "1234");
        RegisterFrame.users.put("w", "3");
    }

    public void login() { // method for: LogIn button
        new StartFrame();
        if(LoginFrame.user != null) {
            System.out.println("main: " + LoginFrame.user);
            fenster.prompt("Username", LoginFrame.user.getUsername());
        } else {
            System.out.println("Niemand angemeldet");
        }
    }

    public void speisekarte() { // method for: Speisekarte button
        fenster.println("Speisekarte:");
        int index = 1;
        for(MyObject myobject : objectList) {
            fenster.println(index + ". " + myobject.getName() + ", Preis: " + myobject.getAttribute());
            index++;
        }
        fenster.println(" ");
    }
    
    public void bezahlen() { // method for: bezahlen button
        if(aktive_bestellung == true) {
            bestellung--;
            fenster.println("Vielen Dank für Ihren Einkauf!");
            fenster.println("Der Bezahlvorgang ist abgeschlossen. \n");
        } else {
            fenster.println("Keine gültige aktive Bestellung");
        }
        aktive_bestellung = false;
    }

    @Override
    public String toString() { //Eig macht das nicht aber kb das zu löschen und wenn ich das mal verstehe kann das glaub ich mega gut sein
        return "Hurensohn";
    }
}
