# 链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

# 示例 1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

# 限制：
# 0 <= s 的长度 <= 10000

# 1. 遍历添加
# - 时间复杂度O（N），遍历list
# - 空间复杂度O（N），新建list
# class Solution:
#     @classmethod
#     def replaceSpace(self, s) -> str:
        # string = list(s)
        # for index, i in enumerate(string):
        #     if i == " ":
        #         string[index] = "%20"
        # return "".join(string)

        # res = []
        # for i in s:
        #     if i == " ": res.append("%20")
        #     else:res.append(i)
        # return "".join(res)



# 2. replace
# - 时间复杂度O（1）
# - 空间复杂度O（1）
# class Solution:
#     @classmethod
#     def replaceSpace(self, s) -> str:
#         return s.replace(" ", "%20")


# 3. split
# - 时间复杂度O（1）
# - 空间复杂度O（1）
class Solution:
    @classmethod
    def replaceSpace(self, s) -> str:
        split_str = str.split()
        





def main():
    string = "We are happy."
    final = Solution.replaceSpace(string)
    print(final)


if __name__ == "__main__":
    main()

