package ChatGPT;

public class Main {
    public static void main(String[] args) {
        // Neues Fenster erstellen
        Display display = new Display("Pizzeria Traditore");

        // Eingabefelder hinzufügen
        display.prompt("Name", "HungrigerTürke da Firenze");
        display.prompt("Bestellung", "Deportare Zaino");
        display.prompt("Lieferadresse", "Florenz");

        // Nachricht ausgeben
        display.ready("Bitte geben Sie Ihre Daten ein und klicken Sie auf Weiter.");

        // Werte auslesen (nachdem der Benutzer Daten eingegeben hat)
        String name = display.getString("Name");
        String bestellung = display.getString("Bestellung");
        String adresse = display.getString("Lieferadresse");

        // Werte in der Konsole anzeigen
        display.println("Name: " + name);
        display.println("Bestellung: " + bestellung);
        display.println("Lieferadresse: " + adresse);
    }
}
