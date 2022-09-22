from tkinter import *
from PIL import ImageTk, Image
from time import sleep
 
img=[0,0,0]
game=Tk()
game.title("Dragon run")
canvas=Canvas(master=game,height=300,width=600,bg="white")
canvas.pack()

img[0]=ImageTk.PhotoImage(Image.open("D:\Code\Python\Game\Dragon_run\Pitctures Game\photos\dragon.jpg"))
img[1]=ImageTk.PhotoImage(Image.open("D:\Code\Python\Game\Dragon_run\Pitctures Game\photos\cloud.jpg"))
img[2]=ImageTk.PhotoImage(Image.open("D:\Code\Python\Game\Dragon_run\Pitctures Game\photos/tree.jpg"))

dragon=canvas.create_image(0,245,anchor=NW,image=img[0])
cloud=canvas.create_image(550,50,anchor=NW,image=img[1])
tree=canvas.create_image(550,250,anchor=NW,image=img[2])
canvas.update()

def moveCloud():
    global cloud
    canvas.move(cloud,-5,0)
    if canvas.coords(cloud)[0]<-20:
        canvas.delete(cloud)
        cloud=canvas.create_image(550,50,anchor=NW,image=img[1])
    canvas.update()
score=0
text_score=canvas.create_text(550,30,text="SCORE:"+str(score),fill="blue",font=("Times",10))
def moveTree():
    global tree,score
    canvas.move(tree,-5,0)
    if canvas.coords(tree)[0]<-20:
        canvas.delete(tree)
        tree=canvas.create_image(550,250,anchor=NW,image=img[2])
        score=score+1
        canvas.itemconfig(text_score,text="SCORE:"+str(score))
    canvas.update()
check_jump=False
def jump():
    global check_jump
    if check_jump==False:
        check_jump=True
        for i in range(0,15):
            canvas.move(dragon,0,-5)
            moveCloud()
            moveTree()
            canvas.update()
            sleep(0.01)
        for i in range(0,15):
            canvas.move(dragon,0,5)
            moveCloud()
            moveTree()
            canvas.update()
            sleep(0.01)
        check_jump=False


def keyPress(event):
    if event.keysym=="space":
        jump()
canvas.bind_all("<KeyPress>",keyPress)
gameover=False
def playagain():
    pass


def check_Gameover():
    global gameover,text_gameover
    if canvas.coords(tree)[0]<50 and canvas.coords(dragon)[1]>220:
        gameover=True
        text_gameover = canvas.create_text(300, 120, text="GAMEOVER", fill="black", font=("Times", 20))
        text_gameover = canvas.create_text(300, 150, text=str(score), fill="red", font=("Times", 20))

    game.after(10,check_Gameover)

check_Gameover()
while not gameover:
    moveCloud()
    moveTree()
    sleep(0.01)
game.mainloop()