#!/usr/bin/python 
# usage: python ftp.py filename 

import os,sys
from ftplib import FTP

server = 'pantoto.org' # Server name
username = 'usrname' # server username
passwd = 'passwd'   # Password for this user ID
filename = sys.argv[1]  # This take an argument from commandline
ftp = FTP(server)
ftp.login(username,passwd)  # It will login by given username & password -- No no, dnt alter here, it jst takes args frm above
fp = open(filename, 'rb') 
ftp.cwd("workspace") # This is a PATH/DIRECTORY where you would like to store the file in your server
ftp.storbinary("STOR small_"+filename, fp) # Store in binary and prefix a name to a file
ftp.quit()
