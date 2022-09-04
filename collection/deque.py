from collections import deque

if __name__ == "__main__":
    nums = [1, 2]
    queue = deque(nums)
    print(list(queue))

    queue.append(3)
    print(list(queue))
    
    queue.appendleft(0)
    print(list(queue))

    queue.popleft()
    print(list(queue))
    
    queue.pop()
    print(list(queue))
