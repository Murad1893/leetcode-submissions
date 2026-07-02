from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Intuition: Expand window until freq match appears, then start shrinking and maintain min
        """

        if len(s) < len(t): return ""

        count_s = Counter()
        count_t = Counter(t)
        
        result = float('inf')
        result_idx = [None,None]

        l = 0
        
        for r in range(len(s)):
            
            if s[r] in count_t:
                count_s[s[r]] += 1

            while count_s >= count_t:
                if r-l+1 < result: # need if for min condition
                    result = r-l+1
                    result_idx = [l, r]
                if s[l] in count_s:
                    count_s[s[l]] -= 1
                l += 1           
                
        return s[result_idx[0]: result_idx[1]+1] if result_idx[0] is not None else ""
                
