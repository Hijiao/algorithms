package interview.Huawei.L1;

import java.util.*;

/**
 * Created by Max on 2018/8/22.
 */
public class Counter {
    private static int counter(String str) {
        Stack<Integer> stack = new Stack<>();
        Map<Integer, Integer> list = new LinkedHashMap<>();


        for (int i = 0; i < str.length(); i++) {
            char s = str.charAt(i);
            if (s == '(') {
                stack.add(i);
            } else if (s == ')') {
                if (!stack.empty()) {
                    int start = stack.pop();
                    list.put(start, i);
                }
            } else stack.clear();
        }

        Iterator iter = list.entrySet().iterator();
        int start, end, max = 0;
        while (iter.hasNext()) {

            Map.Entry<Integer, Integer> entry = (Map.Entry) iter.next();
            start = entry.getKey();
            end = entry.getValue();

            int next = end + 1;
            while (list.containsKey(next)) {
                next = list.get(next) + 1;
            }
            end = next - 1;
            int curr = end - start + 1;
            max = Math.max(max, curr);
        }

        return max;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(counter(str));
    }
}
