from distutils.core import setup
setup (# Distribution meta-data  
	name = "sweep",  
	version = "1.0",  
	description = "a little game of sweeping",  
	py_modules = ['sweep.sweep'],  
	packages = ['sweep'], requires=['PIL']
)