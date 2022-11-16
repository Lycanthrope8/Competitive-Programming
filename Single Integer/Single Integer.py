# Link : https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=nums.count(i)
        for k,v in d.items():
            if v==1:
                return k

d=Solution()
print(d.singleNumber([4,1,2,1,2]))


import collections
class Solution1(object):
    def singleNumber(self, nums):
        c=Counter(nums)
        for k,v in c.items():
            if v==1:
                return k

