"""链接：https://leetcode-cn.com/problems/binary-prefix-divisible-by-5
给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。
 
示例 1：
输入：[0,1,1]
输出：[true,false,false]
解释：
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。

示例 2：
输入：[1,1,1]
输出：[false,false,false]

示例 3：
输入：[0,1,1,1,1,1]
输出：[true,false,false,false,true,false]

示例 4：
输入：[1,1,1,0,1]
输出：[false,false,false,false,false]

提示：
1 <= A.length <= 30000
A[i] 为 0 或 1
"""
class Solution(object):
    # 1. 暴力+二进制+数组
    # 思路： 判断每个二进制前缀是否被five整除
    @classmethode
    def prefixesDivBy5_1(self, A):
        return [not int("".join(map(str, A[:i])), 2)%5 for i in range(1, len(A)+1)]

    # 2. 暴力+二进制+数组 (优化)
    # 思路： 判断每个二进制前缀是否被five整除，用变量保存当前二进制前缀
    @classmethode
    def prefixesDivBy5_2(self, A):
        a = ""
        res = []
        for i in A:
            a += str(i)
            res.append(not int(a, 2)%5)
        return res

    # 3. 二进制+数组+位运算
    # 思路： 利用变量保存当前二进制前缀的值，每次判断是否被5整除，改变保存当前二进制前缀的值的变量并对5取余。
    # 二进制增加：先将前面的数乘2，再加上新增数。
    # 取余原因：  因为n*2%5 == n%5*2%5，所以取余，这样就不用保存非常大的数了。
    @classmethode
    def prefixesDivBy5_3(self, A):
        res = []
        pre = 0
        for i in A:
            pre = (pre<<1)+i
            res.append(not pre%5)
        return res

def main():
    A = [0,1,1]
    a = Solution.prefixesDivBy5_1(A)
    print(a)
