class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.a = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.a.append(val)
        self.d[val] = len(self.a) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        index = self.d[val]

        self.a[index] = self.a[-1]
        self.d[self.a[-1]] = index

        self.a.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.a)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()