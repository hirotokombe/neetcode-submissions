class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque([])
        heap = []

        taskCount = [0] * 26

        for task in tasks:
             taskCount[ord(task) - ord('A')] += 1
            
        for task in taskCount:
            if task >  0:
                heapq.heappush(heap, -task)
        
        time = 0
        while heap or queue:
            if queue:
                queueItem = queue[0]
                if queueItem[1] <= time:
                    heapq.heappush(heap, -queue.popleft()[0])
            if heap:
                task = -heapq.heappop(heap)
                task -= 1
                if task > 0:
                    queue.append((task, time + n + 1))
        

            
            time+=1
        
        return time
