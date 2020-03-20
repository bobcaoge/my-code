import re
f = open("word.txt", "r")
content = f.readlines()
def get(content):
    ret = []
    pattern = r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]'
    pattern = re.compile(pattern)
    buffer = pattern.findall(content)
    if buffer:
        ret.append(buffer)
    pattern = r'^[A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]'
    pattern = re.compile(pattern)
    buffer = pattern.findall(content)
    if buffer:
        ret.append(buffer)
    pattern = r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z]$'
    pattern = re.compile(pattern)
    buffer = pattern.findall(content)
    if buffer:
        ret.append(buffer)
    return ret
for i in range(len(content)):
    p = get(content[i])
    if p:
        print(p)

