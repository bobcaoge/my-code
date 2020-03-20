# /usr/bin/python3.6
# -*- coding:utf-8 -*-


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        length = (len(bottom)*(len(bottom)+1))/2

        def dfs(i, flag, bott):
            if i == flag - 1:
                i += 1
                flag += flag-1

            print(i, bott, length, flag, )
            if len(bott) == length:
                return True
            for c in allowed:
                if c[0:2] == bott[i:i+2]:
                    if dfs(i+1, flag, bott+c[2]):
                        return True
            return False

        return dfs(0, len(bottom), bottom)


def main():
    s = Solution()
    print(s.pyramidTransition(bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]))
    print(s.pyramidTransition("CACAC",["ACB","AAC","AAB","BCD","BCC","BAA","CCD","CCA","CAD","DAD","DAC","DCD","ACD","DCA","ABA","BDA","BDC","BDB","BBA","ADD","ADC","CDB","DDA","CBB","CBC","CBA","CDA","CBD","DBA","DBC","DBD"]))
    print(s.pyramidTransition("BCD",["ACC","ACB","ABD","DAA","BDC","BDB","DBC","BBD","BBC","DBD","BCC","CDD","ABA","BAB","DDC","CCD","DDA","CCA","DDD"]))
    print(s.pyramidTransition("BDBBAA",["ACB","ACA","AAA","ACD","BCD","BAA","BCB","BCC","BAD","BAB","BAC","CAB","CCD","CAA","CCA","CCC","CAD","DAD","DAA","DAC","DCD","DCC","DCA","DDD","BDD","ABB","ABC","ABD","BDB","BBD","BBC","BBA","ADD","ADC","ADA","DDC","DDB","DDA","CDA","CDD","CBA","CDB","CBD","DBA","DBC","DBD","BDA"]))


if __name__ == "__main__":
    main()
