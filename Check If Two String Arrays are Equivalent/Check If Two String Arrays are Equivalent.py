# Link : https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        res1=''
        res2=''
        for i in word1:
            res1+=i
        for i in word2:
            res2+=i
        if sorted(res1)==sorted(res2):
            return True
        return False

class Solution2(object):
    def arrayStringsAreEqual(self, word1, word2):
        return ''.join(word1)==''.join(word2)
d=Solution2()
print(d.arrayStringsAreEqual(["a", "cb"],["ab", "c"]))