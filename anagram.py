# Given two strings s and p, return an array of all the start indices of p's 
# anagrams
#  in s. You may return the answer in any order.

# example
# s = "cbaebabacd", p = "abc"
# 0.cba = abc
# 1.bae = abc
# 2.aeb = abc
# 3.eba = abc
# 4.bab = abc
# 5.aba = abc
# 6.bac = abc
# 7.acd = abc


# Solution

class Solution:
    def findAnagrams(self, s, p):
        arr = []
        p = sorted(p)
        for i in range(len(s) - len(p) + 1):
            subString = s[i:i+len(p)]
            if sorted(subString) == p:
                arr.append(i)
        return arr
            
obj = Solution()
print(obj.findAnagrams("cbaebabacd",'abc'))