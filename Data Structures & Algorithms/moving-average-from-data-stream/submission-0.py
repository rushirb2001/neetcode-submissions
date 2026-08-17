class MovingAverage:

    def __init__(self, size: int):
        self.moving_sum = []
        self.size = size

    def next(self, val: int) -> float:
        if len(self.moving_sum) < self.size:
            self.moving_sum.append(val)
        else:
            self.moving_sum = self.moving_sum[1:]
            self.moving_sum.append(val)

        return sum(self.moving_sum) / len(self.moving_sum)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
