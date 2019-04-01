package B;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class B {
    private static int core(String[] wants, Set<String> limits, int per) {
        StringBuilder bestChose = new StringBuilder(per);
        TreeMap<Integer, List> costmap = new TreeMap<>();
        int baseCost = 0;
        for (int i = 0; i < per; i++) {
            int chose1 = 0;
            int chose0 = 0;

            for (String friend : wants) {
                if (friend.charAt(i) == '1') {
                    chose1++;
                } else chose0++;
            }

            if (chose0 > chose1) {
                int cost = chose0 - chose1;
                if (costmap.get(cost) == null) {
                    List l = new LinkedList<Integer>();
                    l.add(i);
                    costmap.put(cost, l);
                } else {
                    costmap.get(cost).add(i);
                }
                bestChose.append('0');
                baseCost += chose1;

            } else if (chose0 < chose1) {
                int cost = chose1 - chose0;
                if (costmap.get(cost) == null) {
                    List l = new LinkedList<Integer>();
                    l.add(i);
                    costmap.put(cost, l);
                } else {
                    costmap.get(cost).add(i);
                }
                bestChose.append('1');
                baseCost += chose0;
            } else {
                int cost = 0;
                if (costmap.get(cost) == null) {
                    List l = new LinkedList<Integer>();
                    l.add(i);
                    costmap.put(cost, l);
                } else {
                    costmap.get(cost).add(i);
                }
                bestChose.append(0);
                baseCost += chose0;
            }

        }
//        System.out.println(bestChose.toString());
//
//        System.out.println(costmap.toString());
//        System.out.println("base cost: " + baseCost);

        if (!limits.contains(bestChose.toString())) {
            return baseCost;
        }
        int[] costArr = new int[per];
        int[] costIndex = new int[per];
        int i = 0;


        Iterator iter = costmap.entrySet().iterator();
        while (iter.hasNext()) {

            Map.Entry<Integer, List> entry = (Map.Entry) iter.next();
            for (Object index : entry.getValue()) {
                costArr[i] = entry.getKey();
                costIndex[i] = (int) index;
                i++;
            }
        }

        int[] chan = new int[per];
        int carr = 0;
        boolean found = false;
        StringBuilder sb = new StringBuilder(bestChose);
        while (true) {
//            sb = new StringBuilder(bestChose);
            arrAdd(chan, per);
            for (int in = 0; in < per; in++) {
                if (chan[in] == 1) {
                    revertSb(sb, costIndex[in]);
                    baseCost += costArr[in];
                }
            }

            if (!limits.contains(sb.toString())) {
                return baseCost;
            }
            for (int in = 0; in < per; in++) {
                if (chan[in] == 1) {
                    revertSb(sb, costIndex[in]);
                    baseCost -= costArr[in];
                }
            }

        }


    }

    private static boolean arrAdd(int[] arr, int len) {
        for (int i = 0; i < len; i++) {
            if (arr[i] == 0) {
                arr[i] = 1;
                return false;
            }
        }
        return true;
    }

    private static int burp(String[] wants, Set<String> limits, int per) {
        int[] cost0 = new int[per];
        int[] cost1 = new int[per];
        for (int i = 0; i < per; i++) {
            int chose1 = 0;
            int chose0 = 0;

            for (String friend : wants) {
                if (friend.charAt(i) == '1') {
                    chose1++;
                } else chose0++;
            }
            cost0[i] = chose0;
            cost1[i] = chose1;
        }
        int[] recods = new int[per];
        int min = 100000;
        StringBuilder sb = new StringBuilder(per);
        for (int i = 0; i < per; i++) {
            sb.append('0');
        }


        while (!arrAdd(recods, per)) {
            for (int i = 0; i < per; i++) {
                sb.setCharAt(i, '0');
            }

            int c = 0;
            for (int i = 0; i < per; i++) {
                if (recods[i] == 0) {
                    sb.setCharAt(i, '0');
                    c += cost0[i];
                } else {
                    c += cost1[i];
                    sb.setCharAt(i, '1');
                }
            }
            if (c < min) {
                if (limits.contains(sb.toString())) {
                    continue;
                }
            }
            min = Math.min(min, c);
        }
        return min;
    }

    private static void revertSb(StringBuilder sb, int index) {
        if (sb.charAt(index) == '1') {
            sb.setCharAt(index, '0');
        } else sb.setCharAt(index, '1');

    }

//    private static Set lessK(int t, int[] arr){
//        HashSet<String> hashSet = new HashSet();
//        for (int k = arr.length - 1; k > 0; k--) {
//            for (int i = 0; i <= arr.length - k; i++) {
//                int cost = 0;
//                for(int c = i;c< i+k;c++){
//                    if (c == t){
//                        return hashSet;
//                    }else
//                        hashSet.add()
//
//                }
//
//                String x = Arrays.sum.substring(i, i + k);
//                if (hashSet.contains(x)) {
//                    str = x;
//                    return;
//                } else
//                    hashSet.add(x);
//            }
//        }
//    }


    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int t = in.nextInt();
        for (int i = 1; i <= t; i++) {
            int friends = in.nextInt();
            String[] wants = new String[friends];
            int lim = in.nextInt();
            Set limit = new HashSet(lim);
            int pre = in.nextInt();

            for (int j = 0; j < friends; j++) {
                wants[j] = in.next();
            }

            for (int j = 0; j < lim; j++) {
                limit.add(in.next());
            }

            System.out.println("Case #" + i + ": " + burp(wants, limit, pre));

        }

//        Set limit = new HashSet();
//        limit.add("1000");
//        System.out.println("ret: " + core(new String[]{"1100", "1010", "0000"}, limit, 4));
//
//        int[] t = new int[]{0, 1, 0, 1};
//        arrAdd(t, 4);
//        arrAdd(t, 4);
//
//        System.out.println(Arrays.toString(t));
    }

}
