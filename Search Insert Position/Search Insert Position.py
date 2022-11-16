# Link: https://leetcode.com/problems/search-insert-position/
class Solution(object):
    def searchInsert(self, nums, target):
        counter=0
        i=0
        if nums[-1]<target:
            return len(nums)
        while nums[i]<target:
            i+=1
            counter+=1
        return counter