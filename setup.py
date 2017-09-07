#setup.py 
from distutils.core import setup 
import glob
import py2exe
setup(
	windows = ['main.py',],
	data_files=[("images",
	           [r"C:\Python33\Lib\site-packages\PyQt5\libEGL.dll"]),
	          ("platforms",
	           [r"C:\Python33\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll"])],
	options = {'py2exe': py2exe_options}
	)