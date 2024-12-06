package ChatGPT;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginFrame extends JFrame {

    private JTextField usernameField; // Eingabefeld für Benutzernamen
    private JPasswordField passwordField; // Eingabefeld für Passwort
    private JLabel messageLabel; // Beschriftung für Nachrichten

    public LoginFrame() {
        // Titel des Fensters setzen
        super("Login");

        // Layout einstellen
        setLayout(new BorderLayout());

        // Panel für Eingabe
        JPanel inputPanel = new JPanel(new GridLayout(3, 2, 10, 10));
        inputPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Benutzername
        inputPanel.add(new JLabel("Benutzername:"));
        usernameField = new JTextField();
        inputPanel.add(usernameField);

        // Passwort
        inputPanel.add(new JLabel("Passwort:"));
        passwordField = new JPasswordField();
        inputPanel.add(passwordField);

        // Nachricht (z. B. Fehler oder Erfolg)
        messageLabel = new JLabel("", SwingConstants.CENTER);
        messageLabel.setForeground(Color.RED);

        // Button Panel
        JPanel buttonPanel = new JPanel(new FlowLayout());

        // Login-Button
        JButton loginButton = new JButton("Login");
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                handleLogin();
            }
        });
        buttonPanel.add(loginButton);

        // Abbrechen-Button
        JButton cancelButton = new JButton("Abbrechen");
        cancelButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        buttonPanel.add(cancelButton);

        // Hinzufügen der Panels
        add(inputPanel, BorderLayout.CENTER);
        add(messageLabel, BorderLayout.NORTH);
        add(buttonPanel, BorderLayout.SOUTH);

        // Fenstergröße und Verhalten
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // Fenster zentrieren
        setVisible(true);
    }

    /**
     * Methode zur Verarbeitung des Login-Vorgangs.
     */
    private void handleLogin() {
        String username = usernameField.getText();
        String password = new String(passwordField.getPassword());

        // Vordefinierte Anmeldedaten
        String validUsername = "admin";
        String validPassword = "1234";

        // Überprüfen der Eingaben
        if (username.equals(validUsername) && password.equals(validPassword)) {
            messageLabel.setForeground(Color.GREEN);
            messageLabel.setText("Login erfolgreich!");
            // Weitere Aktionen nach erfolgreichem Login (z. B. Öffnen eines neuen Fensters)
        } else {
            messageLabel.setForeground(Color.RED);
            messageLabel.setText("Ungültige Anmeldedaten. Bitte erneut versuchen.");
        }
    }

    /**
     * Hauptmethode, um das Login-Fenster zu starten.
     */
    public static void main(String[] args) {
        new LoginFrame();
    }
}
