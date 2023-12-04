filePath = "D:/学/研/23 Fall/INFSCI 2415/output.txt"
SaveList = []

with open(filePath, "r") as f:
    lines = f.readlines()
    content = f.read()
    print(content)
    for line in lines:
        if 'PN' in line:
            PN = line[3:5]
        if 'AD' in line:
            part = line.split()
            data = part[-1]
            str = PN + " " + data
            SaveList.append(str)
            SaveList.append("\n")   

with open("output0.txt","w") as fo:
    for i in SaveList:
        fo.write(i)

f.close()
fo.close()

