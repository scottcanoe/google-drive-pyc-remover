# google-drive-pyc-remover
Python script for deleting all .pyc files from you didn't realize were being backed up by google drive.

Installation
------------
The only dependency is PyDrive. I used Python 3.8.


Usage
-----
First get a developer authentication secrets file if you don't already have one and put it in the same directory as "remove_pyc_files.py". Make sure it's named "client_secrets.json". This is obviously a lame way to handle files, so feel free to fix it.

Finally, run "remove_pyc_files.py". It'll print the name of each file it deletes along with the number of files deleted so far.


