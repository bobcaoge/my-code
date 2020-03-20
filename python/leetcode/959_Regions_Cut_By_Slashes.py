# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid[0])+1
        visited =[0]*(N*N)
        graph = [[] for i in range(N*N)]
        for i in range(N-1):
            graph[i].append(i+1)
            graph[i+1].append(i)

            graph[N*N-1-i].append(N*N-2-i)
            graph[N*N-2-i].append(N*N-1-i)

            graph[N*i].append(N*i+N)
            graph[N*i+N].append(N*i)

            graph[N*i+N-1].append(N*i+N+N-1)
            graph[N*i+N+N-1].append(N*i+N-1)

        for i in range(N-1):
            for j, c in enumerate(grid[i]):
                a = i*N+j
                if c == "/":
                    graph[a+1].append(a+N)
                    graph[a+N].append(a+1)
                elif c == "\\":
                    graph[a].append(a+N+1)
                    graph[a+N+1].append(a)
        self.ret = 0

        def dfs(i, old):
            if visited[i] == -1:
                self.ret += 1
                return
            if visited[i] == 1:
                return
            visited[i] = -1
            for j in graph[i]:
                if j != old:
                    dfs(j, i)
            visited[i] = 1

        for i in range(N*N):
            dfs(i, -1)

        return self.ret



def main():
    s = Solution()
    print(s.regionsBySlashes([
        "/\\",
        "\\/"
    ]))
    print(s.regionsBySlashes(["///","// ", "/  "]))
    print(s.regionsBySlashes([" /","  "]))


if __name__ == "__main__":
    main()
