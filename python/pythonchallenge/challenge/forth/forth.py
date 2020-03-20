# coding:utf-8
"""
这个代码有问题
"""


def adjust(char_s):
    if "A" <= char_s <= "Z":
        return True


f = open("word.txt", "r")
s = f.readlines()
row_s = len(s)
column_s = len(s[0])
ret = []
print(column_s)
try:
    for i in range(row_s):
        flag = 0
        for j in range(column_s):
            if adjust(s[i][j]):
                continue
            if 2 < j < column_s - 3:
                # print(j)
                if 3 < j < column_s - 4:
                    if adjust(s[i][j - 4]):
                        continue
                    if adjust(s[i][j + 4]):
                        continue
                if j == 3:
                    if adjust(s[i][j + 4]):
                        continue
                if j == column_s - 4:
                    if adjust(s[i][j - 4]):
                        continue

                if adjust(s[i][j - 3]):
                    flag += 1
                else:
                    continue
                if adjust(s[i][j - 2]):
                    flag += 1
                else:
                    continue
                if adjust(s[i][j - 1]):
                    flag += 1
                else:
                    continue
                if adjust(s[i][j + 3]):
                    flag += 1
                else:
                    continue
                if adjust(s[i][j + 2]):
                    flag += 1
                else:
                    continue
                if adjust(s[i][j + 1]):
                    flag += 1
                else:
                    continue
                if flag == 6:
                    ret.append(s[i][j] + ":" + str(i + 1) + ":" + str(j + 1))
except:
    pass

f.close()
print(ret)
