# Link : https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        dic={}
        for i in strs:
            j=sorted(i)
            j="".join(j)
            if j not in dic.keys():
                dic[j]=[i]
            else:
                dic[j].append(i)
        return dic.values()

d=Solution()
print(d.groupAnagrams(["a"]))
