"""s="*****Adu Amazing"
print(s.strip('*'))
print(s.startswith("*")) """
def Locso(dauso):
    dsArr=["0982225556","0981335413","0904646316","0975123164","0981215454"]
    for phone in dsArr:
        if (phone.startswith(dauso)):
            return phone
    return '<empty>'
print("Nhập đầu số:")
dauso=input('')
phone=Locso(dauso)
print(phone)
