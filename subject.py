from tkinter import *
# from tkinter import messagebox
from PIL import Image, ImageTk
# import database

class Addsubject:
    def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 
     
        self.lbl=Label(self.frame2,text='ADD SUBJECTS',bg='#585556',fg='white',font=('times new roman',24,'bold'),width=85)
        self.lbl.place(x=1.5,y=0)
        
            
        self.lb1=Label(self.frame2, text='COURSE',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='210',y='130')     
        
        self.lb1=Label(self.frame2, text='NAME',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='210',y='180')    
        
        self.lb1=Label(self.frame2, text='DESCRIPTION',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        self.lb1.place(x='210',y='230')    
        
        # self.lb1=Label(self.frame2, text='QUALIFICATION',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        # self.lb1.place(x='210',y='280') 
        
        # self.lb1=Label(self.frame2, text='USERNAME',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        # self.lb1.place(x='210',y='330') 
        
        # self.lb1=Label(self.frame2, text='PASSWORD',bg='white',fg='#585556',font=('times new roman',20,'bold'))
        # self.lb1.place(x='210',y='380')
 
        # self.image = ImageTk.PhotoImage(file="images/butt.png")
        # self.dassimage = Label(self.frame2, image=self.image,bg='white')
        # self.dassimage.place(x=120, y=20)
        
        # self.lb1=Label(self.frame2, text='ADD PRODUCT',bg='#195ea8',fg='#2ff3d0',font=('monaco',20,'bold'))
        # self.lb1.place(x='80',y='20')     

        # self.lb2=Label(self.frame2, text='Category',bg='#195ea8',fg='#2ff3d0',font=('monaco',18))
        # self.lb2.place(x='45',y='76')
        self.lb2entry=Entry(self.frame2)
        self.lb2entry.place(x='480',y='130')
        
        self.lb2entry=Entry(self.frame2)
        self.lb2entry.place(x='480',y='180')

        self.lb2entry=Entry(self.frame2)
        self.lb2entry.place(x='480',y='230')

        # self.lb2entry=Entry(self.frame2)
        # self.lb2entry.place(x='480',y='290')

        # self.lb2entry=Entry(self.frame2)
        # self.lb2entry.place(x='480',y='340')

        # self.lb2entry=Entry(self.frame2)
        # self.lb2entry.place(x='480',y='390')
        
        self.lgn_button = Image.open('images\\btn3.jpg')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame2, image=photo, bg='white')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=260, y=440)
        self.login = Button(self.lgn_button_label, text='ADD', font=('monoco', 13, "bold"), width=25, bd=0,
                            bg='#555555', cursor='hand2', activebackground='#555555', fg='white')
        
        
        self.login.place(x=20, y=12)
    #     self.lb3=Label(self.frame2, text='Name',bg='#195ea8',fg='#2ff3d0',font=('monaco',18))
    #     self.lb3.place(x='45',y='126')
    #     self.lb3entry=Entry(self.frame2)
    #     self.lb3entry.place(x='165',y='130')

    #     self.lb4=Label(self.frame2, text='Price',bg='#195ea8',fg='#2ff3d0',font=('monaco',18))
    #     self.lb4.place(x='45',y='176')
    #     self.lb4entry=Entry(self.frame2)
    #     self.lb4entry.place(x='165',y='180')

    #     self.lb5=Label(self.frame2, text='Stock',bg='#195ea8',fg='#2ff3d0',font=('monaco',18))
    #     self.lb5.place(x='45',y='226')
    #     self.lb5entry=Entry(self.frame2)
    #     self.lb5entry.place(x='165',y='230')

    #     self.lb6=Label(self.frame2, text='Code',bg='#195ea8',fg='#2ff3d0',font=('monaco',18))
    #     self.lb6.place(x='45',y='276')
    #     self.lb6entry=Entry(self.frame2)
    #     self.lb6entry.place(x='165',y='280')

    #     self.addbtn=Button(self.frame2, text=' ADD ',bg='#195ea8',fg='#2ff3d0',font=('monaco',14,'bold'),command=self.AddProduct)
    #     self.addbtn.place(x=160,y=340)

    # def AddProduct(self):
    #     if self.lb2entry.get() and self.lb3entry.get() and self.lb4entry.get() and self.lb5entry.get() and self.lb6entry.get():
    #         res= database.Product((self.lb2entry.get(),self.lb3entry.get(),self.lb5entry.get(),self.lb6entry.get()))
    #         if res:
    #             messagebox.showinfo('success',' Add successfully')
    #         else:
    #             messagebox.showinfo('alert','something went wrong')
    #     else:
    # #             messagebox.showinfo('alert','please enter your details')
    # def dest(self):
    #     self.frame2.destroy()
if __name__=='__main__':
    Addsubject() 
