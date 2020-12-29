# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请
# 完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 示例:
# 现有矩阵 matrix 如下：
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
# 给定 target = 20，返回 false。

# 限制：
# 0 <= n <= 1000
# 0 <= m <= 1000



# 1. 暴力破解法
# - 时间复杂度O(n*m)   二维数组的大小
# - 空间复杂度O(1)
# class Solution(object):
#     @classmethod
#     def findNumberIn2DArray(self, matrix, target) -> bool:
#         for row in matrix:
#             for column in row:
#                 if column == target:
#                     return True
#         return False
        

# 2. 线性查找
# - 思路
#   - 选左上角，往右走和往下走都增大，不能选
#   - 选右下角，往上走和往左走都减小，不能选
#   - 选左下角，往右走增大，往上走减小，可选
#   - 选右上角，往下走增大，往左走减小，可选
# - 时间复杂度O(M+N)，其中，N和M分别为矩阵行数和列数，此算法最多循环 M+N 次。
# - 空间复杂度O(1), i,j指针使用常熟大小额外空间

# class Solution(object):
#     @classmethod
#     def findNumberIn2DArray(self, matrix, target) -> bool:
#         row, col = 0, len(matrix[0])-1
#         while row <= len(matrix)-1 and col >= 0:
#             if matrix[row][col] > target:
#                 col -= 1
#             elif matrix[row][col] < target:
#                 row += 1
#             else:
#                 return True
#         return False
            






# 3. 二分查找
# - 从方法2的线性查找变成2分查找，以确定取区域，步长不再是1
class Solution(object):
    @classmethod
    def findNumberIn2DArray(self, matrix, target) -> bool:
        def binary_search(self, matrix, target, vertical):
            low = start
            high = len()



# 4. 递归





def main():
    dic = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
    ]
    final = Solution.findNumberIn2DArray(dic, 5)
    print(final)


if __name__ == "__main__":
    main()