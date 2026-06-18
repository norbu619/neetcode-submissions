class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = "".join(i for i in s if i.isalnum())
        left = 0
        right = len(s) - 1
        for i in range(len(s)):
            if left >= right:
                break
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                print (left, right)
                return False    
        
        return True