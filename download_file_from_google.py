import wget
import os
from os.path import expanduser
import argparse

#########################################################################################################################
#
# Program to download multiple files from Google.
# Syntax ::  Download-file-from-google-drive.py [-h] [-p path] [-u urls]
# Details::  -p :: Argument for '-p' should be string
#          	 -u :: Argument for '-u' should be string and ',' separator between urls(Ex: "url1, url2, url3")
#
#########################################################################################################################



"""
 Function to download files from google to local disk
"""
def download_files(files_url,path):
	os.chdir(path)
	files_url=files_url.split(",")
	
	for f_url in files_url:
		f_url=f_url.strip()
		print "downloading ... "+f_url
		wget.download(str(f_url))

"""
 Main function.
"""
def main():	
    # Default Download path
	download_path = expanduser("~")
	
	# Default download files url
	files_url = "https://drive.google.com/uc?export=download&id=19LJ6Otr9p_stY5MLeEfRnA-jD8xXvK3m, https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
   
	#Using argparse package this is the description of the program... 
	parser = argparse.ArgumentParser(description='Program to download files from Google to local disk')

	# command line arguments with there decsription..
	parser.add_argument('-p', metavar="path" , type=str, help='Files download path', default=download_path)
	parser.add_argument('-u', metavar="urls" , type=str, help='Download files url', default=files_url)

	# parse_args() for parsing arguments
	args = parser.parse_args()

	# Download path and Download file urls taking from the command line..
	Path= args.p
	file_url= args.u

	download_files(file_url,Path)
     

if __name__=="__main__":
    main()

