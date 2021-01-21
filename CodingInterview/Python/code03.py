'''
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
  
限制：
2 <= n <= 100000
'''
class Solutions(object):
    # 1. 哈希法
    # - 空间换时间，对时间复杂度不要求的情况可以使用。
    # - 遍历整个数组,当这个数字没有出现过哈希表的时候将其加入进去,如果在哈希表中则直接返回即可
    # - 时间复杂度O(n)  遍历数组需要的时间
    # - 空间复杂度O(n)  存储数组需要的空间
    @classmethod
    def findRepeatNumber_1(self, nums):
        hash = dict()
        for num in nums:
            if hash.get(num):
                return num
            else:
                hash[num] = True

    # 2 . 排序
    # - 思路是将数组排好序,在查找重复数字,这个思路很简单
    # - 时间复杂度O(nlogn) ： python的sort方法默认排序为TimeSort，平均时间复杂度为O（nlogn），平均空间复杂度为O（n）
    # - 空间复杂度O(1)，pre
    @classmethod
    def findRepeatNumber_2(self, nums):
        nums.sort()
        pre = nums[0]
        for index in range(1, len(nums)):
            if pre == nums[index]:
                return pre
            pre = nums[index]

    # 3. 原地置换法
    # - 因为在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内，所以如果有数字重复，则对应的位置会对不上。
    # - 可以考虑把数和list[数]互换，如果
    # - 时间复杂度O(n)
    # - 空间复杂度O(1)
    @classmethod
    def findRepeatNumber_3(self, nums):
        for index, num in enumerate(nums):
            while index != num:
                if nums[num] == num: 
                    return num
                else:
                    nums[num] = num

    # 4. 暴力循环法
    # - 时间复杂度O（n^2）   双循环
    # - 空间复杂度O（1）     i和j为常数级
    @classmethod
    def findRepeatNumber_4(self, nums):
        for i in nums:
            for j in nums:
                if i == j:
                    return i
        size = len(nums)
        for i in range(size):
            for j in range(i, size)
                if nums[i] == nums[j]:return nums[i]



def main():
    nums = [2, 3, 1, 0, 2, 5, 3]
    final = Solutions.findRepeatNumber_1(nums)
    print(final)


if __name__ == "__main__":
    main()