import glob
import os
from shutil import copy2
import sys
def get_files(path):
    files=glob.glob(f"{path}/*")
    return files

def getfullpath(path):
    return  os.path.abspath(path)

def copyfile(source_path,goal_path):
    if not os.path.exists(goal_path):
        os.makedirs(goal_path)
    copy2(source_path,goal_path)

def splitfile(data,count):
    for i in range(1,len(data),count):
        if i+count-1>len(data):
            start,end=(i-1,len(data))
        else:
            start,end=(i-1,i+count-1)
        yield data[start:end]

def procees(path,count):
    files=get_files(path)
    splited_data=splitfile(files,count)

    for file_name,Folder in enumerate(splited_data):
        name=f"data_{file_name}"
        for file in Folder:
            copyfile(getfullpath(file),getfullpath(name))

if __name__=="__main__":

    if len(sys.argv)!=3:
        print("please provide correct parameters ")
        sys.exit()

    if len(sys.argv)==3:
        path=sys.argv[1]

        if os.path.isdir(path):
            count=sys.argv[2]
            procees(path,int(count))
            print("done")
        else:
            print("current directory is not valid")
    else:
        print("wrong paramter are provided")
