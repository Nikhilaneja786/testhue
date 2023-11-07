
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
# import re
import database

class st:
    def __init__(self) -> None:
        # self.id=data
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 
        
        
        
        self.lbl=Label(self.frame2,text='Add Staff',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,anchor='w',padx=90)
        self.lbl.place(x=650,y=0)
     
        
        #1  
        self.lb1=Label(self.frame2, text='Name',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='100')  
        
        self.username_entry1 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry1.place(x=100, y=145, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=170)  
        # self.username_entry1.bind('<Return>', self.next_entry)
        
         
        #2
        self.lb1=Label(self.frame2, text='D.O.B',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='200')    
        
        self.username_entry2 = DateEntry(self.frame2)
        self.username_entry2.place(x=100, y=250, width=500,height=30)
        self.username_entry2.config(state='readonly')
        # self.username_entry2.bind('<Return>', self.next_entry)
        
        #3
        self.lb1=Label(self.frame2, text='Contact',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='300')    
        
        
        self.username_entry3 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry3.place(x=100, y=355, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=380)
        # self.username_entry3.bind('<Return>', self.next_entry)
        
        #4
        self.lb1=Label(self.frame2, text='Qualification',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='400') 
        
        self.username_entry4 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry4.place(x=100, y=460, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=485)
        # self.username_entry4.bind('<Return>', self.next_entry)
        
        #5
        self.lb1=Label(self.frame2, text='Gender',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='500') 
        
        self.subCombo1 = Combobox(self.frame2, values = ['Male','Female','others'])
        self.subCombo1.set('Select Gender')
        self.subCombo1.config(state='readonly')
        self.subCombo1.pack()
        self.subCombo1.place(x=100, y=550,width=190,height=30)
        # self.subCombo1.bind('<Return>', self.next_entry)
        
        
        
        #6
        self.lb1=Label(self.frame2, text='Username',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='600') 
        
        self.username_entry5 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry5.place(x=100, y=650, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=675)
        
        # self.username_entry5.bind('<Return>', self.next_entry)
        
        #7
        self.lb1=Label(self.frame2, text='Password',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='700')
 
        self.username_entry6 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry6.place(x=100, y=750, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=775)
        # self.username_entry6.bind('<Return>', self.next_entry)
        
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
        
    
 

        for i in database.selectstaff():
                    self.username_entry1.insert(0,i[1])
                    # self.username_entry2.insert(1,i[2])
                    self.username_entry3.insert(2,i[3])
                    self.username_entry4.insert(3,i[4])
                    self.subCombo1.insert(4,i[5])
                    self.username_entry5.insert(5,i[6])
                    self.username_entry6.insert(6,i[7])
                    
#     def next_entry(self, event):
#         event.widget.tk_focusNext().focus()
    
    def staffUpdate(self):
                self.data = (   
                                self.username_entry1.get(),
                                self.username_entry2.get(),
                                self.username_entry3.get(),
                                self.username_entry4.get(),
                                self.subCombo1.get(),
                                self.username_entry5.get(),
                                self.username_entry6.get(),
                                # self.id[0]
                        )

                if (self.username_entry1.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Name ')
                elif(self.username_entry2.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter D.O.B')
                elif(self.username_entry3.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter contact')
                elif(self.username_entry4.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter Qualification')
                elif(self.subCombo1.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter Gender')
                elif(self.username_entry5.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter Username')
                elif(self.username_entry6.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter Password')
                
                else:
                        res = database.updatestaff(self.data)
                        print(res)
                        if res:
                                messagebox.showinfo('Success', 'Successfully Update')
                                # self.frame2.destroy()
                                self.frame2.destroy()
                                # self.obj=staffedit.estaff(gup)

                                # obj.destroy()
                                # homepage.ViewCategory()
                                # ViewCategory.viewCategory()
                        else:
                                messagebox.showinfo('Alert', 'Something went wrong.')
            



if __name__=='__main__':
    st() 
