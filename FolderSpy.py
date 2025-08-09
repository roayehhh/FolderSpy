import os

folderPath = input("\n✅ Please enter the path of a folder: ")
os.chdir(folderPath)
files = os.listdir()

fileCounter = 0
folderCounter = 0
fileList = []

for i in files:
    fullFolderPath = os.path.join(folderPath,i)
    if os.path.isdir(fullFolderPath):
        folderCounter+=1
    elif os.path.isfile(fullFolderPath):
        fileCounter+=1
        fileInB = os.path.getsize(fullFolderPath)
        fileInMB = fileInB / (1024*1024)
        fileDictonary = (
            {"fileName": i, "size": fileInMB}
        )
        fileList.append(fileDictonary)


print(f"🗃️  Files: {fileCounter}, 📁 Folders: {folderCounter}")

try:
    largest = max(fileList,key=lambda x: x["size"])
    smallest = min(fileList, key=lambda x: x["size"])
    print(f"1️⃣  Largest file: {largest['fileName']} - {largest['size']:.2f} MB")
    print(f"2️⃣  Smallest file: {smallest['fileName']} - {smallest['size']:.2f} MB \n")
    
except ValueError:
    print("⚠️  This folder contains no files.\n")




