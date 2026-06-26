class Twitter:

    def __init__(self):
        # whom all a given user follows
        self.followers = defaultdict(set)
        # whom all follow a given user
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)
        self.c = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        #heapq.heappush(self.tweets[userId], -tweetId)
        self.tweets[userId].append((self.c, tweetId))
        self.c -= 1
        print("posted tweet: " + str(self.tweets[userId]) + "\n")
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = list(self.tweets[userId])
        print("followers map: " + str(self.followers))
        print("followees map: " + str(self.followees))
        print("tweets: " + str(self.tweets))
        for follower in self.followees[userId]:
            print("follower: " + str(follower) + ", tweets: " + str(self.tweets[follower]))
            t = self.tweets[follower]
            tweets.extend(t)
        heapq.heapify(tweets)
        print("heapified tweets: ", tweets)
        feed = []
        feedLength = 10
        while len(tweets) > 0 and len(feed) < feedLength:
            feed.append(abs(heapq.heappop(tweets)[1]))
        print()
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers[followeeId].add(followerId)
        self.followees[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
        return

