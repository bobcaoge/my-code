import urllib2
import re
url_front = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
next = 63579
pattern = r"\d+"
pattern = re.compile(pattern)
content = ""
content_old = ''
try:
    for i in range(401):
        print i
        response = urllib2.urlopen(url_front+str(next))
        content = response.read()
        print content
        if next:
            next = pattern.findall(content)[0]
except:
    print content



