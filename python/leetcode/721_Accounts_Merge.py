# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def add(g, x, y):
            if not g.get(x, None):
                g[x] = []
            if not g.get(y, None):
                g[y] = []
            g[x].append(y)
            g[y].append(x)

        m = {}  # mail: index
        graph = {}
        for index, account in enumerate(accounts):
            for i in range(1, len(account)):
                if m.get(account[i], index) != index:
                    add(graph, index, m[account[i]])
                else:
                    m[account[i]] = index
        visited = set()
        def dfs(i):
            if i in visited:
                return set()
            visited.add(i)
            if not graph.get(i, None):
                return set(accounts[i][1:])
            cur = set(accounts[i][1:])
            for j in graph[i]:
                cur |= dfs(j)
            return cur
        ret = []
        for i in range(len(accounts)):
            cur = dfs(i)
            if cur:
                ret.append([accounts[i][0]] + sorted(list(cur)))
        return ret


def main():
    s = Solution()
    # print(s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
    # print(s.accountsMerge([["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]))
    print(s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))


if __name__ == "__main__":
    main()
