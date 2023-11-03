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
        
        for i in database.selectcourse(data):
                    self.username_entry1.insert(0,i[1])
                 
                    self.subCombo1.insert(2,i[2])
            
                    # self.username_entry6.insert(6,i[7])
                    
#     def next_entry(self, event):
#         event.widget.tk_focusNext().focus()
    
    def courseupdate(self):
                self.data = (   
                                self.username_entry1.get(),
                                
                                self.subCombo1.get(),
                              
                                # self.username_entry6.get(),
                                self.id[0]
                        )

                if (self.username_entry1.get() == ''):
                        messagebox.showinfo('Alert', 'Please enter Name ')
              
                elif(self.subCombo1.get()== ''):
                        messagebox.showinfo('Alert', 'Please enter year')
               
                # elif(self.username_entry6.get()== ''):
                #         messagebox.showinfo('Alert', 'Please enter Password')
                
                else:
                        res = database.updatecourse(self.data)
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