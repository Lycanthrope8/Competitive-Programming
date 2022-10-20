# Link : https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


ans=Solution()
print(ans.twoSum(nums=[3,2,4],target=6))