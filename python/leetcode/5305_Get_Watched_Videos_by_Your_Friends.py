# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        visited = [False]*len(friends)
        cur = [id]
        visited[id] = True
        for i in range(level):
            buff = []
            for person in cur:
                for friend in friends[person]:
                    if not visited[friend]:
                        buff.append(friend)
                        visited[friend] = True
            cur = buff
        videos = []
        for person in cur:
            videos.extend(watchedVideos[person])
        buff = sorted([[times, video] for video, times in collections.Counter(videos).items()])
        return [video for times, video in buff]




def main():
    s = Solution()
    print(s.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1))
    print(s.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2))


if __name__ == "__main__":
    main()
