# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        m = {}
        for domain in cpdomains:
            dot_place = 0
            for index, c in enumerate(domain):
                if c == " ":
                    dot_place = index
                    m[domain[dot_place+1:]] = m.get(domain[dot_place+1:], 0) + int(domain[:dot_place])
                if c == ".":
                    m[domain[index+1:]] = m.get(domain[index+1:], 0) + int(domain[:dot_place])
        return [str(value)+" "+key for key, value in m.items()]




def main():
    s = Solution()
    print(s.subdomainVisits(["9001 discuss.leetcode.com"]))

if __name__ == "__main__":
    main()
