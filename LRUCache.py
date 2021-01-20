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

     # O(n) time
     # O(2n) space


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


# class DoubleLinkedNode:
#     def __init__(self, key, val: int):
#         self.val = val
#         self.key = key
#         self.prev = None
#         self.next = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.keyMap = {}
#         self.lru = None # least recently used
#         self.mru = None # most recently used

#     def promote(self, key):
#         if self.capacity == 1 or self.mru == self.keyMap[key]:
#             return

#         cur = self.keyMap[key]
#         prevMru = self.mru

#         prev = cur.prev
#         nxt = cur.next

#         if prev is None: # the node was lru
#             self.lru = nxt
#             nxt.prev = None
#         else: # mid node
#             prev.next = nxt # remove from cur pos
#             nxt.prev = prev

#         prevMru.next = cur
#         cur.prev = prevMru
#         cur.next = None

#         self.mru = cur


#     def evictLRU(self):
#         if len(self.keyMap) == 1:
#             lruKey = self.lru.key
#             del self.keyMap[lruKey]
#             return
#         nextLru = self.lru.next
#         lruKey = self.lru.key
#         del self.keyMap[lruKey]
#         self.lru = nextLru
#         nextLru.prev = None


#     def get(self, key: int) -> int:
#         # case 1.
#         #         add to the linkedin list
#         #         LRU item stays the same
#         # case 2. capacity is full
#         #         evict LRU and update new LRU


#         if key not in self.keyMap:
#             return -1

#         self.promote(key) # promote it to MRU
#         return self.keyMap[key].val


#     def put(self, key: int, value: int) -> None:
#         # case 1. capacity is not full
#         #         add to the linkedin list
#         #         LRU item stays the same
#         # case 2. capacity is full
#         #         evict LRU and update new LRU
#         #
#         if key in self.keyMap:
#             node = self.keyMap[key]
#             node.val = value
#             self.promote(key)
#         else:
#             new = DoubleLinkedNode(key, value)
#             if len(self.keyMap) == self.capacity:
#                 self.evictLRU()
#             if len(self.keyMap) == 0:
#                 self.lru = new

#             self.keyMap[key] = new
#             lastMru = self.mru
#             if lastMru:
#                 lastMru.next = new
#             self.mru = new
#             new.prev = lastMru
