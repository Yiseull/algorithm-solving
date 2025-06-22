import java.util.Arrays;

class Solution {
    public int solution(int[][] info, int n, int m) {
        Arrays.sort(info, (x, y) -> {
            int diff = (x[1] - x[0]) - (y[1] - y[0]);
            return diff != 0 ? diff : Integer.compare(y[0], x[0]);
        });
        
        int aSum = 0, bSum = 0;
        
        for (int[] pair : info) {
            int a = pair[0], b = pair[1];
            
            if (bSum + b < m) {
                bSum += b;
            } else if (aSum + a < n) {
                aSum += a;
            } else {
                return -1;
            }
        }
        
        return aSum;
    }
}