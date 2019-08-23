'''
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1
'''

# 二分法
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or nums[0] == target:
        	return 0
        if target > nums[-1]:
        	return len(nums)
        # 最左和右边元素的下标
        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
        	mid = left + (right - left) // 2
        	if nums[mid] == target:
        		return mid
        	elif nums[mid] > target:
        		right = mid - 1
        	else:
        		left = mid + 1
        return left