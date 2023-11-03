from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
# import re
import database
# import tview

class estudent():
    def _init_(self,data):
        # self.frame2 = frame2 
        self.id= data

        # self.frame2=Frame(width='1610',height='1050',bg='white')
        # self.frame2.place(x='300',y='0')

        # self.frame2=Frame(width='350',height='400',bg='#0a1b23')
        # self.frame2.place(x='330',y='100') 

        # self.frame2=Frame(width='380',height='450',bg='#0a1b23')
        # self.frame2.place(x='430',y='100')
        
        
        
        
        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 
        
        
        
        self.lbl=Label(self.frame2,text='Add Student',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,anchor='w',padx=90)
        self.lbl.place(x=1.5,y=0)
     
        
        self.lb1=Label(self.frame2, text='Name',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='110')     
        
        self.username_entry1 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry1.place(x=100, y=155, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=180)
        # self.username_entry1.bind('<Return>', self.next_entry) 
        
        #2
        self.lb1=Label(self.frame2, text='D.O.B',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='210')    
        
        self.username_entry2 = DateEntry(self.frame2)
        self.username_entry2.place(x=100, y=260, width=500,height=30)
        self.username_entry2.config(state='readonly')
        # self.username_entry2.bind('<Return>', self.next_entry)
        
        #3
        self.lb1=Label(self.frame2, text='Contact',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='310')   
        
        self.username_entry3= Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry3.place(x=100, y=365, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=390)
        # self.username_entry3.bind('<Return>', self.next_entry)
        
        #4
        self.lb1=Label(self.frame2, text='Address',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='410')
 
        self.username_entry4= Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
                                    font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        self.username_entry4.place(x=100, y=460, width=500)
        self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        self.username_line.place(x=100, y=490)
        # self.username_entry4.bind('<Return>', self.next_entry)
        
        #5
        self.lb1=Label(self.frame2, text='Gender',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='535') 
        
        self.subCombo1 = Combobox(self.frame2, values = ['Male','Female','others'])
        self.subCombo1.set('Select Gender')
        self.subCombo1.config(state='readonly')
        self.subCombo1.pack()
        self.subCombo1.place(x=250, y=540,width=190,height=30)
        
        # self.subCombo1.bind('<Return>', self.next_entry)
        #6
        self.lb1=Label(self.frame2, text='Course',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='95',y='635')
        
        self.course=database.COMBOCOURSE()
        self.subCombo2= Combobox(self.frame2,value=self.course)
        self.subCombo2.set('Select course')
        self.subCombo2.config(state='readonly')
        self.subCombo2.pack()
        self.subCombo2.place(x=250, y=640,width=190,height=30)
        # self.subCombo2.bind('<Return>', self.next_entry)
        
        
        # #7
        # self.lb1=Label(self.frame2, text='Password',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        # self.lb1.place(x='95',y='700')
 
        # self.username_entry6 = Entry(self.frame2, highlightthickness=0, relief=FLAT, bg="white", fg="#585556",
        #                             font=("yu gothic ui ", 14, "bold"), insertbackground = '#6b6a69')
        # self.username_entry6.place(x=100, y=750, width=500)
        # self.username_line = Canvas(self.frame2, width=500, height=2.0, bg="#585556", highlightthickness=0)
        # self.username_line.place(x=100, y=775)

        
        # #040405#bdb9b1

        
        self.lgn_button = Image.open('images\\but.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame2, image=photo, bg='#ffffff')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=180, y=850)
        self.login = Button(self.lgn_button_label, text='ADD', font=('monoco', 13, "bold"), width=25, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',command=self.staffUpdate)
        
        #3047ff
        self.login.place(x=18, y=8)
        #############
        # self.lb1=Label(self.frame2, text='Edit Staff',bg='#00c4ac',fg='#050e15',font=('Times New Roman',15,'bold'),pady=5, padx = 130)
        # self.lb1.place(x='0',y='20')   

        # self.lb2=Label(self.frame2, text='Name',bg='#0a1b23',fg='#00c4ac',font=('Times New Roman',15,'bold'), padx = 40)
        # self.lb2.place(x='25',y='116')
        # self.lb2entry = Entry(self.frame2)
        # self.lb2entry.place(x='200', y='122')
        # # self.lb2entry.bind('<Return>', self.next_entry)  

        # self.lb3=Label(self.frame2, text='Tax',bg='#0a1b23',fg='#00c4ac',font=('Times New Roman',15,'bold'), padx = 50)
        # self.lb3.place(x='25',y='176')
        # self.lb3entry = Entry(self.frame2)
        # self.lb3entry.place(x='200', y='180')
        # # self.lb3entry.bind('<Return>', self.next_entry)  

       
        # self.addbtn=Button(self.frame2, text='Update',bg='#0a1b23',fg='#00c4ac',font=('Times New Roman',15,'bold'), padx = 20,command=self.CatUpdate,cursor='hand2')
        # self.addbtn.place(x=65,y=280)

        # self.addbtn=Button(self.frame2, text='Clear',bg='#0a1b23',fg='#00c4ac',font=('Times New Roman',15,'bold'), padx = 20,command=lambda:print(self.lb2entry.delete(0,END) ,self.lb3entry.delete(0,END)),cursor='hand2')
        # self.addbtn.place(x=225,y=280)
        
        for i in database.selectstudent(data):
                    self.username_entry1.insert(0,i[1])
                    self.username_entry2.insert(1,i[2])
                    self.username_entry3.insert(2,i[3])
                    self.username_entry4.insert(3,i[4])
                    self.subCombo1.insert(4,i[5])
                    self.subCombo2.insert(5,i[6])
                    # self.username_entry6.insert(6,i[7])
                    
#     def next_entry(self, event):
#         event.widget.tk_focusNext().focus()
    
    def studentupdate(self):
                self.data = (   
                                self.username_entry1.get(),
                                self.username_entry2.get(),
                                self.username_entry3.get(),
                                self.username_entry4.get(),
                                self.subCombo1.get(),
                                self.subCombo2.get(),
                                # self.username_entry6.get(),
                                self.id[0]
                        )

                if (self.username_entry1.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Name ')
                elif(self.username_entry2.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter D.O.B')
                elif(self.username_entry3.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter contact')
                elif(self.username_entry4.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter address')
                elif(self.subCombo1.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter Gender')
                elif(self.subCombo2.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter course')
                # elif(self.username_entry6.get()== ''):
                #         messagebox.showinfo('Alert', 'Please enter Password')
                
                else:
                        res = database.updatestudent(self.data)
                        print(res)
                        if res:
                                messagebox.showinfo('Success', 'Successfully Update')
                                # self.frame2.destroy()
                                # self.frame2.destroy()
                                # self.obj=staffedit.estaff(gup)

                                # obj.destroy()
                                # homepage.ViewCategory()
                                # ViewCategory.viewCategory()
                        else:
                                messagebox.showinfo('Alert', 'Something went wrong.')
                                
                                
                                


    
if __name__=='__main__':
    estudent()