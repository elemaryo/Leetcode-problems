from heapq import *
from math import *


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda P: P[0]**2+P[1]**2)  # math.sqrt()
        return points[:K]


# Time Complexity: O(N log N) for sorting
# Space Complexity: O(N) for array space
        # Heap method:
#         maxHeap = []
#         origin = (0,0)
#         def getDistanceToOrigin(point):
#             return math.sqrt((origin[0] - point[0]**2) + (origin[1] - point[1]**2))

#         for p in points:
#             distance = getDistanceToOrigin(p)
#             # heap always has to stay size k
#             if len(maxHeap) < K:
#                 heappush(maxHeap, (-distance, p))
#             else:
#                 # if the distance in the heap is larger than the current smallest distance, replace it
#                 if abs(maxHeap[0][0]) > distance:
#                     heapreplace(maxHeap, (-distance, p))


#         ans = []
#         # add all points in heap which has all closest points based on -smallest distance
#         for p in maxHeap:
#             ans.append(p[1])

#         return ans
# Time Complexity: O(n-k) log k
# Space Complexity: O(n + k) size of output array + size of heap
# Videos: https://www.youtube.com/watch?v=yrXTRbM7j9Q&ab_channel=thecodingworld
# https://www.youtube.com/watch?v=eaYX0Ee0Kcg&ab_channel=CSDojo
# https://www.youtube.com/watch?v=1rEUgAG7f_c
