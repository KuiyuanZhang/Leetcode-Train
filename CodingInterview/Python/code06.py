# 链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

# 示例 1：
# 输入：head = [1,3,2]
# 输出：[2,3,1]
# 限制：
# 0 <= 链表长度 <= 10000

#先定一个node的类
class ListNode(object):                  # value + next
    def __init__ (self, value = None, next = None):
        self.val = value
        self.next = next



# 1. 递归法
# 递推阶段： 每次传入 head.next ，以 head == None（即走过链表尾部节点）为递归终止条件，此时返回空列表 [] 。
# 回溯阶段： 利用 Python 语言特性，递归回溯时每次返回 当前 list + 当前节点值 [head.val] ，即可实现节点的倒序输出。
# - 时间复杂度 O(N)
# - 空间复杂度 O(N)

# class Solution(object):
#     @classmethod
#     def reversePrint(self, head):
#         return self.reversePrint(head.next) + [head.val] if head else []



# 2. 辅助栈法
# - 时间复杂度O（N）
# - 空间复杂度O（N）

# class Solution(object):
#     @classmethod
#     def reversePrint(self, head):
#         stack = []
#         while head:
#             print(head.val)
#             stack.insert(0, head.val)
#             head = head.next
#         return stack

        # while head:
        #     print(head.val)
        #     stack.append(head.val)
        #     head = head.next
        # return stack[::-1]

# 3. 反转链表法【最优】
# - 从头到尾遍历，指针调换下即可
# - 时间复杂度O（N）
# - 空间复杂度O（N）
# class Solution(object):
#     @classmethod
    def reversePrint(self, head):
        rev, p = None, head
        while p:
            rev, rev.next, p = p, rev, p.next
        stack = []
        while rev:
            stack.append(rev.val)
            rev = rev.next
        return stack




def main():

    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3 

    final = Solution.reversePrint(node1)
    print(final)


if __name__ == "__main__":
    main()




"""
class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

"""
