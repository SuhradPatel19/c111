import shutil
import os

# copying files
# source=r"D:\dev\python\c111\log.png"
# destination=r"D:\dev\python\c112\log.png"
# moving=shutil.copy(source,destination)
# print("done")

# moving files
# source=r"D:\dev\python\c111\google_icon.png"
# destination=r"D:\dev\python\c112"
# moving=shutil.move(source,destination)
# print("done")

source=r"D:\dev\python\files"
destination=r"D:\dev\python\c112"
dir=os.listdir(source)
for i in dir:
    print(i)
    moving=shutil.move(source+"\\"+ i,destination)
print("done")


