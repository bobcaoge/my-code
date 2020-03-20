# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        pattern = re.compile(r"[a-zA-Z]")
        pattern2 = re.compile(r"(^\w+) ")
        pattern3 = re.compile(r" .*")
        digit_logs = []
        for index, log in enumerate(logs):
            identity = pattern2.findall(log)[0]
            log_file = pattern3.findall(log)[0]
            if not pattern.findall(log_file):
                digit_logs.append([log_file, identity])

            logs[index] = [log_file, identity]
        for log in digit_logs:
            logs.remove(log)
        return [identity+log_file for log_file, identity in sorted(logs) + digit_logs]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
