class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.x = self.head
    def visit(self, url: str) -> None:
        new = Node(url)
        self.x.next = new
        new.prev = self.x
        self.x  = new


    def back(self, steps: int) -> str:
        while self.x != self.head and steps > 0:
            self.x = self.x.prev
            steps -= 1
        return self.x.val

    def forward(self, steps: int) -> str:
        while self.x.next and steps > 0:
            self.x = self.x.next
            steps -= 1
        return self.x.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)