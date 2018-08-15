package leetcode.L0680;

/**
 * Created by Max on 2018/8/8.
 */
public class ValidPalindromeII {
    private boolean core(String s, int start, int stop, boolean hasDeleted) {
//        if (start < 0 || stop >= s.length()) {
//            return false;
//        }
        while (start <= stop) {
            if (s.charAt(start) == s.charAt(stop)) {
                start++;
                stop--;
            } else break;
        }
        if (start >= stop) {
            return true;
        }

        return !hasDeleted && (core(s, start + 1, stop, true) || core(s, start, stop - 1, true));


    }

    public boolean validPalindrome(String s) {
        return core(s, 0, s.length() - 1, false);
    }

    public static void main(String[] args) {
        ValidPalindromeII vp = new ValidPalindromeII();
        System.out.println(vp.validPalindrome("abbzca"));
    }
}
