import os
import time
def log(log_file = "D:/Project/python/modules/log.txt", message=""):
	if not os.path.exists(log_file):
		mode = "w"
	else:
		mode = "a"

	with open(log_file, mode) as f:
		f.write(time.ctime()+":\n    "+message+"\n")
