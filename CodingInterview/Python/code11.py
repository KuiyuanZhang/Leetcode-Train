"""
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0
"""
class Solution:
    # 1. 二分查找 - 双指针
    # 步骤： 1， 初始化左右两端的指针。
    #       2. 如果中间位置大于右侧，则最小数一定在中间到右端之间，左侧等于中间+1，
    #          如果中间位置小于右侧，则...
    #          如果中间等于左右任一个，则右侧-1
    # 时间复杂度：O（logN）
    # 空间复杂度：O（1）
    @classmethod
    def minArray(self, numbers):
        low, high = 0, len(numbers) - 1 
        while low < high:
            minu =  (low+high) // 2
            if numbers[minu] > numbers[high]:
                low = minu + 1
            elif numbers[minu] < numbers[high]:
                high = minu
            else:
                high -= 1
        return numbers[low]

def main():
    numbers =  [3,4,5,1,2]
    a = Solution.minArray(numbers)
    print(a)
main()