# https://leetcode.com/problems/design-twitter/

import time
class Twitter:

    def __init__(self, usernum=1, usermat=[], tweet = [0,time.time()]):
        self.usernum = usernum
        self.tweet = tweet
        self.usermat = [[[]]]
        """
        Initialize your data structure here.
        """

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        #add user
        if self.usernum < userId:
            print('expand U.M.')
            added = userId-self.usernum
            self.usernum = userId
            for i in self.usermat:
                i += [[]]*added
            for i in range(added):
                self.usermat.append([[]] * self.usernum)
            print('U.M', self.usermat)
            
        #add tweet
        self.usermat[userId-1][userId-1].insert(0,{time.time():tweetId})
        print('U.M', self.usermat)
        
        
    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        #add user
        if self.usernum < userId:
            print('expand U.M.')
            added = userId-self.usernum
            self.usernum = userId
            for i in self.usermat:
                i += [[]]*added
            for i in range(added):
                self.usermat.append([[]] * self.usernum)
            print('U.M', self.usermat)

        print('U.M', self.usermat)
        nf = {}
        nfcontents = []
        for i in self.usermat[userId-1]:
            for j in i:
                nf.update(j)
        timesort = list(nf.keys())
        timesort.sort()
        timesort.reverse()
        if len(timesort) > 10:
            timesort = timesort[0:10]
        for i in timesort:
            nfcontents.append(nf[i])
        print('nfcon',nfcontents)
        return nfcontents
            

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # add user
        if self.usernum < max(followerId, followeeId):
            print('expand U.M.')
            added = max(followerId, followeeId)-self.usernum
            self.usernum = max(followerId, followeeId)
            for i in self.usermat:
                i += [[]]*added
            for i in range(added):
                self.usermat.append([[]] * self.usernum)
            print('U.M', self.usermat)

        self.usermat[followerId-1][followeeId-1] = self.usermat[followeeId-1][followeeId-1]
        print('U.M', self.usermat)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # add user
        if self.usernum < max(followerId, followeeId):
            newusernum = max(followerId, followeeId)
            added = newusernum-self.usernum
            self.usernum = newusernum
            for i in self.usermat:
                i += [[]]*added
            for i in range(added):
                self.usermat.append([[]] * self.usernum)
        if followerId == followeeId:
            return None
        self.usermat[followerId-1][followeeId-1] = []
        print('U.M', self.usermat)


twt = Twitter()
# twt.postTweet(1,1)
# twt.postTweet(1,2)
# twt.postTweet(1,3)
# twt.postTweet(1,4)
# twt.postTweet(1,5)
# twt.postTweet(1,6)
# twt.postTweet(1,7)
# twt.postTweet(1,8)
# twt.postTweet(1,9)
# twt.postTweet(1,10)
# twt.postTweet(1,11)
# twt.postTweet(2,20)
# twt.postTweet(1,12)
# twt.follow(1,2)
# twt.postTweet(2,21)
# twt.unfollow(1,2)
# twt.postTweet(1,13)
twt.getNewsFeed(3)
# twt.follow(1,3)
# twt.postTweet(2,6)
# twt.getNewsFeed(1)
# twt.unfollow(1,2)
# twt.getNewsFeed(1)

