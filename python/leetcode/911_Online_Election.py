# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.info = self.manage(persons)
        self.times = times


    def manage(self, persons):
        votes = [0]*(max(persons)+1)
        old = -1
        query_info = []
        for person in persons:
            if old == -1:
                votes[person] += 1
                old = person
                query_info.append(person)
            else:
                votes[person] += 1
                if votes[person] >= votes[old]:
                    query_info.append(person)
                    old = person
                else:
                    query_info.append(old)
        return query_info

    def get_time(self, t):
        start = 0
        end = len(self.times) - 1
        mid = (start+end)/2
        while start < end:
            if self.times[mid] == t:
                return mid
            elif self.times[mid] > t:
                end = mid - 1
            else:
                if self.times[mid+1] <= t:
                    start = mid+1
                else:
                    return mid
            mid = (start+end)/2
        return mid


    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.info[self.get_time(t)]



def main():
    s = TopVotedCandidate([0,1,0,0], [1,3,5,7])
    # for i in range(1, 10):
    #     print(s.get_time(i))
    print(s.info)


if __name__ == "__main__":
    main()
