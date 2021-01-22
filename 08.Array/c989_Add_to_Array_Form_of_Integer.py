"""
https://leetcode-cn.com/problems/add-to-array-form-of-integer/
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

示例 1：
输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234

示例 2：
输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455

示例 3：
输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021

示例 4：
输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000
 

提示：
1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
如果 A.length > 1，那么 A[0] != 0"""


class Solution:

    # 1. 暴力破解
    # 思路： A数组转化为数字，+K, 再转回数组
    # 时间复杂度：O（n）
    # 空间复杂度：O（1）
    @classmethod
    def addToArrayForm(self, A, K):
        num = 0
        for i in range(len(A)):
            num += A[-i-1] * 10**i
        res = num + K
        return list(str(res))

    # 2. 从最后一位，每次递加
    # 思路：根据K的位数，只进行单位相加，满10 进1
    # 时间复杂度：O（n）
    # 空间复杂度：O（n）
    @classmethod
    def addToArrayForm(self, A, K):
        k = list(str(K))
        res = [0 for i in range(len(A))]
        jin = 0
        for i in range(len(A)):
            if i < len(k):
                tmp = A[-i-1] +  int(k[-i-1]) + jin
                jin = 0
                res[-i-1] = tmp%10
                if tmp > 10:
                    jin = 1
            else:
                res[-i-1] = A[-i-1]
        return res
            

def main():
    A = [1,2,0,0]
    K = 34
    a = Solution.addToArrayForm(A, K)
    print(a)


main()
