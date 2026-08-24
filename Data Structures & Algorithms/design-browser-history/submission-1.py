class BrowserURL:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = BrowserURL(homepage)
        self.currentIndex = self.head

    def visit(self, url: str) -> None:
        newURL = BrowserURL(url)

        newURL.prev = self.currentIndex
        newURL.next = None
        self.currentIndex.next = newURL
        self.currentIndex = newURL
     

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.currentIndex.prev == None:
                break
            self.currentIndex = self.currentIndex.prev
            steps -= 1
        return self.currentIndex.url

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.currentIndex.next == None:
                break
            self.currentIndex = self.currentIndex.next
            steps -= 1
        return self.currentIndex.url
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)