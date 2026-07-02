class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        char_dict = defaultdict(int)
        l = 0
        result = 0

        for r in range(len(s)):
            char_dict[s[r]] += 1
            max_count = max(max_count, char_dict[s[r]])
            
            if (r - l + 1 ) - max_count > k:
                char_dict[s[l]] -= 1
                l += 1
                
            result = max(result, r - l + 1)

        return result
        