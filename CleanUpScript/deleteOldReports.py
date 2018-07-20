import os
import time
import shutil
numdays = 86400*30 # 30 days 
now = time.time()  # Get current time
directory=os.path.join("/home","C:/Users/Aquarell/Desktop/current_files") # directory to delete files
for dir in os.listdir(directory): # for all the names of directory
	timestamp = os.path.getmtime(os.path.join(directory,dir)) # when the file is created
	if now-numdays > timestamp: # is not older than 30 days
		shutil.rmtree(os.path.join(directory,dir)) # recursively delete directory
