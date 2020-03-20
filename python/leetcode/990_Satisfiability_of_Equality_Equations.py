# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph = {}
        def add_edge(x, y):
            if not graph.get(x, None):
                graph[x] = set()
            if not graph.get(y, None):
                graph[y] = set()
            graph[x].add(y)
            graph[y].add(x)

        for equation in equations:
            start = equation[0]
            eq = equation[1:3]
            end = equation[3]
            if eq == "==":
                add_edge(start, end)
        fathers = {chr(x+97): chr(x+97) for x in range(26)}
        visited = set()

        def dfs(i, father):
            if i not in visited:
                visited.add(i)
                fathers[i] = father
                for node in graph.get(i, []):
                    dfs(node, father)

        for i in range(26):
            dfs(chr(i+97), i)
        for equation in equations:
            start = equation[0]
            eq = equation[1:3]
            end = equation[3]
            if eq == "!=":
                if fathers[start] == fathers[end]:
                    return False
        return True






def main():
    s = Solution()
    print(s.equationsPossible(["a==b","b!=a"]))
    print(s.equationsPossible(["a==b","c==d", "b==c"]))
    print(s.equationsPossible(["a==b","b==a"]))
    print(s.equationsPossible(["a==b","b==c","a==c"]))
    print(s.equationsPossible(["a==b","b!=c","c==a"]))
    print(s.equationsPossible(["c==c","b==d","x!=z"]))
    print(s.equationsPossible(["t!=b","h!=u","l!=y","j==j","w==s","p==q","r!=t","r==i","e!=y","v==s","i!=p","h!=i","i==o","e==e","j!=h","y!=s","k==g","c==f","n==v","a==w","d==w","f!=e","v==s","w!=g","g!=s","j!=d","c!=u","y!=n","q!=j","d!=x","l==m","q!=b","r!=n","j!=o","w!=q","t!=e","a!=m","m!=j","j!=b","v!=w"]))
    print(s.equationsPossible(["i!=c","i!=f","k==j","g==e","h!=e","h==d","j==e","k==a","i==h"]))


if __name__ == "__main__":
    main()
