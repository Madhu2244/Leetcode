import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        int[] arr= new int[q];
        for (int i = 0; i < q; i++)
            arr[i] = sc.nextInt();
        //System.out.println(Arrays.toString(arr));
        int maxVal = 1;
        for (int i = 0; i < q; i++) {
            int localMax = 1;
            int curMax = arr[i];
            for (int j = i + 1; j < q; j++) {
                if (arr[j] > curMax) {
                    localMax++;
                    curMax = arr[j];
                }
                    /*)
                if (arr[j] - arr[i] < j - i) {
                    continue;
                }
                else {
                    localMax++;
                }*/
            }
            maxVal = Math.max(localMax,maxVal);
        }
        System.out.println(maxVal);
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}
