# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        # IPV4 用点分十进制表示，数字0-255，不能有前导零
        # IPV6 用冒号分隔的四位十六进制表示
        if IP.count(":") >0 and IP.count(".") > 0:
            return "Neither"

        if IP.find(".") != -1:
            return self.ipv4_judger(IP)
        return self.ipv6_judger(IP)

    def ipv4_judger(self, ip):
        ip_nums = ip.split(".")
        if len(ip_nums) != 4:
            return "Neither"
        for num_s in ip_nums:
            if num_s == "" or num_s.startswith("0") and len(num_s) != 1 or (not num_s.isdigit()) or int(num_s) > 255:
                return "Neither"
        return "IPv4"

    def ipv6_judger(self, ip):
        ip_nums = ip.split(":")
        if len(ip_nums) != 8:
            return "Neither"
        for num_s in ip_nums:
            if len(num_s) > 4 or len(num_s) == 0:
                return "Neither"
            for c in num_s:
                if not "0"<=c<="9" and not "a"<=c<="f" and not "A"<=c<="F":
                    return "Neither"
        return "IPv6"



def main():
    s = Solution()
    print(s.validIPAddress("256.256.256.2:6"))


if __name__ == "__main__":
    main()
