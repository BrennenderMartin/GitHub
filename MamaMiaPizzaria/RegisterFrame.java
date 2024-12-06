import javax.swing.*;
import java.awt.*;
import java.util.HashMap;

public class RegisterFrame extends JFrame {

    private static HashMap<String, String> users = new HashMap<>(); // Speicherung der Benutzerdaten

    private JTextField usernameField;
    private JPasswordField passwordField;
    private JLabel messageLabel;

    public RegisterFrame() {
        super("Registrieren");

        // Layout
        setLayout(new BorderLayout());

        // Eingabefelder und Labels
        JPanel inputPanel = new JPanel(new GridLayout(3, 2, 10, 10));
        inputPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        inputPanel.add(new JLabel("Benutzername:"));
        usernameField = new JTextField();
        inputPanel.add(usernameField);

        inputPanel.add(new JLabel("Passwort:"));
        passwordField = new JPasswordField();
        inputPanel.add(passwordField);

        messageLabel = new JLabel("", SwingConstants.CENTER);
        messageLabel.setForeground(Color.RED);

        // Buttons
        JPanel buttonPanel = new JPanel(new FlowLayout());
        JButton registerButton = new JButton("Registrieren");
        JButton backButton = new JButton("Zurück");

        // Registrierung
        registerButton.addActionListener(_ -> handleRegister());

        // Zurück zum Hauptfenster
        backButton.addActionListener(_ -> {
            new StartFrame();
            dispose();
        });

        buttonPanel.add(registerButton);
        buttonPanel.add(backButton);

        // Hinzufügen zu JFrame
        add(inputPanel, BorderLayout.CENTER);
        add(messageLabel, BorderLayout.NORTH);
        add(buttonPanel, BorderLayout.SOUTH);

        // Fenster-Einstellungen
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void handleRegister() {
        String username = usernameField.getText();
        String password = new String(passwordField.getPassword());

        // Validierung der Eingabe
        if (username.isEmpty() || password.isEmpty()) {
            messageLabel.setText("Bitte füllen Sie alle Felder aus!");
        } else if (users.containsKey(username)) {
            messageLabel.setText("Benutzername existiert bereits!");
        } else {
            users.put(username, password); // Benutzer speichern
            messageLabel.setForeground(Color.GREEN);
            messageLabel.setText("Registrierung erfolgreich!");
        }
    }

    public static HashMap<String, String> getUsers() {
        return users;
    }
}
