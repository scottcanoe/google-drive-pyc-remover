"""
author: Scott Knudstrup
email: scottknudstrup at gmail dot com
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


# Get authorized. Opens a browser so you can tell google to trust this app.
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Repeatedly grab a bunch of pyc files and delete them.
n_deleted = 0
while True:
    files = drive.ListFile({'q': "title contains '.pyc'", 'maxResults' : 1000}).GetList()
    files = [f for f in files if f["title"].endswith(".pyc")]
    if len(files) == 0:
        break
        
    for fd in files:
        fname = fd["title"]
        try:            
            fd.Delete()
            n_deleted += 1
            print("{}: deleted {}".format(n_deleted, fname))
            
        except Exception as exc:
            print("---Exception raised: could not delete {}---".format(fname))
            
print(f"Deleted a total of {n_deleted} .pyc files.")


