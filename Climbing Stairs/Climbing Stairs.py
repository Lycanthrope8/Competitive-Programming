# Link: https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n):
        fib=[1,1]
        for i in range(n-1):
            fib.append(fib[i]+fib[i+1])
        return fib[-1]

c=Solution()
print(c.climbStairs(4))