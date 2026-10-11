# Users will have the following attributes: tweets, followers, and followings 
class Twitter:
 
    def __init__(self):
        self.users = defaultdict(list)
        self.followings = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        userIds = self.followings[userId] | {userId}
        for uid in userIds:
            if self.users[uid]:
                idx = len(self.users[uid]) - 1
                time, tweetId = self.users[uid][idx]

                heapq.heappush(heap, (time, tweetId, uid, idx))

        while heap and len(res) < 10:
            time, tweetId, uid, idx = heapq.heappop(heap)

            res.append(tweetId)
            if idx > 0:
                idx -= 1

                prevTime, prevTweetId = self.users[uid][idx]

                heapq.heappush(
                    heap,
                    (prevTime, prevTweetId, uid, idx)
                )
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)
