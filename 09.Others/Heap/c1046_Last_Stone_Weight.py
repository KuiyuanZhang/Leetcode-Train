# 链接：https://leetcode-cn.com/problems/last-stone-weight
# 有一堆石头，每块石头的重量都是正整数。
# 每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

#  

# 示例：
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
# 再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
# 接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
# 最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
#  

# 提示：
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000




import heapq
from PythonStructure.Heap import  Heap

class Solution:
    # 1. 最大堆
    # 将所有石头的重量放入最大堆中,堆这个可以自动实现排序的数据结构，而且添加和删除一个元素的时间复杂度都是O(logn)
    # Python 只支持小顶堆
    # 时间复杂度：O(nlogn)，其中 n 是石头数量。每次从队列中取出元素需要花费 O(logn) 的时间，最多共需要粉碎 n−1 次石头。
    # 空间复杂度: O(n)
    @classmethod
    def lastStoneWeight_1(self, stones):
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x-y)
        if heap:return -heap[0]
        return 0

    # 2. 手写大顶堆
    @classmethod
    def lastStoneWeight_2(self, stones):
        # 初始化大顶堆
        heap = Heap(desc=True)
        for stone in stones:
            heap.push(stone)
        # 模拟
        while heap.size > 1:
            x,y = heap.pop(),heap.pop()
            if x != y:
                heap.push(x-y)
        if heap.size: return heap.heap[0]
        return 0


def main():
    stones = [2,7,4,1,8,1]
    result = Solution.lastStoneWeight_2(stones)
    print(result)


main()