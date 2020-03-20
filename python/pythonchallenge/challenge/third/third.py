f = open("word.txt", "r")
s = f.read()
ret = {}
for i in range(len(s)):
    buffer = s[i]
    if buffer in ret.keys():
        ret[buffer] += 1
    else:
        ret[buffer] = 1


print(ret)
f.close()