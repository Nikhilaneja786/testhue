from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from datetime import *
import time
import database

# import database

class noteadd:
    def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 
     
    
        self.lbl=Label(self.frame2,text='Add Notice',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,anchor='w',padx=90)
        self.lbl.place(x=650,y=0)
     
       
      
        
        
        #1
        self.lb1=Label(self.frame2, text='Title',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='95')   
        
        self.username_entry1 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry1.place(x=100, y=150, width=800)
        self.username_line = Canvas(self.frame2, width=800, height=1.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=175)  
        self.username_entry1.bind('<Return>', self.next_entry)
        # #040405#bdb9b1
        
        #2
        self.lb1=Label(self.frame2, text='Description',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='210') 
        
        self.username_entry2 = Text(self.frame2, bg="white", fg="#585556",relief=SOLID,font=("yu gothic ui ", 14, "bold"),bd=1)
        self.username_entry2.place(x=100, y=255, width=800,height=300)
        # self.username_line = Canvas(self.frame2, width=800, height=2.0, bg="#585556", highlightthickness=0)
        # self.username_line.place(x=100, y=590)
        self.username_entry2.bind('<Return>', self.next_entry)

        #button#585556"
        
        self.lgn_button = Image.open('images\\but.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame2, image=photo, bg='#ffffff')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=100, y=650)
        self.login = Button(self.lgn_button_label, text='ADD', font=('monoco', 13, "bold"), width=25, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995',pady=-1, fg='white',command=self.Addnote)
        
        #3047ff
        self.login.place(x=20, y=12)
    def next_entry(self, event):
        event.widget.tk_focusNext().focus()
        
    def Addnote(self):
     
        if self.username_entry1.get() and self.username_entry2.get("1.0","end-1c"):
            res=database.Addnote((self.username_entry1.get(),self.username_entry2.get("1.0","end-1c")))
            if res:
                messagebox.showinfo('success',' Add successfully')
            else:
                messagebox.showinfo('alert','something went wrong')
        else:
                messagebox.showinfo('alert','please enter your details')
        
        
        
if __name__=='__main__':
    noteadd() 
