package leetcode.L0204;

public class CountPrimes {
    public int countPrimes(int n) {
        boolean[] notPrime = new boolean[n + 1];
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (notPrime[i]) {
                continue;
            }
            count++;
            for (long j = (long)i * i; j < n; j +=i) {
                notPrime[(int)j] = true;
            }
        }

        return count;

    }

    public static void main(String[] args) {
        CountPrimes cp = new CountPrimes();
        System.out.println(cp.countPrimes(1500000));
    }
}
