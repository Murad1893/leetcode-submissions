class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs: # O(n)
            result += str(len(s)) + "#" + s # this is O(m)
        
        return result
                
    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        length = ""
        result = []
        
        while i < len(s): # O(n)
            j = i
            
            while s[j] != "#":
                # traverse up until delimiter
                j += 1
            # use slicing instead of appending
            length = int(s[i:j])
            j += 1 # to move past delimiter
            result.append(s[j:j+length]) # append the string up until length of chars - O(m)
            i = j + length # increment i to the next length

        return result