# metatrim written by Yamil Asusta (elbuo8)
# To execute use: python metatrim.py mainfolder

import sys
import os
import eyeD3

def main():
	#Read parameters from Command Line
	trimmer(sys.argv[1])
	
def trimmer(directory):
	tag = eyeD3.Tag()
	
	for root, dirs, files in os.walk(directory):
		for name in files:
			if name.split(".")[-1] == "mp3":
				tag.link(root + "/" + name)
				tag.setArtist(tag.getArtist().strip())
				tag.setTitle(tag.getTitle().strip())
				tag.update()
							
		for name in dirs:
			trimmer(name)
			
			
if __name__ == '__main__':
  main()