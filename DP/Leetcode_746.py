'''
746.使用最小花费爬楼梯
数组的每个索引做为一个阶梯，第i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为0 或 1 的元素作为初始阶梯。

示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
'''
# 动态规划
# 1.状态定义：DP[i]为第i步包括cost[i]的最小花费
# 2.状态转移方程：DP[0]=cost[0];DP[1]=cost[1];DP[i] = min(DP[i-1], DP[i-2] + cost[i])
# 时间复杂度O(n)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # DP[i]为第i步包括cost[i]的最小花费
        DP = cost
        for i in range(2, len(cost)):
            DP[i] = min(DP[i-1], DP[i-2] + cost[i])
        return min(DP[-1], DP[-2])


