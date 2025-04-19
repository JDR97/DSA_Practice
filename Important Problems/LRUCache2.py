from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.orderQ = deque()

    def get(self, key):
        if key in self.cache:
            self.orderQ.remove(key)
            self.orderQ.appendleft(key)
            return self.cache[key]
        else:
            return -1
        
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.orderQ.remove(key)
            self.orderQ.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:
                lru_item = self.orderQ.pop()
                del self.cache[lru_item]

            self.cache[key] = value
            self.orderQ.appendleft(key)



if __name__ == "__main__":
  
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))