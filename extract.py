import os

filePath = "D:/学/研/22 Fall/INFSCI 2125/project/citespace/input/"
SaveList = []
flag = False
files = os.listdir(filePath)

for file in files:
    position = filePath + file
    with open(position, "r",encoding='utf-8') as f:
        lines = f.readlines()
        content = f.read()
        print(content)
        for line in lines:
            if 'PN ' in line:
                flag = True
            if 'AD ' in line:
                flag = True
            if '(' in line:
                flag = False  
            if ':' in line:
                flag = False
            if '.' in line:
                flag = False
            if ',' in line:
                flag = False
            if 'AU ' in line:
                flag = False
            if flag == True:
                SaveList.append(line)
            flag = False

with open("output.txt","w") as fo:
    for i in SaveList:
        fo.write(i)

f.close()
fo.close()