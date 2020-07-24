# https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.recent = [] # queue of key

    def get(self, key: int) -> int:
        print('get',key)
        print(self.cache)
        #return value
        if key in self.cache:
            self.recent.remove(key)
            self.recent.insert(0,key)
            print(self.cache)
            print(self.recent)
            return self.cache[key]
        else:
            print(self.cache)
            print(self.recent)
            return -1

    def put(self, key: int, value: int) -> None:
        print('put',key,value)
        if key in self.cache:
            self.cache[key] = value
            self.recent.remove(key)
            self.recent.insert(0,key)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.recent.pop()]
            self.cache[key] = value
            self.recent.insert(0,key)
        print(self.cache)
        print(self.recent)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

lc = LRUCache(2)
lc.put(1,1)
lc.put(2,2)
lc.get(1)
lc.put(3,3)
lc.get(2)
lc.put(4,4)
lc.get(1)
lc.get(3)
lc.get(4)