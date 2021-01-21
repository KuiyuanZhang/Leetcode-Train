class Solution {
    public int climbStairs(int n) {
        if(n == 1){
            return 1;
        }
        if(n == 2){
            return 2;
        }
        return climbStairs(n-1) + climbStairs(n-2);
    }
    public static void main(String[] args){
        int n = 10;
        Solution a = new Solution();
        int b = a.climbStairs(n);
        System.out.println(b);

    }
}