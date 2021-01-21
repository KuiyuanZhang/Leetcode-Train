
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


    # 1. 记忆化递归
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


def main():
    n = 10
    a = Solution(n)
    b = a.climbStairs_2(n)
    print(b)


if __name__ == "__main__":
    main()