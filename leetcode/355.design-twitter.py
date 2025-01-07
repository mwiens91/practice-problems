# @leet start
class Twitter:
    def __init__(self):
        # For each user, we have a set of followers
        self.following_dict: dict[int, set[int]] = {}

        # We'll keep tweets in a list. The order will be in from oldest
        # to newest. Each element will be a two-tuple containing the
        # user and the tweet.
        self.tweets: list[tuple[int, int]] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        MAX_TWEETS_IN_FEED = 10

        # Get set of IDs (including self) user is following
        following_set = {userId}

        try:
            following_set |= self.following_dict[userId]
        except KeyError:
            pass

        # Build up the news feed
        news_feed = []

        for poster_id, tweet_id in reversed(self.tweets):
            if poster_id in following_set:
                news_feed.append(tweet_id)

            if len(news_feed) >= MAX_TWEETS_IN_FEED:
                break

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        try:
            self.following_dict[followerId].add(followeeId)
        except KeyError:
            self.following_dict[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.following_dict[followerId].remove(followeeId)
        except KeyError:
            pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @leet end
