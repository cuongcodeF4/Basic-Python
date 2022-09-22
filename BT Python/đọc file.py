def Docfile(path):
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.upper()
        print(data)
    file.close()
Docfile("csdl.txt")