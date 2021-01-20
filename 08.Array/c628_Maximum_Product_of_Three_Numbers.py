"""链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers
给定一个整型数组，在数组中找出由三个数组成的最大乘积，
并输出这个乘积。

示例 1:
输入: [1,2,3]
输出: 6

示例 2:
输入: [1,2,3,4]
输出: 24

注意:
给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。"""

class Solution:

    # 1. 暴力破解
    # 思路：三个一枚举
    # 时间复杂度：O(n**3)
    @classmethod
    def maximumProduct_1(self, nums):
        n = len(nums)
        return [nums[i] * nums[j] * nums[z] 
            for i in range(n) for j in range(i + 1, n) for z in range(j + 1, n)]
    # 2. 排序+贪心
    # 排序后,三种情况 ：全正和全负数都是最后三个乘积最大，两个最小的负数，最小负数乘最大正数最大
    # 时间复杂度：O(N*logN) 排序TimSort
    # 空间复杂度：O(logN)  排序花销
    @classmethod
    def maximumProduct_2(self, nums):
        nums.sort()
        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]
        return max(a, b)

    # 3. 线性扫描(三树排序)
    # 只需要找出最小的两个数和最大的三个数
    # 时间复杂度： O（n）
    # 空间复杂度： O（1）
    @classmethod
    def maximumProduct_3(self, nums):
        a = b = c = float("-inf")   # 最大三个数的初始定义
        d = e = float("inf")        # 最小两个数的初始定义
        for index, num in enumerate(nums):
            # 更新最大值
            if num > a:
                a, b, c = num, a, b
            elif num > b:
                b, c = num, b
            elif num > c:
                c = num
            # 更新最小值
            if num < d:
                d, e = num, d
            elif num < e:
                e = num
        return max(a*b*c, d*e*a)
                
                


def main():
    nums = [1,2,3,4]
    a = Solution.maximumProduct_3(nums)
    print(a)

main()