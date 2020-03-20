import zipfile as zp
import re

z = zp.ZipFile("channel.zip")
num = 90052
flag = True
ret = ""
while flag:
    filename = str(num) + ".txt"
    info_of_num_txt = z.getinfo(filename)
    content = z.read(filename)
    pattern = "\d+"
    pattern = re.compile(pattern)
    try:
        num = pattern.findall(content)
        if num:
            num = num[0]
        else:
            flag = False
    except:
        pass
    ret += info_of_num_txt.comment
print ret
