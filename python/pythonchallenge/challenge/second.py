
def str_tran(a):
    length = len(a)
    ret = ""
    b = "abcdefghijklmnopqrstuvwxyz"
    c = "cdefghijklmnopqrstuvwxyzab"
    d = {}
    # d[" "] = " "
    # d['.'] = '.'
    for i in range(len(b)):
        d[b[i]] = c[i]
    # print(d)
    ret = ""
    for i in range(0, len(a)):
        buffer = a[i]
        # print(buffer)
        if 'a' <= buffer <= 'z':
            ret += d[buffer]
        else:
            ret += buffer
    return ret
a =  "http://www.pythonchallenge.com/pc/def/map.html"
b = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(str_tran(a))
print(str_tran(b))


