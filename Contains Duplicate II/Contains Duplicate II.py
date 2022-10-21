# Link:https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp={}
        for i in range(len(nums)):
            if nums[i] in temp and abs(temp[nums[i]]-i)<=k:
                return True
            temp[nums[i]]=i
        return False




