# 链接：https://leetcode-cn.com/problems/patching-array
# 定一个已排序的正整数数组 nums，和一个正整数 n 。
# 从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。
# 请输出满足上述要求的最少需要补充的数字个数。


# 示例 1:
# 输入: nums = [1,3], n = 6
# 输出: 1 
# 解释:
# 根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
# 现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
# 其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
# 所以我们最少需要添加一个数字。

# 示例 2:
# 输入: nums = [1,5,10], n = 20
# 输出: 2
# 解释: 我们需要添加 [2, 4]

# 示例 3:
# 输入: nums = [1,2,2], n = 5
# 输出: 0


class Solution(object):
    # 1. 贪心算法
    # 证明：对于正整数 xx，如果区间 [1,x-1][1,x−1] 内的所有数字都已经被覆盖，且 xx 在数组中，则区间 [1,2x-1][1,2x−1] 内的所有数字也都被覆盖
    # 方法：每次找到未被数组 nums 覆盖的最小的整数 xx，在数组中补充 xx，然后寻找下一个未被覆盖的最小的整数，重复上述步骤直到区间 [1,n][1,n] 中的所有数字都被覆盖
    # 时间复杂度：O(m+log n)
    # 空间复杂度：O(1)
    @classmethod
    def minPatchess_1(self, nums , n):
        furthest = index = ans =0
        while furthest < n:
            # 可覆盖到，直接用前缀更新区间
            if index < len(nums) and nums[index] <= furthest + 1:
                furthest += nums[index]
                index += 1
            # 不可覆盖到，增加一个数 further + 1， 并用前缀和更新区间
            else:
                furthest = 2*furthest + 1
                ans += 1
        return ans

    # 2. 其他
    # 核心逻辑：[0,x) 的若干个数加上 k，可扩大值域至 [0,x+k)，注意 k∈[0,x]。
    @classmethod
    def minPatchess_2(self, nums , n):
        max = 1
        index = need = 0
        while max <= n:
            if index < len(nums) and nums[index] <= max:
                max += nums[index]
                index = index+1
            else:
                max += max
                need += 1
        return need

def main( ):
    nums = [1,3]
    n = 6
    # nums = [1,5,10], n = 20  
    # nums = [1,2,2], n = 5
    a = Solution.minPatchess_2(nums, n)
    print(a)


main()
