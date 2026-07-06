import os
# os.mkdir("C://python projects//new_directory")
# os.mkdir(f"C://python projects//new_directory//folder_{1}")
print(os.listdir("C://python projects//new_directory//folder_1"))
png=1
jpg=1
pdf=1
path="C://python projects//new_directory//folder_1"
if(os.path.exists(path)):
    for file in os.listdir(path):
        if file.endswith(".png"):
            os.rename(f"{path}//{file}",f"{path}//png_{png}.png")
            png+=1
        elif file.endswith(".jpg"):
            os.rename(f"{path}//{file}",f"{path}//jpg_{jpg}.jpg")
            jpg+=1
        elif file.endswith(".pdf"):
            os.rename(f"{path}//{file}",f"{path}//pdf_{pdf}.pdf") 
            pdf+=1
    print("os.listdir(path) after renaming files:", os.listdir(path))
else:
    print("Path does not exist")