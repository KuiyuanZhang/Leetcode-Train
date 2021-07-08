# 链接：https://leetcode-cn.com/problems/count-primes
# 统计所有小于非负整数 n 的质数的数量。

# 示例 1：
# 输入：n = 10 
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#    y  
# 示例 2：
# 输入：n = 0
# 输出：0

# 示例 3：
# 输入：n = 1
# 输出：0
#  
# 提示：
# 0 <= n <= 5 * 106

# 质数：只能整除1和本身，整除其他数则不是

# 1. 暴力枚举法
# 时间复杂度O(n^2)
# 空间复杂度O（1）
class Solution(object):
    @classmethod
    def isPrime(self, num):
        for i in range(2, num):
            if num%i == 0:
                return True
        return False
        
    @classmethod
    def countPrimes_1(self, n: int) -> int:
        if n <= 2: return 0
        find = 0
        for num in range(2, n):
            if self.isPrime(num):
                find += 1
        return find


    # 2. 优化判断质数遍历的枚举法
    # - 实际上，并不需要除以所有小于等于某整数(c)的整数来判断该整数(c)是否为质数。
    # - 因为，除该整数(c)的平方根外，其他所有可以整除该整数的两个数，都是一个小于平方根，一个大于平方根。例如： 4 < sqrt(24) < 6
    # - 所以，当除到该整数(c)的平方根时，就已经可以将所有可能的情况枚举出来了。
    # 时间复杂度O(n)
    # 空间复杂度O（1）
    @classmethod
    def isPrime(self, num):
        for i in range(2, int(pow(num, 0.5))+1):
            if num%i == 0:
                return True
        return False
        
    @classmethod
    def countPrimes_2(self, n: int) -> int:
        if n <= 2: return 0
        find = 0
        for num in range(2, n):
            if self.isPrime(num):
                find += 1
        return find

    # 3. 再优化判断质数遍历的枚举法
    # 在解法二的基础上，我们发现其实如果已经除了2，那么再除4、6等偶数都是没有意义的。
    # 因此，我们将算法优化为只除以之前已经发现的质数，得到如下算法：
    # 时间复杂度O(n)
    # 空间复杂度O（1）
    @classmethod
    def isPrime(self, num):
        for i in range(2, int(pow(num, 0.5))+1):
            if num%i == 0:
                return True
        return False
        
    @classmethod
    def countPrimes_3(self, n: int) -> int:
        find = []
        for num in range(2, n):
            for i in find:
                find += 1
        return find




def main():
    n = 10
    final = Solution.countPrimes(n)
    print(final)


if __name__ == "__main__":
    main()