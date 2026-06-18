class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        count2 = defaultdict(int)
        for i in s:
            count[i] += 1
        for x in t:
            count2[x] += 1
        
        if count == count2:
            return True
        return False

        