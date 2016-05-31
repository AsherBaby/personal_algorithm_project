from collections import defaultdict


class Tweet:

    @classmethod
    def create(cls, user_id, tweet_text):
        return Tweet(user_id, tweet_text)

    def __init__(self, user_id, tweet_text):
        self.user_id = user_id
        self.tweet_text = tweet_text


class MiniTwitter:

    def __init__(self):
        self.tweets = defaultdict(list)  # user_id: [Tweet]
        self.followGraph = defaultdict(set)  # from_user_id: [to_user_id]
        self.internal_count = 0

    def postTweet(self, user_id, tweet_text):
        tweet = Tweet.create(user_id, tweet_text)
        self.tweets[user_id].append((self.internal_count, tweet))
        self.internal_count += 1
        return tweet

    def getNewsFeed(self, user_id):
        """
        Get the given user's most recently 10 tweets in his news feed (posted by his friends and himself).
        Order by timestamp from most recent to least recent.
        """
        tweets = self.tweets[user_id][-10:]
        for followee in self.followGraph[user_id]:
            tweets += self.tweets[followee][-10:]

        tweets.sort(key=lambda x: x[0])
        return map(
            lambda x: x[1],
            tweets[-1:-11:-1]
        )

    def getTimeline(self, user_id):
        """
        Get the given user's most recently 10 tweets posted by himself,
        order by timestamp from most recent to least recent.
        """
        return map(
            lambda x: x[1],
            self.tweets[user_id][-1:-11:-1]
        )

    def follow(self, from_user_id, to_user_id):
        self.followGraph[from_user_id].add(to_user_id)

    def unfollow(self, from_user_id, to_user_id):
        self.followGraph[from_user_id].remove(to_user_id)
