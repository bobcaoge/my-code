import re
import zipfile
import os
import urllib2

file_number = 90052
info = []
ret = 0
number = 0
while True:
    file_path = "./channel/"+str(file_number)+".txt"
    # try:
    #     #     response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/"+str(file_number)+".html")
    #     #     print response.read()
    #     #     info.append(response.read())
    #     # except:
    #     #     pass
    with open(file_path, "rb") as f:
        content = f.read()
        print content
        pattern = r'(\d+)'
        pattern = re.compile(pattern)
        file_number = pattern.findall(content)[0]
        number += int(file_number)
        print number
    ret += 1
    print ret
        # print file_number
    # os.remove(file_path)
    # print(info)

