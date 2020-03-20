# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.m = {0:{i: 0 for i in range(length)}}
        self.cur_num_of_snapshot = 0


    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.m[self.cur_num_of_snapshot][index] = val


    def snap(self):
        """
        :rtype: int
        """
        self.cur_num_of_snapshot += 1
        self.m[self.cur_num_of_snapshot] = {}
        return self.cur_num_of_snapshot - 1


    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        while self.m[snap_id].get(index, -1) == -1:
            snap_id -= 1

        return self.m[snap_id][index]



def main():
    s = SnapshotArray(3)
    s.set(0, 5)
    print(s.m)
    s.snap()
    print(s.m)
    s.set(0, 6)
    print(s.m)
    print(s.get(0, 0))



if __name__ == "__main__":
    main()
