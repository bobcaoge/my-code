# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution:
    ret = []
    def dfs(self, s, path):
        if not s:
           self.ret.append(path)
        for i in range(len(s)):
            if self.ispali(s[:i+1]):
                self.dfs(s[i+1:], path+[s[:i+1]])

    def ispali(self, s):
        return s == s[-1::-1]

    def partition(self, s):
        self.ret = []
        self.dfs(s, [])
        return self.ret




def main():
    s = Solution()


if __name__ == "__main__":
    main()
