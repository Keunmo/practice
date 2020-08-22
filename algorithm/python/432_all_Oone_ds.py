class AllOne:

    def __init__(self):
        # data = {1:[]}   # {1:[a,b,c], 2:[d,e]}
        # datalist = {}   # {a:1, b:1}
        self.data = {}
        
        """
        Initialize your data structure here.
        """
        

    def inc(self, key: str) -> None:
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        

    def dec(self, key: str) -> None:
        if key in self.data:
            if self.data[key] == 1:
                del self.data[key]
            else:
                self.data[key] -= 1
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        stddata = sorted(self.data.items(), key=lambda x: x[1], reverse=True)
        if stddata == []:
            return ''
        return stddata[0][0]
        
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        stddata = sorted(self.data.items(), key=lambda x: x[1])
        if stddata == []:
            return ''
        return stddata[0][0]
        
# getMax, getMin is not O(1) time complex.

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
