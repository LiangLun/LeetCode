'''
300. 最长上升子序列
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''

# DP法, 时间复杂度O(n^2)
# 1.定义状态。DP[i]为以nums[i]结束的最长上升子序列
# 2.状态转移方程。DP[i] = max{DP[i], DP[j]+1 if j<i and num[j]<num[i]}
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        DP = [1 for _ in range(len(nums))]
        res = 1
        for i in range(1, len(nums)):
        	# nums[i]要与前面的数都进行比较
        	for j in range(i):
        		# 状态转移方程，更新DP[i]
        		if nums[i] > nums[j]:
        			DP[i] = max(DP[i], DP[j]+1)
        	# 遍历DP中的每个值，取最大值
        	res = max(res, DP[i])
        return res

# 二分法
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 循环终止条件
        if not nums:
        	return 0
        