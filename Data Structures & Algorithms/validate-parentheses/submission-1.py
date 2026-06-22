class Solution:
    def isValid(self, s: str) -> bool:
        # if valid then stack should be empty at the end
        stack = []

        for char in s:
            if char in "])}" and stack:
                if char == "}" and stack[-1] != "{" or char == "]" and stack[-1] != "[" or char == ")" and stack[-1] != "(":
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

        