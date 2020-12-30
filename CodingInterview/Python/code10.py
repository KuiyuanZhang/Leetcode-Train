# 链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 示例 1：
# 输入：n = 2
# 输出：2

# 示例 2：
# 输入：n = 7
# 输出：21

# 示例 3：
# 输入：n = 0
# 输出：1
# 提示：

# 0 <= n <= 100

# 题目分析：
# 设跳上 nn 级台阶有 f(n) 种跳法。
# 在所有跳法中，青蛙的最后一步只有两种情况： 跳上 1 级或 2 级台阶。
# 当为 1 级台阶： 剩 n−1 个台阶，此情况共有 f(n−1) 种跳法
# 当为 2 级台阶： 剩 n−2 个台阶，此情况共有 f(n−2) 种跳法。


class Solution(object):
    # 1. 递归
    @classmethod
    def numWays_1(cls, n):


    # 2. 记忆化的递归
    @classmethod
    def numWays_1(cls, n):

    # 3. 动态规划
    @classmethod
    def numWays_1(cls, n):




def main():
    n = 6
    a = Solution.minPatchess_2(nums, n)
    print(a)


main()
