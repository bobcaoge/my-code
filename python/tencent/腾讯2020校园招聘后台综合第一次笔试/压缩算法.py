#! /usr/bin/python3.6
#-*- coding:utf-8 -*-



def decode(s):
    ret = ""
    if not s:
        return ret
    i = 0
    num_of_middle = 0
    pos = 0
    while i < len(s):
        if s[i] != '[':
            ret += s[i]
            i += 1
        else:
            flag = True
            for k in range(i, len(s)):
                if s[k] == '|' and flag:
                    pos = k
                    flag = False
                if s[k] == "[":
                    num_of_middle += 1
                elif s[k] == ']':
                    num_of_middle -= 1
                if num_of_middle == 0:
                    num = int(s[i+1:pos])
                    return ret + decode(s[pos+1:k])*num+decode(s[k+1:])
    return ret


def main():
    s = input()
    print(decode(s))


if __name__ == "__main__":
    main()