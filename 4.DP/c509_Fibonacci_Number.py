
# 链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 示例 1：
# 输入：n = 2
# 输出：1

# 示例 2：
# 输入：n = 5
# 输出：5
#  
# 提示：
# 0 <= n <= 100


class Solution(object):
    
    # 暴力递归
    # 递归会造成重复计算，效率低
    # 时间：
    # 空间：
    @classmethod
    def fib_1(self, n):
        if n == 1 or n == 2: return 1
        else:
            return self.fib_1(n-1) + self.fib_1(n-2) 
    
    # 带备忘录的递归



    @classmethod
    def fib_2(self,tmp, n):
        if n == 1 or n == 2: return 1

    @classmethod
    def run_2(self, n):
        




    # 迭代
    @classmethod
    def fib_2(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b
        return a % 1000000007

    # 动态规划
    @classmethod
    def fib_3(self, n): 
        pass        


def main():
    n = 10
    result = Solution.fib_2(10)
    print(result)


main()