import os

def get_size_of_dir(path):
	size = 0
	try:
		if not os.path.isdir(path):
			size = os.path.getsize(path)
			#with open("log.log", "wa") as f:
			#	f.write(str((path, size)))
			print (path, size)
			return size 
		for root,dirs,files in os.walk(path):
			for f in files:
				size += get_size_of_dir(root+'/'+f)
			for d in dirs:
				size += get_size_of_dir(root+'/'+d)
	except:
		pass
	return size
	

path = raw_input('please input the dictionary which size you want to get \n') 
#print path
#print type(path)


print get_size_of_dir(path)

