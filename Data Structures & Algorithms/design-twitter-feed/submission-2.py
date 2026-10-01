class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followMap[userId].copy()
        users.add(userId)

        heap = []
        for user in users:
            if not self.tweetMap[user]:
                continue
            index = len(self.tweetMap[user]) - 1
            time, tweetId = self.tweetMap[user][index]

            heapq.heappush(heap, (-time, tweetId, user, index))
        
        res = []
        while heap and len(res) < 10:
            _, tweetId, user, index = heapq.heappop(heap)
            res.append(tweetId)
            
            index -= 1
            if index >= 0:
                time, tweetId = self.tweetMap[user][index]
                heapq.heappush(heap, (-time, tweetId, user, index))

        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
