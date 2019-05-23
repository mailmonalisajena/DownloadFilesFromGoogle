# DownloadFilesFromGoogle
This python script is used to download files from Google. This will take 'Download_path' and 'Download_file_urls' as   command line argument or if you are not passing any argument then it will take default value of 'Download_path' and   'Download_file_urls' this argument.

Default value of 'Download_path' :: User home path
Default value of 'Download_file_urls' :: "https://drive.google.com/uc?export=download&id=19LJ6Otr9p_stY5MLeEfRnA-jD8xXvK3m, 

https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

Usage of this script:
usage: Python download_file_from_google.py [-h] [-p path] [-u urls]

Details::  -h :: For help
	   -p :: Argument for '-p' should be string(Ex: "Download\path")
           -u :: Argument for '-u' should be string and ',' separator between urls(Ex: "url1, url2, url3")

For help:: 
	Python download_file_from_google.py -h

Execute with out passing arguments::  
	python  download_file_from_google.py

Execute with passing arguments::  
	python  download_file_from_google.py -p "Download\path" -u "url1, url2, url3"
