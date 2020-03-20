# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        values = self.m.get(key, None)
        if values:
            values.append((value, timestamp))
        else:
            self.m[key] = [(value, timestamp)]


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        info = self.m.get(key, None)
        if not info or info[0][1] > timestamp:
            return ""
        if info[-1][1] < timestamp:
            return info[-1][0]
        start = 0
        end = len(info)
        mid = (start+end)/2
        while start < end:
            if info[mid][1] == timestamp:
                return info[mid][0]
            if info[mid][1] < timestamp:
                start = mid+1
                if info[start][1] >timestamp:
                    return info[start][0]

            else:
                end = mid-1
            mid = (start+end)/2
        return info[start][0]




def main():
    pass


if __name__ == "__main__":
    main()
