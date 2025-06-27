# from collections import deque

def timeRequiredToBuy(tickets,k):
    queue = []
    time = 0

    for i in range(len(tickets)):
        queue.append(i)

    while queue:
        index = queue.pop(0)
        tickets[index] -= 1
        time += 1

        if tickets[index] == 0 and index == k:
            return time
        if tickets[index] > 0:
            queue.append(index)

    return time

tickets = [2,3,2]
k = 2
print(timeRequiredToBuy(tickets,k))