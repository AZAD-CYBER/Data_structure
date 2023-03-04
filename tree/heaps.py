'''
Heap is a special tree structure in which each parent node is less than or equal to its child node. Then it is called a Min Heap. If each parent node is greater than or equal to its child node then it is called a max heap. It is very useful is implementing priority queues where the queue item with higher weightage is given more priority in processing.

'''

import heapq

H=[21,1,45,78,3,5]
#use heapify to rearrange the elements
heapq.heapify(H)
print(H)
#add element
heapq.heappush(H,8)
print(H)
#remove element from the heap (smallest one )
heapq.heappop(H)
print(H)
#replace an element
heapq.heapreplace(H,6)

print(H)

