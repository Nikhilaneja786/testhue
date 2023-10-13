from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
# import re
import database

class Addteacher:
    def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 
        
        
        
        self.lbl=Label(self.frame2,text='ADD STAFF',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,anchor='w',padx=90)
        self.lbl.place(x=1.5,y=0)
     
        
        #1  
        self.lb1=Label(self.frame2, text='Name',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='100')  
        
        self.username_entry1 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry1.place(x=100, y=145, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=170)  
        
        
         
        #2
        self.lb1=Label(self.frame2, text='D.O.B',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='200')    
        
        self.username_entry2 = DateEntry(self.frame2)
        self.username_entry2.place(x=100, y=250, width=500,height=30)
        self.username_entry2.config(state='readonly')
        
        
        #3
        self.lb1=Label(self.frame2, text='Contact',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='300')    
        
        
        self.username_entry3 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry3.place(x=100, y=355, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=380)
        
        
        #4
        self.lb1=Label(self.frame2, text='Qualification',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='400') 
        
        self.username_entry4 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry4.place(x=100, y=460, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=485)
        
        #5
        self.lb1=Label(self.frame2, text='Gender',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='500') 
        
        self.subCombo1 = Combobox(self.frame2, values = ['Male','Female','others'])
        self.subCombo1.set('Select Gender')
        self.subCombo1.config(state='readonly')
        self.subCombo1.pack()
        self.subCombo1.place(x=100, y=550,width=190,height=30)
        
        
        
        
        #6
        self.lb1=Label(self.frame2, text='Username',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='600') 
        
        self.username_entry5 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry5.place(x=100, y=650, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=675)
        
        
        
        #7
        self.lb1=Label(self.frame2, text='Password',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='700')
 
        self.username_entry6 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry6.place(x=100, y=750, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=775)

        
        # #040405#bdb9b1

        
        self.lgn_button = Image.open('images\\but.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame2, image=photo, bg='#ffffff')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=180, y=850)
        self.login = Button(self.lgn_button_label, text='ADD', font=('monoco', 13, "bold"), width=25, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',command=self.addstaff)
        
        #3047ff
        self.login.place(x=18, y=8)
        
        
    def addstaff(self):
        if self.username_entry1.get() and self.username_entry2.get() and self.username_entry3.get() and self.username_entry4.get() and self.subCombo1.get() and self.username_entry5.get() and self.username_entry6.get():
            res=database.addstaff((self.username_entry1.get(),self.username_entry2.get(), self.username_entry3.get(),self.username_entry4.get(),self.subCombo1.get(),self.username_entry5.get(), self.username_entry6.get()))
            if res:
                messagebox.showinfo('success',' Add successfully')
            else:
                messagebox.showinfo('alert','something went wrong')
        else:
                messagebox.showinfo('alert','please enter your details')
            
    
# def validate_phone_number(phone_number):
#     # Define a regular expression pattern for a common phone number format
#     pattern = r'^\d{3}-\d{3}-\d{4}$'  # Example: 123-456-7890

#     # Use the re.match() function to check if the input matches the pattern
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False

# # Test the function
# phone_number = "123-456-7890"
# if validate_phone_number(phone_number):
#     print(f"{phone_number} is a valid phone number.")
# else:
#     print(f"{phone_number} is not a valid phone number.")



if __name__=='__main__':
    Addteacher() 
