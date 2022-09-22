def luudulieusp(path,data):
    file=open(path,"w",encoding="utf-8")
    file.writelines(data)
    file.writelines('\n')
    file.close()
def Docfile(path):
    a=[]
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        b=data.split(';')
        a.append(b)
    file.close()
    return a
