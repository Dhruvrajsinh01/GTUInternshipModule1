import os
import shutil
path = 'folder'
try:
	#os.remove(path)
	os.rmdir(path)
	#shutil.rmtree(path)

except FileNotFoundError as e:
	print(e)
except PermissionError as e:
	print(e)
except OSError as e:
	print(e)
else:
	print("file deleted")