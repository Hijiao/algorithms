package leetcode.L0125;

/**
 * Created by Max on 2018/8/7.
 */
public class ValidPalindrome {
    private boolean shouldSkip(char c) {
        if ((c <= '9' && c >= '0') || (c <= 'z' && c >= 'a') || (c <= 'Z' && c >= 'A')) {
            return false;
        }
        return true;
    }

    public boolean isPalindrome(String s) {
        int start = 0, stop = s.length() - 1;
        while (start <= stop) {
            if (shouldSkip(s.charAt(start))) {
                start++;
                continue;
            }
            if (shouldSkip(s.charAt(stop))) {
                stop--;
                continue;
            }
            if (Character.toLowerCase(s.charAt(stop)) != Character.toLowerCase(s.charAt(start))) {
                return false;
            } else {
                start++;
                stop--;
            }

        }
        return start > stop;

    }

    public static void main(String[] args) {
        ValidPalindrome vp = new ValidPalindrome();
        System.out.println(vp.isPalindrome("`aca"));
//        System.out.println(vp.isPalindrome("`l;`` 1o1 ??;l`"));
    }
}
