package HerrLinden;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class fallschirmspringer {
    public static void main(String[] args) {
        double m = 0.2; /* Masse */
        double D = 0.1; /* Federhärte */
        double x = 0.15; /* "Starthöhe" */
        
        double v_alt = 0;
        double v = 0; /* Geschwindigkeit */
        double a = 0; /* Beschleunigung */
        double t = 0; /* Zeit */

        double delta_t = 0.2; /* Änderungsrate */
        int n = 100; /* Anzahl Wiederholungen */

        double[][] result = new double[n][4];

        for (int i = 0; i < n; i++) {
            v_alt = v;
            t = t + delta_t;
            a = -(D / m) * x;
            v = v + a * delta_t;
            x = x + (v + v_alt) / 2 * delta_t;
            System.out.printf("t: %.2f a: %.3f v: %.3f h: %.3f%n", t, a, v, x);
            result[i][0] = t;
            result[i][1] = a;
            result[i][2] = v;
            result[i][3] = x; 
        }
        writeCSV(result, n);
    }

    public static void writeCSV(double[][] result, int n) {
        // Write result matrix to CSV file without recursion
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("result2.csv"))) {
            // Write CSV header
            writer.write("Time(t),Acceleration(a),Velocity(v),Height(x)");
            writer.newLine();
            // Write CSV rows
            for (int i = 0; i < n; i++) {
                writer.write(String.format("%.2f,%.3f,%.3f,%.3f",
                            result[i][0],
                            result[i][1],
                            result[i][2],
                            result[i][3]));
                writer.newLine();
            }
            System.out.println("CSV file 'result.csv' created successfully.");
        } catch (IOException e) {
            System.err.println("Error writing CSV file: " + e.getMessage());
        }
    }
}
