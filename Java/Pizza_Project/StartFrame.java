package Pizza_Project;

import javax.swing.*;
import java.awt.*;
import java.util.HashMap;

public class StartFrame extends JFrame {

    public StartFrame() {
        super("LogIn!");

        // Setze ein vertikales Layout für das Fenster
        setLayout(new BoxLayout(getContentPane(), BoxLayout.Y_AXIS));

        // Buttons erstellen
        JButton loginButton = new JButton("Anmelden");
        JButton registerButton = new JButton("Registrieren");
        JButton closeButton = new JButton("Schließen");

        // Gleiche Breite für alle Buttons
        Dimension buttonSize = new Dimension(200, 40); // Breite: 200px, Höhe: 40px
        loginButton.setMaximumSize(buttonSize);
        loginButton.setPreferredSize(buttonSize);
        registerButton.setMaximumSize(buttonSize);
        registerButton.setPreferredSize(buttonSize);
        closeButton.setMaximumSize(buttonSize);
        closeButton.setPreferredSize(buttonSize);

        // Abstände und Ausrichtung setzen
        loginButton.setAlignmentX(Component.CENTER_ALIGNMENT);
        registerButton.setAlignmentX(Component.CENTER_ALIGNMENT);
        closeButton.setAlignmentX(Component.CENTER_ALIGNMENT);

        // Leere Border für Abstände
        loginButton.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));
        registerButton.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));
        closeButton.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));

        // Aktion: Öffnet das Login-Fenster
        loginButton.addActionListener(e -> {
            //checkUsers();
            new LoginFrame();
            dispose(); // Schließt das aktuelle Fenster
        });

        // Aktion: Öffnet das Registrierungs-Fenster
        registerButton.addActionListener(e -> {
            new RegisterFrame();
            dispose(); // Schließt das aktuelle Fenster
        });

        // Aktion: Beendet die Anwendung
        closeButton.addActionListener(e -> {
            dispose();
        });

        // Buttons zum Fenster hinzufügen
        add(Box.createVerticalGlue()); // Platzhalter für flexiblen Abstand (oben)
        add(loginButton);
        add(registerButton);
        add(closeButton);
        add(Box.createVerticalGlue()); // Platzhalter für flexiblen Abstand (unten)

        // Fenster-Einstellungen
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Zentriert das Fenster
        setVisible(true);

        MamaMiaPizzaria.setUsers();
    }

    @SuppressWarnings("unused")
    private static void checkUsers() {
        for (HashMap.Entry<String, String> entry : RegisterFrame.users.entrySet()) {
            System.out.println("Username: " + entry.getKey() + ", Password: " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        new StartFrame(); // Startet das Programm
    }
}
