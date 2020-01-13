class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        # self.queue = []
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        value = self.cache[key]
        self.cache.pop(key)
        self.cache.update({key: value})
        return self.cache[key]
#         if key not in self.queue:
#             return -1
        
#         index = self.queue.index(key)
#         del self.queue[index]
#         self.queue.append(key)
#         return self.cache[key]
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            
        elif self.capacity == len(self.cache):
            keys = list(self.cache.keys())
            self.cache.pop(keys[0])
            
        self.cache.update({key: value})    
            
            
#         if key in self.queue:           
#             index = self.queue.index(key)
#             del self.queue[index]
        
#         elif self.capacity == len(self.queue):
#             self.queue.pop(0)

        
#         self.queue.append(key)
#         self.cache[key] = value
            
     #O(n) time
     #O(2n) space
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# import collections
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = collections.OrderedDict()
#         self.capacity = capacity
        
        

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#             return self.cache[key]
        
#         return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key not in self.cache:
#             if len(self.cache) == self.capacity:
#                 self.cache.popitem(last=False)
        
#         else:
#             del self.cache[key]
            
#         self.cache[key] = value
        
        


