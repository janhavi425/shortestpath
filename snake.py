import tkinter as tk
import random2
from PIL import Image,ImageTk  #allow to load img,place the img
p=20

class snack(tk.Canvas):
    def __init__(self):
        super().__init__(width=600,height=620,background="black",highlightthickness=0)

        self.sp = [(100,100),(80,100),(60,100)]
        self.fp = self.set_food()
        self.score=0
        self.d="Right"
        self.bind_all("<Key>",self.on_press)
        self.load_asserts()
        self.co()
        self.perform()


    def load_asserts(self):
        try:
            self.sbi = Image.open("./assets/snake.png")
            self.sb = ImageTk.PhotoImage(self.sbi)
            self.food = Image.open("./assets/food.png")
            self.sf = ImageTk.PhotoImage(self.food)
        except IOError as e:
            print(e)
            root.destroy()
    def co(self):
        #display score
        self.create_text(300,15,text=("score:",self.score),tag="score",fill="#fff",font=("Comic Sans", 25))

        for xp,yp in self.sp:
            self.create_image(xp,yp,image=self.sb,tag="snake")
        self.create_image(*self.fp, image=self.sf,tag="food")
        #creat boundary
        #self.create_rectangle(0,0,600,600,outline="#fff")
    def move(self):
        headx,heady=self.sp[0]
        if self.d=="Left":
            newhead=(headx-p,heady)
        elif self.d=="Right":
            newhead = (headx+p,heady)
        elif self.d == "Down":
            newhead = (headx, heady+p)
        elif self.d == "Up":
            newhead = (headx, heady-p)
        self.sp = [newhead]+self.sp[:-1]
        for seg,pos in zip(self.find_withtag("snake"),self.sp):
            self.coords(seg,pos)
    def perform(self):
        if self.collision():
            self.end()
            return
        self.food_collision()
        self.move()
        self.after(75,self.perform)
    def collision(self):
        headx, heady = self.sp[0]
        return(headx in (0,600) or heady in (20,620) or (headx, heady) in self.sp[1:])
    def on_press(self,e):
        nd=e.keysym
        ad = ("Up","Left","Right","Down")
        od = (("Up","Down"),("Left","Right"))
        if (nd in ad and (nd,self.d) not in od):
            self.d=nd
    def food_collision(self):
        if self.sp[0]==self.fp:
            self.score+=5
            self.sp.append(self.sp[-1])

            self.create_image(
                *self.sp[-1],image=self.sb,tag="snake"
            )
            self.fp = self.set_food()
            self.coords(self.find_withtag("food"),self.fp)
            score = self.find_withtag("score")
            self.itemconfigure(score,text=("score:",self.score),tag="score")
    def set_food(self):
        while True:
            xpos = random2.randint(1,29)*p
            ypos = random2.randint(3, 30) * p
            fp = (xpos,ypos)
            if fp not in self.sp:
                return fp
    def end(self):
        self.delete(tk.ALL)

        self.create_text(
            self.winfo_width()/2,
            self.winfo_height() / 2,
            text=f"Game over!\nyour score: {self.score}",
            fill="#fff",
            font=("Comic Sans", 24)

        )


root = tk.Tk()
root.title("SnackGame")
root.resizable(False,False)
b = snack()
b.pack()
root.mainloop()