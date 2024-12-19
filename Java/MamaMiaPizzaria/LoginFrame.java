import javax.swing.*;
import java.awt.*;
import java.util.HashMap;

public class LoginFrame extends JFrame {

    private JTextField usernameField;
    private JPasswordField passwordField;
    private JLabel messageLabel;
    public static User user;
    
    public LoginFrame() {
        super("Anmelden");

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
        JButton loginButton = new JButton("Anmelden");
        JButton backButton = new JButton("Zurück");

        // Anmeldung
        loginButton.addActionListener(e -> handleLogin());

        // Zurück zum Hauptfenster
        backButton.addActionListener(e -> {
            new StartFrame();
            dispose();
        });

        buttonPanel.add(loginButton);
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

    private void handleLogin() {
        String username = usernameField.getText();
        String password = new String(passwordField.getPassword());

        HashMap<String, String> users = RegisterFrame.getUsers();

        // Validierung
        if (users.containsKey(username) && users.get(username).equals(password)) {
            messageLabel.setForeground(Color.GREEN);
            messageLabel.setText("Login erfolgreich!");
            user = new User(username, password);
            System.out.println("LoginFrame" + user);
        } else {
            messageLabel.setForeground(Color.RED);
            messageLabel.setText("Ungültige Anmeldedaten!");
        }
    }
}
