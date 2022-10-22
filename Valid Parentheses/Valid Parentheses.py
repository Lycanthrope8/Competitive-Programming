##Link: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        stack=[]
        dic={'(':')',
             '{':'}',
             '[':']'}
        for i in s:
            if i in dic.keys():
                stack.append(dic[i])
                # print(stack)
            elif stack==[] or i!=stack[-1]:
                ##if stack is empty and one closing bracket comes
                ##it means that bracket isn't opened yet
                return False
            else:
                stack.pop()
        return stack==[]
###This is alternate easy code
    def AltisValid(self, s):
        for x in range((len(s) // 2) + 1):
            if s == '':
                return True
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return False