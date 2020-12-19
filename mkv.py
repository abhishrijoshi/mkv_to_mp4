import os
import sys
import subprocess as sp
import glob

currentWorkingDir = os.getcwd()

print(currentWorkingDir)

files = [file for file in glob.glob("*.mkv")]


print(files)

for i in range(0,len(files)):

    try:

        sp.call(["ffmpeg", "-i", files[i], "-codec", "copy", files[i]+".mp4"])
        sp.call(["rm", "-rf", files[i]])
        
	
	
