# Link: https://leetcode.com/problems/continuous-subarray-sum/
# Solution : https://www.youtube.com/watch?v=OKcrLfR-8mE

class Solution(object):
    def checkSubarraySum(self, nums, k):
        rem={0:-1}
        total=0
        for i,e in enumerate(nums):
            total+=e
            r=total%k
            if r not in rem:
                rem[r]=i
            elif i-rem[r]>1:
                return True
        return False

d=Solution()
print(d.checkSubarraySum([23,2,4,6,7],6))