import java.io.*;
import java.util.*;

public class Solution {
    public static List<Integer> createArray(int n){
        List<Integer> array=new ArrayList<>();
        for (int i=1;i<=n;i++){
            array.add(i);
        }
        return array;
    }

    public static void main(String[] args) {
        Scanner scanner =new Scanner(System.in);
        int n=scanner.nextInt();
        scanner.close();
        System.out.println(createArray(n));
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}
