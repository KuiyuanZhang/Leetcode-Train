"""链接：https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。


示例 1：
输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true

示例 2：
输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false
 
提示：
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates 中不含重复的点
"""

class Solution:
    
    # 1. 根据三点之间的斜率计算 
    # 时间 O（n）
    # 空间 O（1）
    @classmethod 
    def checkStraightLine_1(self, coordinates):
        for i in range(len(coordinates)-2):
            y_1 = coordinates[i+1][1] - coordinates[i][1]
            y_2 = coordinates[i+2][1] - coordinates[i+1][1]
            x_1 = coordinates[i+1][0] - coordinates[i][0]
            x_2 = coordinates[i+2][0] - coordinates[i+1][0]
            if y_1*x_2 != x_1*y_2:
                return False
                break
        return True

    # 
            




def main():
    # coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    # coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    coordinates = [[0,0],[0,5],[5,5],[5,0]]
    a = Solution.checkStraightLine_1(coordinates)
    print(a)

main()