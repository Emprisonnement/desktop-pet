
import tkinter as tk
from PIL import Image, ImageTk
import random

class DesktopPet:
    def __init__(self):
        self.root=tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.config(bg='white')
        try:
            self.root.wm_attributes('-transparentcolor','white')
        except:
            pass

        self.img=Image.open('pet.png')
        self.photo=ImageTk.PhotoImage(self.img)
        self.label=tk.Label(self.root,image=self.photo,bg='white',borderwidth=0)
        self.label.pack()

        self.msg=tk.Label(self.root,text='',bg='lightyellow')

        self.root.geometry('220x220+200+200')
        self.label.bind('<Button-1>', self.start_drag)
        self.label.bind('<B1-Motion>', self.drag)
        self.label.bind('<Button-3>', self.talk)
        self.label.bind('<Double-Button-1>', self.react)

        self.x=self.y=0
        self.idle()

    def start_drag(self,e):
        self.x=e.x; self.y=e.y

    def drag(self,e):
        nx=self.root.winfo_x()+e.x-self.x
        ny=self.root.winfo_y()+e.y-self.y
        self.root.geometry(f'+{nx}+{ny}')

    def react(self,e=None):
        self.show('喵~ 很高兴见到你!')
        self.root.geometry(f'240x240+{self.root.winfo_x()}+{self.root.winfo_y()}')
        self.root.after(500, lambda:self.root.geometry(f'220x220+{self.root.winfo_x()}+{self.root.winfo_y()}'))

    def talk(self,e=None):
        self.show(random.choice(['工作加油!','记得喝水~','今天也要开心','需要帮忙吗?']))

    def show(self,text):
        self.msg.config(text=text)
        self.msg.pack()
        self.root.after(3000, self.msg.pack_forget)

    def idle(self):
        dx=random.randint(-10,10)
        dy=random.randint(-5,5)
        self.root.geometry(f'+{self.root.winfo_x()+dx}+{self.root.winfo_y()+dy}')
        self.root.after(4000,self.idle)

    def run(self):
        self.root.mainloop()

DesktopPet().run()
