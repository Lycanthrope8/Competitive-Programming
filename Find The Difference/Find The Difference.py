# Link: https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if s.count(i) != t.count(i):
                return i
d=Solution()
d.findTheDifference('abcd','abcde')

