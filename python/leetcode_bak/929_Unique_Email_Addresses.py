# /usr/bin/python3.6
# -*- coding:utf-8 -*-
import re

class Solution(object):

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = set()
        pattern = re.compile(r"(.*?)\+")
        for email in emails:
            index = email.rfind("@")
            domain = email[index:]
            local_name = pattern.findall(email[:index]+"+")[0].replace(".", "")
            # print(local_name)
            s.add(local_name+domain)
        print(s)
        return len(s)

def main():
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


if __name__ == "__main__":
    main()
