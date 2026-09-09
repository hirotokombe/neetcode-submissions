class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # user sees their own tweets + people they follow
        users = set(self.followMap[userId])
        users.add(userId)

        # put each user's newest tweet into the heap
        for user in users:
            if self.tweetMap[user]:
                index = len(self.tweetMap[user]) - 1
                time, tweetId = self.tweetMap[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        # get at most 10 newest tweets
        while heap and len(res) < 10:
            negTime, tweetId, user, index = heapq.heappop(heap)

            res.append(tweetId)

            # move to this user's next older tweet
            index -= 1

            if index >= 0:
                time, tweetId = self.tweetMap[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
