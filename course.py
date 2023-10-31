from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import database
from tkinter.ttk import Combobox

# import database

class Addcourse:
    def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 
     
     
        self.lbl=Label(self.frame2,text='Add Course',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,anchor='w',padx=90)
        self.lbl.place(x=650,y=0)
     
        
        #1
        self.lb1=Label(self.frame2, text='Name',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='100')     
        
        self.username_entry1 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry1.place(x=100, y=145, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=170)
        
        
        #2
        self.lb1=Label(self.frame2, text='Duration',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='200')   
        
        self.subCombo1 = Combobox(self.frame2, values = ['1 YEAR','2 YEARS','3 YEARS', '4 YEARS'])
        self.subCombo1.set('Select years')
        self.subCombo1.config(state='readonly')
        self.subCombo1.pack()
        self.subCombo1.place(x=100, y=260,width=190,height=30) 

        # #040405#bdb9b1

        #button
        self.lgn_button = Image.open('images\\but.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame2, image=photo, bg='#ffffff')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=90, y=350)
        self.login = Button(self.lgn_button_label, text='ADD', font=('monoco', 13, "bold"), width=24, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',command=self.Addcourse)
        
        #3047ff
        self.login.place(x=18, y=8)
        
    def Addcourse(self):
     
        if self.username_entry1.get() and self.subCombo1.get():
            res=database.Addcourse((self.username_entry1.get(),self.subCombo1.get()))
            if res:
                messagebox.showinfo('success',' Add successfully')
            else:
                messagebox.showinfo('alert','something went wrong')
        else:
                messagebox.showinfo('alert','please enter your details')
        
if __name__=='__main__':
    Addcourse() 
