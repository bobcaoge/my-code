# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        def compare(s1, s2):
            """
            :type s1: str
            :type s2: str
            :return:
            """
            return s1[s1.rfind(":"):] > s2[s2.rfind(":"):]
        sorted(logs, compare)
        # print(logs)
        stack = []
        ret = [0]*n
        pause = []
        for log in logs:
            if "start" in log:
                stack.append(log)
                pause.append(0)
            else:
                id = int(log[:log.find(":")])
                interval = int(log[log.rfind(":")+1:]) - int(stack[-1][stack[-1].rfind(":")+1:]) - pause[-1] + 1
                ret[id] += interval
                stack.pop()
                pause[-1] += interval
                if stack:
                    pause[-2] += pause[-1]
                    pause.pop()
                else:
                    pause = []
        return ret



def main():
    s = Solution()
    print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
    print(s.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))


if __name__ == "__main__":
    main()
