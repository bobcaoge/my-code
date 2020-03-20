# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import bisect
import collections


class TweetCounts(object):

    def __init__(self):
        self.tweet = collections.defaultdict(list)
        self.interval = {'minute': 60,
                         'hour': 3600,
                         'day': 3600*24}


    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        buff = self.tweet[tweetName]
        buff.insert(bisect.bisect(buff, time), time)
        self.tweet[tweetName] = buff

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        interval = self.interval[freq]
        cur_times = self.tweet[tweetName]
        start = bisect.bisect(cur_times, startTime-1)
        end = bisect.bisect(cur_times, endTime)
        length_of_time = endTime - startTime
        ret = [0]*(length_of_time//interval+1)
        for i in range(start, end):
            ret[(cur_times[i]-startTime)//interval] += 1
        return ret



def main():
    tc = TweetCounts()
    tc.recordTweet('t', 0)
    tc.recordTweet('t', 60)
    tc.recordTweet('t', 10)
    print(tc.getTweetCountsPerFrequency('minute', 't', 0, 59))
    print(tc.getTweetCountsPerFrequency('minute', 't', 0, 60))
    tc.recordTweet('t', 120)
    print(tc.getTweetCountsPerFrequency('hour', 't', 0, 210))



if __name__ == "__main__":
    main()
