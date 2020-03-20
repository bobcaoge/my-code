# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def simplifyPath1(self, path):
        """
        :type path: str
        :rtype: str
        """
        ret = []
        last_of_latter = 0
        name = ""
        last_of_dot = 0
        for index, c in enumerate(path+"/"):
            if c == "/":
                if last_of_latter != 0:
                    ret.append(name)
                else:
                    if last_of_dot == 2:
                        if ret:
                            ret.pop()
                    if last_of_dot> 2:
                        ret.append("."*last_of_dot)
                name = ""
                last_of_latter = 0
                last_of_dot = 0
            else:
                if c == ".":
                    last_of_dot += 1
                else:
                    last_of_latter += 1
                name += c
            # print(ret)
        return "/" + "/".join(ret)

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        ret = []
        for p in path:
            if p:
                if p == "..":
                    if ret:
                        ret.pop()
                elif p == ".":
                    continue
                else:
                    ret.append(p)

        return "/" + "/".join(ret)


def main():
    s = Solution()
    print(s.simplifyPath("/home/"))
    print(s.simplifyPath("/../"))
    print(s.simplifyPath("/home//foo/"))
    print(s.simplifyPath("/a/./b/../../c/"))
    print(s.simplifyPath("/a/../../b/../c//.//"))
    print(s.simplifyPath("/a//b////c/d//././/.."))
    print(s.simplifyPath("/..."))
    print(s.simplifyPath("/..hidden"))


if __name__ == "__main__":
    main()
