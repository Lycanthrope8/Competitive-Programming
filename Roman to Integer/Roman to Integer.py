# Link : https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        intRom={"I":1,

                "IV":4,

                "V":5,

                "IX":9,

                "X":10,

                "XL":40,

                "L":50,

                "XC":90,

                "C":100,

                "CD":400,

                "D":500,

                "CM":900,

                "M":1000}
        ans=0
        out=[]
        condition=["IV","IX","XL","XC","CD","CM"]
        for i in condition:
            if i in s:
                out.append(i)
                s=s.replace(str(i),"")
        for i in s:
            out.append(i)
            s.replace(i,"")
        # print(out)
        for i in out:
            for k,v in intRom.items():
                if i==k:
                    ans+=v
        return ans





