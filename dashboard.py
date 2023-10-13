from tkinter import  *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import *
import time
import teacher
import course
import datavw
import front
import Addstudent

# import database
import dashboard
# import tview
# import cview
# import sview
# import LoginPage
# import subject
import addnote

class main():
    

    def __init__(self):
    
        self.root=Tk()
        self.root.title("Recodir")
        # self.root.geometry('700x500')
        self.root.geometry('1910x1050')
        self.root.config(bg='white')
        self.root.resizable(False,False)
        #035995
        #frame1#3545f9
        self.frame1 = Frame(self.root, bg='#035995', width=300, height=1050)
        self.frame1.place(x=0, y=0)
        
        #logo
        self.img = Image.open('images/recodir.png').resize((220, 60))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.frame1, image = self.imgTk,bg='#035995')
        self.imgLbl.place(x = 33, y = 2)
        
        # homme
        self.lgn_button = Image.open('images\\homme.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=25,height=20,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=30, y=120)
        
        
        # self.lgn_button = Image.open('images\\btn5.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame1, image=photo, bg='#035995',width=300,height=50)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=80, y=110)
        self.login = Button(self.frame1, text='Home', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w',command=self.hom)
        self.login.place(x=80, y=110)
        
        #ADD TEACHER
        
        self.lgn_button = Image.open('images\\addstaff.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=195)
        
        # self.lgn_button = Image.open('images\\btn5.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame1, image=photo, bg='#035995',width=300,height=50)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=80, y=200)
        self.login = Button(self.frame1, text='Add Staff', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w',command=self.tech)
        self.login.place(x=80, y=200)
        
        
        #add COURSEself
        
        self.lgn_button = Image.open('images\\addcrs.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=285)
        
        # self.lgn_button = Image.open('images\\btn5.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame1, image=photo, bg='#035995',width=300,height=50)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=80, y=290)
        self.login = Button(self.frame1, text='Add Course', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w',command=self.crs)
        self.login.place(x=80, y=290)
        
        
        #add student
        self.lgn_button = Image.open('images\\addstudent.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=375)
        
        # self.lgn_button = Image.open('images\\btn5.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame1, image=photo, bg='#035995',width=300,height=50)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=80, y=380)
        self.login = Button(self.frame1, text='Add Student', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w',command=self.sTudent)
        self.login.place(x=80, y=380)
        
        #view attendence
        
        self.lgn_button = Image.open('images\\checked.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=460)
        
        # self.lgn_button = Image.open('images\\btn5.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame1, image=photo, bg='#035995',width=300,height=50)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=80, y=460)
        self.login = Button(self.frame1, text='Attendence', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995',anchor='w', fg='white')
        self.login.place(x=80, y=460)
        
        #add note
        
        self.lgn_button = Image.open('images\\addnote.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=545)
        
        # self.lgn_button = Image.open('images\\btn5.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame1, image=photo, bg='#035995',width=300,height=50)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=80, y=550)
        self.login = Button(self.frame1, text='Add Note', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995',anchor='w', fg='white',command=self.note)
        self.login.place(x=80, y=550)
        
        # DATA 
        
        self.lgn_button = Image.open('images\\viewc.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=640)
        
        # self.lgn_button = Image.open('images\\btn5.jpg')
        # photo = ImageTk.PhotoImage(self.lgn_button)
        # self.lgn_button_label = Label(self.frame1, image=photo, bg='#035995',width=300,height=50)
        # self.lgn_button_label.image = photo
        # self.lgn_button_label.place(x=80, y=640)
        self.login = Button(self.frame1, text='View Data', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995',anchor='w', fg='white',command=self.dviw)
        self.login.place(x=80, y=640)
        
    
        
        # logout
        
        self.lgn_button = Image.open('images\\exit.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=70,height=70,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=0, y=960)
        
        #edf2fa
        self.logout = Button(self.frame1, text="Logout", bg='#035995', font=("times new roman", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#035995',command=self.log)
        self.logout.place(x=60, y=980)
        
        
        
        
        #frame2
        #585556
        
        self.frame2 = Frame(self.root, bg='white', width=1600, height=1000)
        self.frame2.place(x=300, y=0)
        
        self.lbl=Label(self.frame2,text='Welcome Admin!',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,padx=50,anchor='w')
        self.lbl.place(x=1.5,y=15)
        
        
        # # nik
        # self.image = ImageTk.PhotoImage(file="images/cm.jpg")
        # self.dassimage = Label(self.frame2, image=self.image,height=400,width=700)
        # self.dassimage.place(x=470, y=300)

# time
        # self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        # self.date_time_image = Label(self.frame2, image=self.clock_image, bg='#3545f9')
        # self.date_time_image.place(x=670, y=6)
        
    #     self.date_time = Label(self.frame2)
    #     self.date_time.place(x=1500, y=0)
    #     self.show_time()

    # def show_time(self):
    #     self.time = time.strftime("%H:%M:%S",)
    #     self.date = time.strftime('%d/%h/%y')
    #     set_text = f"  {self.time} \n {self.date}"
    #     self.date_time.configure(text=set_text, font=("times new roman", 13, "bold"), bd=0, bg="#585556", fg="white")
    #     self.date_time.after(100, self.show_time)

        
        self.root.mainloop()
        
    def log(self):
        
        rs= messagebox.askyesno('Alert','Are you sure for logout?')
        if rs:
            self.root.destroy()
            front.main()
        else:
            return None
            

        
            
            
            
        
    def tech(self):
        teacher.Addteacher(self.frame2)
        
    def hom(self):
       
        self.frame2 = Frame(self.root, bg='white', width=1600, height=1000)
        self.frame2.place(x=300, y=0)
        
        self.lbl=Label(self.frame2,text='Welcome Admin!',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,padx=50,anchor='w')
        self.lbl.place(x=1.5,y=15)
        
        # self.image = ImageTk.PhotoImage(file="images/nik.jpg")
        # self.dassimage = Label(self.frame2, image=self.image,height=750,width=700)
        # self.dassimage.place(x=470, y=120)
        
        dashboard.main(self.frame2)
        # my_object = main()
        # my_object.method("foo")
        
    def crs(self):
        course.Addcourse(self.frame2)
        
    def dviw(self):
        datavw.dataview(self.frame2)
        
    def sTudent(self):
        Addstudent.student(self.frame2)
        
    def note(self):
        addnote.noteadd(self.frame2)

    
    
                
    def dash():
        root=Tk
        
if __name__=='__main__':
    obj=main()