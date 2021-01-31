// 递归
class Solution {
    public int numWays(int n) {
        return Ways();
    }
    private int Ways(int n){
        if(n<1){
            return 1;
        }
        if(n<2){
            return 2
        }
        return ((Ways(n-1) % 1000000007)+(Ways(n-2)%1000000007))
    }
// 备忘录法  空间换时间
class Solution{
    public int numWays(int n) {
        // 备忘录初始化
        int[] memo = new int[101];
        memo[0] = 1;
        memo[1] = 1;
        memo[2] = 2;
        return Ways(memo, n);
    }
    private