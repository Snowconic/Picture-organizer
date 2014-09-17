import shutil, os
def renameFile(source, destination):
    numberOfFiles = []
    for item in os.listdir(destination):
        numberOfFiles.append(item)
    newName = (os.path.splitext(source)[0]).split('%')[0] + str(len(numberOfFiles)) + os.path.splitext(source)[1]
    os.rename(source, newName)
    return newName
    
def moveFile(source, destination):
    filename = source
    if not os.path.isdir(destination):
        os.mkdir(destination)
   # if os.path.isfile(destination+"/"+filename.split('%')[0]+filename.split('%')[1]):
    filename = renameFile(filename, destination)
    shutil.move(filename, destination)

def organizePictures():
    for item in os.listdir(os.getcwd()):
        if not os.path.isdir(item) and not item.endswith('.py'):
            moveFile(item, (os.path.splitext(item)[0]).split('%')[0] + " Folder")

organizePictures()
