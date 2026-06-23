import operator

class Solution:
    # truncated towards zero mean towards -inf -> 0 (drop the decimal part)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for token in tokens:
            if token in operator_map:
                n1, n2 = int(stack.pop()), int(stack.pop())
                operation = operator_map.get(token)
                stack.append(operation(n2, n1))
            else:
                stack.append(token)

        return int(stack.pop())