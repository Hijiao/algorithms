package leetcode.L0067;

public class AddBinary {
    private int count(char a, char b, char c) {
        int t = 0;
        if (a == '1')
            t++;
        if (b == '1')
            t++;
        if (c == '1')
            t++;
        return t;

    }

    public String addBinary(String a, String b) {
        String l = a.length() >= b.length() ? a : b;
        String s = a.length() >= b.length() ? b : a;
        int d = l.length() - s.length();


        StringBuilder sb = new StringBuilder();
        int i = l.length() - 1;
        char carry = '0';
        while (i >= d) {
            int t = count(l.charAt(i), s.charAt(i - d), carry);
            sb.insert(0, t % 2 == 0 ? '0' : '1');
            carry = t / 2 > 0 ? '1' : '0';
            i--;
        }
        while (i >= 0) {
            int t = count(l.charAt(i), '0', carry);
            sb.insert(0, t % 2 == 0 ? '0' : '1');
            carry = t / 2 > 0 ? '1' : '0';
            i--;

        }
        if (carry == '1') {
            sb.insert(0, '1');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        AddBinary ab = new AddBinary();
        System.out.println(ab.addBinary("11", "11"));
    }
}
