# 链接：https://leetcode-cn.com/problems/sliding-window-maximum
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回滑动窗口中的最大值。

#  

# 示例 1：
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# 示例 2：
# 输入：nums = [1], k = 1
# 输出：[1]

# 示例 3：
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]

# 示例 4：
# 输入：nums = [9,11], k = 2
# 输出：[11]

# 示例 5：
# 输入：nums = [4,-2], k = 2
# 输出：[4]
#  
# 提示：
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


import heapq

class Solution(object):

    # 1. 优先队列
    # 思路：使用小根堆，当
    @classmethod
    def maxSlidingWindow_1(self, nums, k):
        q = [(-nums[i], i) for i in range(k)]  # 起始nums的前k个
        heapq.heapify(q)

        ans = [-q[0][0]] # 取前k个元素的最大值
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i-k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans




    # def maxSlidingWindow_2(self, nums, k):


    # def maxSlidingWindow_3(self, nums, k):






def main( ):
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    a = Solution.maxSlidingWindow_1(nums, k)
    print(a)


main()
