# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        record = {c:i for i, c in enumerate(S)}

        anchor = 0
        ret = []
        end = 0
        for index, c in enumerate(S):
            end = max(end, record[c])
            if index == end:
                ret.append(end-anchor+1)
                anchor = index + 1
        return ret



def main():
    s = Solution()
    print(s.partitionLabels("acacd"))
    print(s.partitionLabels("ababcbacadefegdehijhklij"))


if __name__ == "__main__":
    main()
