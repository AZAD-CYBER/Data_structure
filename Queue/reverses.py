# from queue import Queue

# def reverseQueueFirstKElements(k, Queue):
# 	if (Queue.empty() == True or
# 			k > Queue.qsize()):
# 		return
# 	if (k <= 0):
# 		return

# 	Stack = []
# 	for i in range(k):
# 		Stack.append(Queue.queue[0])
# 		Queue.get()

# 	while (len(Stack) != 0):
# 		Queue.put(Stack[-1])
# 		Stack.pop()

# 	for i in range(Queue.qsize() - k):
# 		Queue.put(Queue.queue[0])
# 		Queue.get()

# def Print(Queue):
# 	while (not Queue.empty()):
# 		print(Queue.queue[0], end=" ")
# 		Queue.get()


# Queue = Queue()
# Queue.put(10)
# Queue.put(20)
# Queue.put(30)
# Queue.put(40)
# Queue.put(50)
	
# k = 2
# reverseQueueFirstKElements(k, Queue)
# Print(Queue)

from collections import deque
def reverse(queue):
	Stack = []
	while (queue):
		Stack.append(queue[0])
		queue.popleft()

	while (len(Stack) != 0):
		queue.append(Stack[-1])
		Stack.pop()

queue=deque([10,20,30,40,50])
reverse(queue)
print(queue)