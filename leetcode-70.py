# 链接：https://leetcode-cn.com/problems/climbing-stairs

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。

# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶

# 示例 2：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶



# 解题思路：
# f(x)=f(x−1)+f(x−2)
# 


class Solution(object):

    # 1. 递归
    # 时间：O（2^n） 递归树有2^n个结点  
    # 空间：O (n)    递归树深度为n
    @classmethod
    def climbStairs_1(cls, n):
        if n == 1: return 1
        if n == 2: return 2
        if n > 2:
            return cls.climbStairs_1(n-1) + cls.climbStairs_1(n-2)



    # # 1. 动态规划
    # @classmethod
    # def  climbStairs_1(cls, ):



    # # 2. 矩阵快速幂
    # @classmethod
    # def  climbStairs_1(cls, ):


    # # 3. 通项公式
    # @classmethod
    # def  climbStairs_1(cls, ):




def main( ):
    n = 6
    a = Solution.climbStairs_1(n)
    print(a)


main()
