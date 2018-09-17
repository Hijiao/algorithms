package neteast;

public class game {
    private static double cal(int day) {
        if (day < 1) {
            return 1d;
        }
        Double x = cal(day - 1);//yesterday
        return x + (50 - x) * (1 - Math.pow(48 / 49D, x));
    }

    public static void main(String[] args) {
        for (int i = 0; i < 20; i++) {
            System.out.println(i + "  " + cal(i));
        }
    }
}
