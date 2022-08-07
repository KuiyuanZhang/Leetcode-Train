# 
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
# 示例1
# 输入: "()"
# 输出: true
# 示例2
# 输入: "()[]{}"
# 输出: true
# 示例3
# 输入: "(]"
# 输出: false
# 示例4
# 输入: "([)]"
# 输出: false
# 示例5
# 输入: "{[]}"
# 输出: true


class Solution(object):
    # 1. 栈
    # 思路： 用栈从左向右存储括号，当出现右括号时，判断左边是否为对应的括号。
    @classmethod
    def isValid_1(self, s):
        stack = []
        mapping =  {'(': ')', '{': '}', '[': ']', '#': '$'}
        for char in s:
            if char not in mapping:   # 右括号 与 左括号是否对应
                top_element = stack.pop()  if stack  else "#"   # 取左括号或取为#号
                if mapping[top_element] != char:
                    return False
            else:
                stack.append(char)    # 左括号存入数组
        return not  stack

def main():
    s = "()[]{}"
    a = Solution.isValid_1(s)
    print(a)

main()
