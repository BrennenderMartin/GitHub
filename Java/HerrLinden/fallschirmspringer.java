package HerrLinden;

public class fallschirmspringer {
    public static void main(String[] args) {
        double delta_t = 0.02; /* Änderungsrate */
        double m = 0.2; /* Masse */
        double D = 0.1; /* Federhärte */
        double x = 0.15; /* "Starthöhe" */
        
        double v_alt = 0;
        double v = 0; /* Geschwindigkeit */
        double a = 0; /* Beschleunigung */
        double t = 0; /* Zeit */

        int n = 30; /* Anzahl Wiederholungen */

        double[][] result = new double[n][4];

        for (int i = 0; i < n; i++) {
            t = t + delta_t;
            a = -(D / m) * x;
            v_alt = v;
            v = v + a * delta_t;
            x = x + (v + v_alt) / 2 * delta_t;
            System.out.printf("t: %.2f a: %.3f v: %.3f h: %.3f%n", t, a, v, x);
            result[i][0] = t;
            result[i][1] = a;
            result[i][2] = v;
            result[i][3] = x; 
        }
    }
}
