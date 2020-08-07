# https://leetcode.com/problems/design-browser-history/submissions/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = -1

    def visit(self, url: str) -> None:
        if self.cur == -1:
            self.history.append(url)
            self.cur = -1
            print(self.history)
            print(self.cur)
        else:
            self.history = self.history[:self.cur+1]
            self.history.append(url)
            self.cur = -1
            print(self.history)
            print(self.cur)
        
    def back(self, steps: int) -> str:
        self.cur = self.cur - steps
        if -self.cur > len(self.history):
            self.cur = -len(self.history)
        print(self.history[self.cur])
        print(self.cur)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = self.cur + steps
        if self.cur > -1:
            self.cur = -1
        print(self.history[self.cur])
        print(self.cur)
        return self.history[self.cur]

bh = BrowserHistory('leetcode')
bh.visit('google')
bh.visit('facebook')
bh.visit('youtube')
bh.back(1)
bh.back(1)
bh.forward(1)
bh.visit('linkedin')
bh.forward(2)
bh.back(2)
bh.back(7)
