from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def build_char_map(s):
            char_freq = [0] * 26
            for char in s:
                diff = ord(char) - ord('a')
                char_freq[diff] += 1
            return char_freq

        str_map = defaultdict(list)
        
        for s in strs:
            # we made tuple here as keys can be immutable only
            str_map[tuple(build_char_map(s))].append(s)
        
        return list(str_map.values())