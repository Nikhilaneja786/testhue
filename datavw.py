from tkinter import *
# from tkinter import messagebox
from PIL import Image, ImageTk
import sview
import tview
import cview
import vnote
# import database

class dataview:
    def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 
        
        self.btn_frame=Frame(self.frame2,bd=5,relief=RIDGE,bg='white')
        self.btn_frame.place(x=20,y=10,width=1570,height=65)
        
        # self.lgn_button = Image.open('images\\red.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame2, image=photo, bg='#ff3332',width=250)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=10, y=30)
        
        #view course
        self.login = Button(self.btn_frame, text='View Course', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',command=self.cviw)
        self.login.place(x=70, y=8)
        
        
        # self.lgn_button = Image.open('images\\yellow.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame2, image=photo, bg='#ff9932',width=250)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=300, y=30)
        
        #view student
        self.login = Button(self.btn_frame, text='View Student', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',command=self.sviw)
        self.login.place(x=370, y=8)
        
        
        
        
        # self.lgn_button = Image.open('images\\blue1.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame2, image=photo, bg='#035995',width=250)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=590, y=30)
        
        #view staff
        self.login = Button(self.btn_frame, text='View Staff', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',command=self.tviw)
        self.login.place(x=670, y=8)
        
        
        # view note
        self.login = Button(self.btn_frame, text='View Note', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',command=self.nviw)
        self.login.place(x=970, y=8)
        
        
        # view leave
        self.login = Button(self.btn_frame, text='View Leave', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white')
        self.login.place(x=1270, y=8)
        
        
    def sviw(self):
        sview.sw(self.frame2)
        
    def tviw(self):
        tview.vwt(self.frame2)
        
    def cviw(self):
        cview.cw(self.frame2)
        
    def nviw(self):
        vnote.nw(self.frame2)
        
        
if __name__=='__main__':
    dataview() 