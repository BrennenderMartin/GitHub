package HerrLinden;
/*
 * f(x) = x^2 + 2x
 * F(x) = 1/3 x^3 + x^2
 * Integral(a-->b) f(x) dx = [(1/3 b^3 + b^2)-(1/3 a^3 + a^2)]
 * 
 * Beispiel f(x) = x^2
 * a = 0 ; b = 6
 * F(x) = 1/3 x^3
 * Integral(0-->6) f(x) dx =  1/3 6^3 - 1/3 0^3 = 186/3 = 72
 */
public class programm {
    int start_range = 0;
    int end_range = 6;
    int[] values;
    
    public static void main(String[] args) {
        new programm();
    }

    public programm() {
        System.out.println(get_area(start_range, end_range));
    }

    public float function(float x) {
        float y = x * x;

        return y;
    }

    public float get_height(int start, int end) {
        float value = 0;
        float i = start;
        int counter = 0;

        while(i <= end) {
            value += function(i);
            //System.out.println(i);
            i += 0.1;
            counter++;
        }
        value = value / counter;
        value = Math.round(value);
        return value;
    }

    public float get_width(int start, int end) {
        return end - start;
    }

    public float get_area(int start, int end) {
        return get_height(start, end) * get_width(start, end);
    }
}