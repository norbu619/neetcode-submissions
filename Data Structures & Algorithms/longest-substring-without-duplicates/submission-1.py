class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        count = 0
        left = 0
        right = 0

        for i in s:
            if i not in res:
                res.append(i)
            else:
                if len(res) > count:
                    count = len(res)
                
                # Keep the part of the current substring after the first occurrence of the duplicate
                res = res[res.index(i) + 1:]
                res.append(i)
        
        if len(res) > count:
            count = len(res)

        return count