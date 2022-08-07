# 链接：https://leetcode-cn.com/problems/positions-of-large-groups
# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
# 例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。
# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。

# 示例 1：
# 输入：s = "abbxxxxzzy"
# 输出：[[3,6]]
# 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。

# 示例 2：
# 输入：s = "abc"
# 输出：[]
# 解释："a","b" 和 "c" 均不是符合要求的较大分组。

# 示例 3：
# 输入：s = "abcdddeeeeaabbbcd"
# 输出：[[3,5],[6,9],[12,14]]
# 解释：较大分组为 "ddd", "eeee" 和 "bbb"

# 示例 4：
# 输入：s = "aba"
# 输出：[]
#  
# 提示：
# 1 <= s.length <= 1000
# s 仅含小写英文字母




class Solution(object):
    # 1. 暴力迭代法
    # 时间：O（n）
    # 空间：O（n）
    @classmethod
    def largeGroupPositions_1(self, s):
        res = [] 
        tmp = []
        for index in range(len(s)-1): 
            if s[index] == s[index+1]:
                tmp.append(index)
            else:
                tmp.append(index)
                if len(tmp) >= 3:
                    res.append([tmp[0], tmp[-1]])
                tmp = []
        return res  



    # 2. 一次遍历[官方]
    # 时间：O（n）
    # 空间：O（1）
    @classmethod
    def largeGroupPositions_2(self, s):
        res = []
        n, num = len(s), 1    # num表示前后 相同的个数
        for i in range(n):
            if i == n-1 or s[i] != s[i+1]:
                if num >= 3:
                    res.append([i-num+1, i])
                num = 1
            else:
                num += 1
        return res


def main():
    s = "abcdddeeeeaabbbcd"
    a = Solution.largeGroupPositions_2(s)
    print(a)


main()


