class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.has_one = defaultdict(int)

    def add(self, number: int) -> None:
        orig = self.freq[number]
        self.freq[number] += 1
        if orig:
            self.has_one[orig] -= 1
        self.has_one[self.freq[number]] += 1
    def deleteOne(self, number: int) -> None:
        orig = self.freq[number]
        if self.freq[number]:
            self.freq[number] -= 1
        if orig:
            self.has_one[orig] -= 1
        self.has_one[self.freq[number]] += 1
    def hasFrequency(self, frequency: int) -> bool:

        return bool(self.has_one[frequency])

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)