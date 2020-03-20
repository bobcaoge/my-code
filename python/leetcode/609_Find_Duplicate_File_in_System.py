# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re


class Solution(object):
    def manager(self, s, m):
        """
        :type s: str
        :type m: dict
        :return:
        """
        info = s.split(" ")
        directory = info[0]
        pattern = re.compile(r"\((.*)\)")
        pattern2 = re.compile(r"(.*?)\(")
        for file in info[1:]:
            content = pattern.findall(file)[-1]
            filename = pattern2.findall(file)[-1]
            if m.get(content, None):
                m[content].append(directory+"/"+filename)
            else:
                m[content] = [directory+"/"+filename]

    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for path in paths:
            self.manager(path, m)
        ret = filter(lambda x: True if len(x) > 1 else False, [y for x, y in m.items()])
        return list(ret)


def main():
    s = Solution()
    print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
    print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]))


if __name__ == "__main__":
    main()
