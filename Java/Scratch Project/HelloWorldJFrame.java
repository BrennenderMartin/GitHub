import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Font;


public class HelloWorldJFrame {

    public static void main(String[] args) {
        // Create a JFrame
        JFrame frame = new JFrame("Hello World JFrame");

        // Set default close operation
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Set size of the JFrame
        frame.setSize(400, 300); // Width: 400, Height: 300

        // Create a JLabel to display "Hello World!"
        JLabel label = new JLabel("Hello World!", JLabel.CENTER);
        label.setFont(new Font("Arial", Font.BOLD, 24)); // Set font and size

        // Add the JLabel to the JFrame
        frame.add(label);

        // Make the JFrame visible
        frame.setVisible(true);
    }
}
