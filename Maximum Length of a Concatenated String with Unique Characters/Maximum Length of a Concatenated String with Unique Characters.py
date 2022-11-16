# Link: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
class Solution:
    def maxLength(self, arr):
        unique=['']
        max_len=0
        for i in arr:
            if len(arr)==len(set(arr)):
                for j in unique:
                    temp=i+j
                    if len(temp)!=len(set(temp)):
                        continue
                    unique.append(temp)
        for i in unique:
            if len(i)>max_len:
                max_len=len(i)
        return max_len
d=Solution()
print(d.maxLength(["un","iq","ue"]))


