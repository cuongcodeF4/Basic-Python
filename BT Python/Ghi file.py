def LuuFile(path):
    file=open(path,'w',encoding = 'utf-8')
    file.writelines("sv1;Thái Việt Cường;9.5\n")
    file.writelines("sv2;TRương Quốc Tín;9\n")
    file.close()
LuuFile("csdl.txt")