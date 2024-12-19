package ChatGPT;

import javax.swing.*;
import java.awt.*;
import java.util.HashMap;
import java.util.Map;

public class Display {
    private JFrame frame; // Das Hauptfenster
    private JPanel inputPanel; // Panel für Eingaben
    private JTextArea outputArea; // Bereich für Ausgaben
    private Map<String, JTextField> inputFields; // Map zur Zuordnung von Labels und Eingabefeldern

    /**
     * Konstruktor: Erstellt ein neues Fenster mit dem angegebenen Titel.
     *
     * @param title Titel des Fensters
     */
    public Display(String title) {
        // Initialisiere Hauptfenster
        frame = new JFrame(title);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Initialisiere Eingabepanel
        inputPanel = new JPanel();
        inputPanel.setLayout(new GridLayout(0, 2));
        frame.add(inputPanel, BorderLayout.NORTH);

        // Initialisiere Ausgabebereich
        outputArea = new JTextArea(10, 50);
        outputArea.setEditable(false);
        frame.add(new JScrollPane(outputArea), BorderLayout.CENTER);

        // Initialisiere Map für Eingabefelder
        inputFields = new HashMap<>();

        // Fenster sichtbar machen
        frame.pack();
        frame.setVisible(true);
    }

    /**
     * Gibt einen Text im Ausgabebereich aus.
     *
     * @param text Der anzuzeigende Text
     */
    public void println(String text) {
        outputArea.append(text + "\n");
    }

    /**
     * Fügt ein Eingabefeld mit einem Label und einem Standardwert hinzu.
     *
     * @param label Das Label des Eingabefeldes
     * @param value Der Standardwert des Eingabefeldes
     */
    public void prompt(String label, String value) {
        JLabel jLabel = new JLabel(label);
        JTextField textField = new JTextField(value);
        inputPanel.add(jLabel);
        inputPanel.add(textField);
        inputFields.put(label, textField);

        frame.pack(); // Fenstergröße aktualisieren
    }

    /**
     * Gibt eine Nachricht aus und ermöglicht die Eingabe aus den Feldern.
     *
     * @param message Die Nachricht
     */
    public void ready(String message) {
        println(message);
    }

    /**
     * Liest einen String-Wert aus einem Eingabefeld.
     *
     * @param label Das Label des Eingabefeldes
     * @return Der eingegebene Wert
     */
    public String getString(String label) {
        JTextField textField = inputFields.get(label);
        if (textField != null) {
            return textField.getText();
        }
        return null;
    }

    /**
     * Liest einen Double-Wert aus einem Eingabefeld.
     *
     * @param label Das Label des Eingabefeldes
     * @return Der eingegebene Wert als Double
     * @throws NumberFormatException Wenn der Wert kein gültiger Double ist
     */
    public double getDouble(String label) {
        String text = getString(label);
        if (text != null) {
            return Double.parseDouble(text);
        }
        throw new NumberFormatException("Kein gültiger Double-Wert eingegeben.");
    }

    /**
     * Liest einen Integer-Wert aus einem Eingabefeld.
     *
     * @param label Das Label des Eingabefeldes
     * @return Der eingegebene Wert als Integer
     * @throws NumberFormatException Wenn der Wert kein gültiger Integer ist
     */
    public int getInt(String label) {
        String text = getString(label);
        if (text != null) {
            return Integer.parseInt(text);
        }
        throw new NumberFormatException("Kein gültiger Integer-Wert eingegeben.");
    }

    /**
     * Platziert ein Diagramm (Graph) am unteren Rand des Fensters.
     *
     * @param graph Das Diagramm (als JPanel)
     */
    public void reposition(JPanel graph) {
        frame.add(graph, BorderLayout.SOUTH);
        frame.pack(); // Fenstergröße aktualisieren
    }
}
