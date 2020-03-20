# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):

    hour_storage = []
    minute_storage = []

    def __init__(self):
        self.prepare()

    def prepare(self):
        for i in range(60):
            index = bin(i).count("1")
            # print(index)
            if i < 10:
                store = "0"+str(i)
            else:
                store = str(i)
            if len(self.minute_storage) <= index:
                self.minute_storage.append([store])
            else:
                # print(self.minute_storage)
                self.minute_storage[index].append(store)
            if i < 12:
                if len(self.hour_storage) <= index:
                    self.hour_storage.append([str(i)])
                else:
                    self.hour_storage[index].append(str(i))

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        for i in range(num+1):
            if i == 4:
                break
            hours = self.hour_storage[i]
            if num-i < 6:
                minutes = self.minute_storage[num-i]
                for hour in hours:
                    for minute in minutes:
                        ret.append("{0}:{1}".format(hour, minute))
        return ret




def main():
    s = Solution()
    print(s.hour_storage)
    print(s.minute_storage)
    print(s.readBinaryWatch(1))
    print(s.readBinaryWatch(2))
    a = ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
    print()

if __name__ == "__main__":
    main()
