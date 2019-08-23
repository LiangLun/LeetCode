'''
62. 不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28

'''
# 方法1：排列组合
# 从起点到终点一共需要m+n-2步，在m+n-2步选出m-1步向右，剩下n-1步则向下。即有C(m-1)(m+n+2)种选择
import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

# 方法2：动态规划
# 1.状态定义：DP[i][j]为到位置(i,j)的路径数
# 2.状态转移方程：DP[i][j]=DP[i-1][j]+DP[i][j-1]
# 时间复杂度O(m*n)，空间复杂度O(m*n)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                DP[i][j] = DP[i][j-1] + DP[i-1][j]
        return DP[-1][-1]
# 对上面的方法进行简单优化 
