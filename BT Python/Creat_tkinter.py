from tkinter import *
root=Tk()
root.title("HỌC CONTROL CƠ BẢN")
Label(root,text="Hi!!!"
                "Nice too meet you",fg="blue").pack()
Button(root,text="Nhấn vào để thoát",command=root.quit).pack()
e=StringVar()
e.set("https://www.youtube.com/watch?v=STCmIDdrWOU&list=PLiZ__4NpI1FVTb_CK63aCrpqFaVDsbbLd&index=98")
Entry(root,textvariable=e,width=30).pack()
root.resizable(height=True,width=True)
root.minsize(height=300,width=400)
root.mainloop()