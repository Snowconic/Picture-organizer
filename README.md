Picture-organizer
=================

Organizes all non-python, non-directory files in the current directory based on name. Ignores/removes any % signs at the end of the file's name, in order to allow semi-duplicate names so that files go to the same folder if needed.

Extrapolation:
In a folder you have Organize.py, and five files named "Akito.png", "Akito.jpg", "Akito.txt", "Akito%.jpg" (As "Akito.jpg" is already taken), and "Garbage.jpg".

It creates new folders "Akito Folder", and "Garbage Folder".

It will take every file with "Akito.extension" as the name, and all files with "Akito%.extension" as the name with any number of % symbols, and then place them in the "Akito Folder".

"Garbage.jpg", due to having a different name, is placed in the "Garbage Folder" that was made for it.
