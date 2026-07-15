class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        i = -1
        while i >= -len(self.stack):
            if self.stack[i] <= price:
                count +=1
            else:
                break
            i -= 1
        self.stack.append(price)
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)