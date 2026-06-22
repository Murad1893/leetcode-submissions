class Solution:
    def isPalindrome(self, s: str) -> bool:
        # implementing own alphanumeric function
        # def isalnum(char):
        #     return ord('A') <= ord(char) <= ord('Z') or \
        #     ord('a') <= ord(char) <= ord('z') or \
        #     ord('0') <= ord(char) <= ord('9')
        
        l, r = 0, len(s) - 1
        s = s.lower()
        while l < r:
            # use while loops to ignore punctuation
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r-=1
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True
        