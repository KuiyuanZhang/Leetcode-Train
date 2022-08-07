
"""链接：https://leetcode-cn.com/problems/climbing-stairs
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶"""

import math

class Solution:
    def __init__(self, n):
        self.memo = [0 for i in range(n+1)]

    # 1. 递归
    # 时间复杂度：O（2**n）    递归树有2**个结点
    # 空间复杂度：O（n）       递归树有n层
    def climbStairs_1(self, n):
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs_1(n-1) + self.climbStairs_1(n-2)


    # 2. 记忆化递归
    # 时间复杂度：O（n）       一次遍历
    # 空间复杂度：O（n）       mem记忆数组
    def climbStairs_2(self, n):
        if self.memo[n] > 0: 
            return self.memo[n]
        if n == 1: 
            self.memo[n] = 1
        elif n == 2: 
            self.memo[n] = 2
        else:
            self.memo[n] = self.climbStairs_2(n)
        return self.memo[n]

    # 3. 动态规划
    # 思路：
    # 时间复杂度： O（n)
    # 空间复杂度： O（n)
    def climbStairs_3(self, n):
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] +dp[i-2]
        return dp[n]

    # 3. 动态规划 - 滚动数组
    # 思路：
    # 时间复杂度： O（n)
    # 空间复杂度： O（1)
    def climbStairs_3_2(self, n):
        if n == 1 or n == 2:return n
        a, b, tmp = 1, 2, 0
        for i in range(3, n+1):
            tmp = a + b
            a, b = b, tmp
        return tmp



    # # 4. 矩阵快速幂
    # def climbStairs_4(self, n):


    # 5。 通项公式
    def climbStairs_5(self, n):
        import math
        sqrt5 = 5**0.5
        fibin = math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
        return int(fibin/sqrt5)

    # 6. 生成器 yeild
    def climbStairs_5(self, n):
        return 


    # 7. 面向测试用例
    def climbStairs_7(self, n) :
        a = [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155,165580141,267914296,433494437,701408733,1134903170,1836311903]
        return a[n-1]




def main():
    n = 10
    a = Solution(n)
    b = a.climbStairs_2(n)
    print(b)


if __name__ == "__main__":
    main()