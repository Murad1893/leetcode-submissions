class MinStack:
    """
    Intuition:
    2 x val - prev_min = new_val | and not | val - min_val
    Why? 
        this and not val - prev_min. Because to know top is encoded, top < min_value
        This breaks if -3 -> -5, because top becomes -3 + 5 -> 2 and hence the next time you pop
        you don't know if 2 was encoded or not!

    val < prev_min
    val - prev_min < 0
    val + (val-prev_min) < val
    2.val - prev_min < val
    """


    def __init__(self):
        self.stack = []
        self.min_value = None 

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_value = val
            self.stack.append(val)
        else:
            if val < self.min_value:
                self.stack.append(2 * val - self.min_value)
                self.min_value = val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < self.min_value:
            self.min_value = 2 * self.min_value - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top < self.min_value:
            return self.min_value
        return top

    def getMin(self) -> int:
        return self.min_value
