# google-drive-pyc-remover
Python script for deleting all .pyc files you didn't realize were being tracked and synced by drive. I made this because restoring my synced folders using Google Backup and Sync was taking forever, and I realized there was a ton of junk (mostly .pyc files) being backed up that I didn't have a reason to care about previously. And I couldn't just simply delete the .pyc files locally, wait for google drive to catch up, and then disable tracking since I had just wiped my hard drive to start fresh. Lesson learned. On the other hand, I did get to play around with PyDrive a little which might come in handy down the line.


Installation
------------
The only dependency is PyDrive. I used Python 3.8.


Usage
-----
First get a developer authentication secrets file if you don't already have one and put it in the same directory as "remove_pyc_files.py". Make sure it's named "client_secrets.json". This is obviously a lame way to handle files, so feel free to fix it.

Finally, run "remove_pyc_files.py". It'll print the name of each file it deletes along with the number of files deleted so far.


