# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        if not votes:
            return ''
        teams = {}
        for vote in votes:
            for i, name in enumerate(vote):
                if name not in teams.keys():
                    teams[name] = [0]*len(vote)
                teams[name][i] -= 1
        info = [[v, name] for name, v in teams.items()]
        info.sort()
        ret = ''.join([n for _, n in info])
        return ret



def main():
    s = Solution()
    print(s.rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))
    print(s.rankTeams(["ABC","ACB","ABC","ACB","ACB"]))


if __name__ == "__main__":
    main()
