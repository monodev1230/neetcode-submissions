class FreqStack:

    def __init__(self):
        self.counts = {}
        self.maxFreq = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        valCount = self.counts.get(val, 0) + 1
        self.counts[val] = valCount
        if valCount > self.maxFreq:
            self.maxFreq = valCount
        if valCount not in self.stacks:
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxFreq].pop()
        self.counts[res] -= 1
        if len(self.stacks[self.maxFreq]) == 0:
            del self.stacks[self.maxFreq]
            self.maxFreq -= 1
        return res
