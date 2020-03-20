# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class RecentCounter(object):

    def __init__(self):
        self.requests = []
        self.length = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        i = 0
        while i < self.length:
            if t - self.requests[i] <= 3000:
                break
            i += 1
        self.requests[0:i] = []
        self.requests.append(t)
        self.length = self.length - i + 1
        return self.length



def main():
    pass


if __name__ == "__main__":
    main()
