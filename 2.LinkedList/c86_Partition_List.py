# 链接：https://leetcode-cn.com/problems/partition-list
# 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。

# 示例：
# 输入：head = 1->4->3->2->5->2, x = 3
# 输出：1->2->2->4->3->5



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

class Solution:
    # 1. 模拟
    # 思路：
    # 时间：O（n） 其中 n 是原链表的长度。我们对该链表进行了一次遍历
    # 空间：O（1）
    @classmethod
    def partition_1(self, head, x):
        dummy1, dummy2 = ListNode(), ListNode()
        cur1,cur2, cur = dummy1, dummy2, head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        cur1.next, cur2.next = dummy2.next, None
        return dummy1.next




def main():
    head = ListNode(1)
    node1 = ListNode(4)
    node2 = ListNode(3)
    node3 = ListNode(2)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)
    head.next = node1
    node1.next = node2 
    node2.next = node3 
    node3.next = node4 
    node4.next = node5  
    node5.next = node6 
    x = 3
    final = Solution.partition_1(head, x)
    print(final)


if __name__ == "__main__":
    main()