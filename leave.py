from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# from tkinter.ttk import Combobox
from tkcalendar import DateEntry
# from datetime import *
# import time
import database
import re
# import database

class holiadd:
    def __init__(self,frame2) -> None:
        self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 
     
    
        self.lbl=Label(self.frame2,text='Add leave',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,anchor='w',padx=90)
        self.lbl.place(x=650,y=0)
     
       
      
        
        
        #1
        self.lb1=Label(self.frame2, text='Name',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='95')   
        # def is_alphabet(input_str):
        #     return bool(re.match("^[a-zA-Z]+$", input_str))

        # self.validate_alphabet = self.frame2.register(is_alphabet)
        self.username_entry1 = Entry(self.frame2,validate="key", validatecommand=(self.frame2.register(self.validate_alpha),"%P"),highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry1.place(x=100, y=150, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=175)  
        self.username_entry1.bind('<Return>', self.next_entry)

# self.username_entry1 = Entry(self.frame2, validate="key", validatecommand=(self.validate_alphabet, "%P"),
#                                       highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
#                                       font=("yu gothic ui ", 14, "bold"), insertbackground='#6b6a69')
#         self.username_entry1.place(x=100, y=145, width=500)
#         self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
#         self.username_line.place(x=100, y=170)
        # #040405#bdb9b1
        
        #2
        self.lb1=Label(self.frame2, text='reason',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='210') 
        # def is_alphabet(input_str):
        #     return bool(re.match("^[a-zA-Z]+$", input_str))

        # self.validate_alphabet = self.frame2.register(is_alphabet)
        self.username_entry2 = Entry(self.frame2,validate="key", validatecommand=(self.frame2.register(self.validate_alpha),"%P"), highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry2.place(x=100, y=265, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=290)
        self.username_entry2.bind('<Return>', self.next_entry)
        
        self.lb1=Label(self.frame2, text='Start Date',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='325') 
        
        self.username_entry3 = DateEntry(self.frame2)
        self.username_entry3.place(x=100, y=405, width=500,height=30)
        self.username_entry3.config(state='readonly')


        self.lb1=Label(self.frame2, text='End Date',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='440') 
        
        self.username_entry4 = DateEntry(self.frame2)
        # self.username_entry4.insert(0,'dd/mm/yyyy')
        self.username_entry4.place(x=100, y=520, width=500,height=30)
        self.username_entry4.config(state='readonly')
        
        self.lgn_button = Image.open('images\\but.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame2, image=photo, bg='#ffffff')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=90, y=650)
        self.login = Button(self.lgn_button_label, text='ADD', font=('monoco', 13, "bold"), width=25, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995',pady=-1, fg='white',command=self.Addl)
        
        #3047ff
        self.login.place(x=20, y=12)
    def next_entry(self, event):
        event.widget.tk_focusNext().focus()
        
    def Addl(self):
     
        if self.username_entry1.get() and self.username_entry2.get() and self.username_entry3.get() and self.username_entry4.get():
            # s=self.username_entry3.get()
            # print(s)
            # n=self.username_entry4.get()
            # print(n)
            res=database.Addl((self.username_entry1.get(),self.username_entry2.get(), self.username_entry3.get(),self.username_entry4.get()))
            if res:
                messagebox.showinfo('success',' Add successfully')
            else:
                messagebox.showinfo('alert','something went wrong')
        else:
                messagebox.showinfo('alert','please enter your details')
                
    def validate_alpha(self,P):
        if P.isalpha() or P == "":
            return True
        else:
            messagebox.showerror("Invalid Input", "Please enter alphabetic characters only.")
            return False
        
if __name__=='__main__':
    holiadd() 
