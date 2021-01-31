"""
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入：n = 2
输出：2

示例 2：
输入：n = 7
输出：21

示例 3：
输入：n = 0
输出：1
提示：

0 <= n <= 100

题目分析：
设跳上 n 级台阶有 f(n) 种跳法。
在所有跳法中，青蛙的最后一步只有两种情况： 跳上 1 级或 2 级台阶。
当为 1 级台阶： 剩 n−1 个台阶，此情况共有 f(n−1) 种跳法
当为 2 级台阶： 剩 n−2 个台阶，此情况共有 f(n−2) 种跳法。
"""


class Solution(object):
    # 1. 递归
    # 思路：把 f(n) 问题的计算拆分成 f(n-1)和f(n−2) 两个子问题的计算，并递归，以 f(0) 和 f(1) 为终止条件
    @classmethod
    def numWays_1(cls, n):
        if n <= 1 : return n
        return (cls.numWays_1(n-1) + cls.numWays_1(n-2)) % 1000000007  # 当n很大的时候可能会出现数字溢出，所以我们需要用结果对1000000007求余

    # 2. 记忆化递归
    # 思路：在递归法的基础上，新建一个长度为 n 的数组，用于在递归时存储 f(0)至f(n) 的数字值，重复遇到某数字时则直接从数组取用，避免了重复的递归计算。
    @classmethod
    def numWays_2(cls, n):
        tmp = []

        

    # 3. 动态规划 + 滑动窗口
    # 思路： 以斐波那契数列性质 dp(n+1)= (dp(n)+dp(n−1)) % 1000000007为转移方程。
    @classmethod
    def numWays_3(cls, n):
        if n == 0 : return 0
        if n < 3 : return n
        a, b = 1, 2
        for i in range(3, n):
            tmp = b
            b = (a+b) % 1000000007
            a = tmp
        return b






def main():
    n = 6
    a = Solution.numWays_3(n)
    print(a)


main()
