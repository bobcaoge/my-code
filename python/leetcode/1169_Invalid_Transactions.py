# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import collections


class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        def manager(info):
            ret = set()
            # time, amount, city
            for i in range(len(info)):
                if info[i][1] > 1000:
                    ret.add(info[i])
                for j in range(i+1, len(info)):
                    if info[j][0] - info[i][0] < 60 and info[i][2] != info[j][2]:
                        ret.add(tuple(info[i]))
                        ret.add(tuple(info[j]))
                    if info[j][0] - info[i][0] > 60:
                        break
            return ret


        info = collections.defaultdict(list)
        ret = []
        for transaction  in transactions:
            arr = transaction.split(",")
            info[arr[0]].append((int(arr[1]), int(arr[2]), arr[3]))

        for key, other in info.items():
            print(key, sorted(other))
            cur = manager(sorted(other))
            if cur:
                ret.extend([key+","+",".join(str(i) for i in x) for x in cur])

        return ret


def main():
    s = Solution()
    print(s.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
    print(s.invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))
    print(s.invalidTransactions(["alex,741,1507,barcelona","xnova,683,1149,amsterdam","bob,52,1152,beijing","bob,137,1261,beijing","bob,607,14,amsterdam","bob,307,645,barcelona","bob,220,105,beijing","xnova,914,715,beijing","alex,279,632,beijing"]))
    print(s.invalidTransactions(["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))


if __name__ == "__main__":
    main()
