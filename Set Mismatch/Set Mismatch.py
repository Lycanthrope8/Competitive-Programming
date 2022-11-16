# Link: https://leetcode.com/problems/set-mismatch/
class Solution(object):
    def findErrorNums(self, nums):
        c=Counter(nums)
        result=[0,0]
        # print(c)
        for i in range(1,len(nums)+1):
            # print(c[i])
            if c[i]==2:
                result[0]=i
            if c[i]==0:
                result[1]=i
        return result