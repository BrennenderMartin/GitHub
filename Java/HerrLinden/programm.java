package HerrLinden;

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