# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class User(object):
    def __init__(self):
        self.messages = []
        self.follows = set()


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # m key: user id  value: user follows is a list object
        self.m = {}
        self.t = 1

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        user = self.m.get(userId, None)
        if not user:
            user = User()
            user.messages.append([self.t, tweetId])
            self.m[userId] = user
        else:
            user.messages.append([self.t, tweetId])
        self.t -= 1


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        user = self.m.get(userId, None)
        if not user:
            return []
        else:
            ret = [x for x in user.messages]
            for follow in user.follows:
                followee = self.m.get(follow, None)
                if followee:
                    ret.extend(followee.messages)
            return [x[1] for x in sorted(ret)[:10]]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            user = self.m.get(followerId)
            if user:
                user.follows.add(followeeId)
            else:
                user = User()
                user.follows.add(followeeId)
                self.m[followerId] = user

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId:
            return
        user = self.m.get(followerId, None)
        if user:
            if followeeId in user.follows:
                user.follows.remove(followeeId)

def main():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))



if __name__ == "__main__":
    main()
