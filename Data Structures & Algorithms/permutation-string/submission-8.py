class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use matches 

        freq_s1 = [0] * 26
        freq_s2 = [0] * 26
        l = 0
        matches = 0

        if len(s2) < len(s1): return False

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1

        for i in range(len(freq_s1)):
            if freq_s1[i] == freq_s2[i]:
                matches += 1
            
        for r in range(len(s1), len(s2)): # already did the check above
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')

            freq_s2[index] += 1
            if freq_s1[index] == freq_s2[index]:
                matches += 1
            elif freq_s1[index] + 1 == freq_s2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            freq_s2[index] -= 1
            if freq_s1[index] == freq_s2[index]:
                matches += 1
            elif freq_s1[index] - 1 == freq_s2[index]:
                matches -= 1

            l += 1

        return matches == 26



