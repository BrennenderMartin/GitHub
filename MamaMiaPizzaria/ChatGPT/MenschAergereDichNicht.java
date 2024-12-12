package ChatGPT;

import javax.swing.*;
import java.awt.*;
//import java.awt.event.ActionEvent;
//import java.awt.event.ActionListener;

public class MenschAergereDichNicht {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(MenschAergereDichNicht::createAndShowGUI);
    }

    private static void createAndShowGUI() {
        JFrame frame = new JFrame("Mensch Ärgere Dich Nicht");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);
        frame.setLayout(new BorderLayout());

        // Header Section
        JPanel headerPanel = new JPanel();
        headerPanel.setBackground(new Color(0, 120, 215)); // Microsoft-style blue
        headerPanel.setLayout(new FlowLayout(FlowLayout.CENTER));
        JLabel headerLabel = new JLabel("Mensch Ärgere Dich Nicht");
        headerLabel.setForeground(Color.WHITE);
        headerLabel.setFont(new Font("Segoe UI", Font.BOLD, 24));
        headerPanel.add(headerLabel);
        frame.add(headerPanel, BorderLayout.NORTH);

        // Game Board Section
        JPanel boardPanel = new JPanel();
        boardPanel.setLayout(new GridLayout(11, 11)); // 11x11 grid for game board

        for (int i = 0; i < 121; i++) {
            JButton cell = new JButton();
            cell.setEnabled(false);
            cell.setBackground(Color.LIGHT_GRAY);

            // Example: Marking the starting positions
            if (i == 0 || i == 10 || i == 110 || i == 120) {
                cell.setBackground(Color.YELLOW);
            }

            boardPanel.add(cell);
        }

        frame.add(boardPanel, BorderLayout.CENTER);

        // Footer Section
        JPanel footerPanel = new JPanel();
        footerPanel.setBackground(new Color(240, 240, 240));
        footerPanel.setLayout(new FlowLayout(FlowLayout.CENTER));
        JLabel footerLabel = new JLabel("Mensch Ärgere Dich Nicht - Simple Java Edition");
        footerLabel.setFont(new Font("Segoe UI", Font.PLAIN, 12));
        footerPanel.add(footerLabel);
        frame.add(footerPanel, BorderLayout.SOUTH);

        frame.setLocationRelativeTo(null); // Center on screen
        frame.setVisible(true);
    }
}
