from tkinter import  *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import *
import time
# import teacher
# import course
# import datavw
import front
# import Addstudent
# import dashboard
# import addholiday
import database
# import addnote
import time
# from tkcalendar import DateEntry
# from datetime import datetime
# from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar

class td():
    def __init__(self):
    
        self.root=Tk()
        self.root.title("main")
        # self.root.geometry('700x500')
        self.root.geometry('1910x1050')
        self.root.config(bg='white')
        self.root.resizable(False,False)
        
        #frame1#3545f9  035995
        self.frame1 = Frame(self.root, bg='#035995', width=300, height=1050)
        self.frame1.place(x=0, y=0)
        
        #logo
        self.img = Image.open('images/recodir.png').resize((220, 60))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.frame1, image = self.imgTk,bg='#035995')
        self.imgLbl.place(x = 33, y = 2)
        
        #home
        self.lgn_button = Image.open('images\\homme.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=25,height=20,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=30, y=110)
        
        
   
        self.login = Button(self.frame1, text='Home', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w')
        self.login.place(x=80, y=100)
        
        
        
        #Attendence
        
        self.lgn_button = Image.open('images\\attendance.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=185)
 
        self.login = Button(self.frame1, text='Attendence ', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w')
        self.login.place(x=80, y=190)
        
        
        #add leave
        
        self.lgn_button = Image.open('images\\addnote.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=275)
        
      
        self.login = Button(self.frame1, text='Addd Leave', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w')
        self.login.place(x=80, y=280)
        
        
        #add note
        self.lgn_button = Image.open('images\\viewc.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=365)
     
        self.login = Button(self.frame1, text='View Data', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w')
        self.login.place(x=80, y=370)
        
        
        # logout
        
        self.lgn_button = Image.open('images\\exit.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=70,height=70,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=0, y=960)
        
        #edf2fa
        self.logout = Button(self.frame1, text="Logout", bg='#035995', font=("times new roman", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#035995')
        self.logout.place(x=60, y=980)
        
        self.frame2 = Frame(self.root, bg='white', width=1600, height=1000)
        self.frame2.place(x=300, y=0)
        
        self.lbl=Label(self.frame2,text='Welcome Teacher!',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,padx=50,anchor='w')
        self.lbl.place(x=1.5,y=15)

        
    
        # cal=Calendar(self.frame2)
        # cal = Calendar(self.frame2, font="Arial 13", selectmode='day', locale='en_US',
        #        cursor="hand2")
        # cal.place(x=1150,y=490)
        
        
        
        
        #addstaff
        self.lgn_button = Image.open('images\\dashbut2.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label1 = Label(self.frame2, image=photo,width=350,height=280,bg='#ffffff')
        self.lgn_button_label1.image = photo
        self.lgn_button_label1.place(x=100, y=80)
        
        count=0
        for data in database.Tstaff():
            count+=1
            
        self.countTeacher=Label(self.lgn_button_label1,text=count,bg='#FF91A5',fg='black',font=('',15,'bold'))
        # print(count)
        self.countTeacher.place(x=215,y=110)
        
        
        #showstudent
        self.lgn_button = Image.open('images\\dashbut.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label2 = Label(self.frame2, image=photo,width=350,height=280,bg='#ffffff')
        self.lgn_button_label2.image = photo
        self.lgn_button_label2.place(x=440, y=80)
        
        
        count=0
        for data in database.Studenteview():
            count+=1
            
        self.countTeacher=Label(self.lgn_button_label2,text=count,bg='#ffcd5e',fg='black',font=('',15,'bold'))
        # print(count)
        self.countTeacher.place(x=215,y=110)
       
        
        
        
        #addcourse
        self.lgn_button = Image.open('images\\dashbut3.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label3 = Label(self.frame2, image=photo,width=350,height=280,bg='#ffffff')
        self.lgn_button_label3.image = photo
        self.lgn_button_label3.place(x=780, y=80)
        
        
        
        count=0
        for data in database.courseview():
            count+=1
            
        self.countTeacher=Label(self.lgn_button_label3,text=count,bg='#95ff93',fg='black',font=('',15,'bold'))
        # print(count)
        self.countTeacher.place(x=215,y=110)
        
        
        
        
        #addnote
        self.lgn_button = Image.open('images\\but5.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label4 = Label(self.frame2, image=photo,width=350,height=280,bg='#ffffff')
        self.lgn_button_label4.image = photo
        self.lgn_button_label4.place(x=1160, y=80)
        
        
        count=0
        for data in database.vnote():
            count+=1
            
        self.countTeacher=Label(self.lgn_button_label4,text=count,bg='#38ABFE',fg='black',font=('',15,'bold'))
        # print(count)
        self.countTeacher.place(x=200,y=110)

        #frame
        self.frame3 = Frame(self.frame2, bg='white',highlightbackground='black',highlightthickness=2, width=580, height=450)
        self.frame3.place(x=150, y=450)

        self.lbl=Label(self.frame3,text='Staff-Students Ratio',bg='#035995',fg='white',font=('times new roman',24,'bold'),width=29,padx=11,anchor='w')
        self.lbl.place(x=0,y=0)

        self.date_time = Label(self.frame3)
        self.date_time.place(x=10, y=42)
        self.create_pie_chart()

        self.frame4 = Frame(self.frame2, bg='white',highlightbackground='black',highlightthickness=2, width=580, height=450)
        self.frame4.place(x=860, y=450)


        self.lbl=Label(self.frame4,text='Data-Count',bg='#035995',fg='white',font=('times new roman',24,'bold'),width=29,padx=11,anchor='w')
        self.lbl.place(x=0,y=0)
        
        self.date_time1 = Label(self.frame4)
        self.date_time1.place(x=20, y=42)
        self.create_bar_chart()


        self.date_time= Label(self.frame2)
        self.date_time.place(x=1400, y=30)
        self.show_time()
    
        
        self.root.mainloop()
        
    def show_time(self):
        self.time = time.strftime("%H:%M:%S",)
        self.date = time.strftime('%d/%h/%y')
        set_text = f"  {self.time} \n{self.date}"
        self.date_time.configure(text=set_text, font=("times new roman", 20, "bold"), bd=0, bg="white", fg="#035995")
        self.date_time.after(100, self.show_time)


    def create_pie_chart(self):
        staff_count, student_count = database.pieview()  # Call the function to get the counts

        labels = ['Student', 'Staff']
        sizes = [student_count, staff_count]
        colors = ['#ffcd5e', 'lightcoral']

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=150)
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self.frame3)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=10, y=42)


    # Handle the error condition

    
    def create_bar_chart(self):
        # Data for the bar chart
        # categories = ['Staff', 'Students', 'Course', 'Notice']
        # values = [3,1,4,1]
        
        staff_count, student_count ,course_count,addnote = database.barview()  # Call the function to get the counts

        categories = ['Staff', 'Students', 'Course', 'Notice']
        values= [staff_count, student_count ,course_count,addnote]
        # colors = ['#ffcd5e', 'lightcoral', 'blue', 'orange']
        colors = ['lightcoral', '#ffcd5e', '#95ff93', 'lightskyblue']
        # Create a figure and axis for the bar chart
        fig, ax = plt.subplots(figsize=(5,4))
        ax.bar(categories, values, color=colors)
        # ax.bar.set_edgecolor(ax.bar.get_facecolor())
        # plt.figure(figsize=(5, 4))
        # Add labels and title
        ax.set_xlabel('Names')
        ax.set_ylabel('Values')
        # ax.set_title('Bar Chart Example')

        # Embed the bar chart in a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.frame4)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=20,y=42)
  
    
    def log(self):
        
        rs= messagebox.askyesno('Alert','Are you sure for logout?')
        if rs:
            self.root.destroy()
            front.main()
        else:
            return None
        
        
        #frame2
        #585556
        
#         self.frame2 = Frame(self.root, bg='white', width=1600, height=1000)
#         self.frame2.place(x=300, y=0)
        
#         self.lbl=Label(self.frame2,text='Welcome Staff!',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,padx=50,anchor='w')
#         self.lbl.place(x=1.5,y=15) 
        
        
#         self.lgn_button = Image.open('images\\dashbut2.png')
#         photo = ImageTk.PhotoImage(self.lgn_button)
#         self.lgn_button_label = Label(self.frame2, image=photo,width=350,height=280,bg='#ffffff')
#         self.lgn_button_label.image = photo
#         self.lgn_button_label.place(x=150+60, y=80)
        
        
#         self.lgn_button = Image.open('images\\dashbut.png')
#         photo = ImageTk.PhotoImage(self.lgn_button)
#         self.lgn_button_label = Label(self.frame2, image=photo,width=350,height=280,bg='#ffffff')
#         self.lgn_button_label.image = photo
#         self.lgn_button_label.place(x=150+460, y=80)
        
#         self.lgn_button = Image.open('images\\dashbut3.png')
#         photo = ImageTk.PhotoImage(self.lgn_button)
#         self.lgn_button_label = Label(self.frame2, image=photo,width=350,height=280,bg='#ffffff')
#         self.lgn_button_label.image = photo
#         self.lgn_button_label.place(x=150+860, y=80)
        
#         # self.image = ImageTk.PhotoImage(file="images/nik.jpg")
#         # self.dassimage = Label(self.frame2, image=self.image,height=750,width=700)
#         # self.dassimage.place(x=470, y=120)

# # time
#         # self.clock_image = ImageTk.PhotoImage(file="images/time.png")
#         # self.date_time_image = Label(self.frame2, image=self.clock_image, bg='#3545f9')
#         # self.date_time_image.place(x=670, y=6)
        
#     #     self.date_time = Label(self.frame2)
#     #     self.date_time.place(x=1500, y=0)
#     #     self.show_time()

#     # def show_time(self):
#     #     self.time = time.strftime("%H:%M:%S",)
#     #     self.date = time.strftime('%d/%h/%y')
#     #     set_text = f"  {self.time} \n {self.date}"
#     #     self.date_time.configure(text=set_text, font=("times new roman", 13, "bold"), bd=0, bg="#585556", fg="white")
#     #     self.date_time.after(100, self.show_time)

        
#         self.root.mainloop()
        
#     # def log(self):
#     #     print('button is clicked')
#     #     rs=1 
#     #     if rs==1:
                
#     #         self.root.destroy()
#     #         front.main()
        
#     # def tech(self):
#     #     teacher.Addteacher(self.frame2)
        
    # def hom(self):
       
    #     self.frame2 = Frame(self.root, bg='white', width=1600, height=1000)
    #     self.frame2.place(x=300, y=0)
        
    #     self.lbl=Label(self.frame2,text='WELCOME ADMIN !',bg='#585556',fg='white',font=('times new roman',24,'bold'),width=95)
    #     self.lbl.place(x=1.5,y=0)
        
    #     self.image = ImageTk.PhotoImage(file="images/nik.jpg")
    #     self.dassimage = Label(self.frame2, image=self.image,height=750,width=700)
    #     self.dassimage.place(x=470, y=120)
        
    #     dashboard.main(self.frame2)

        
        
    # def crs(self):
    #     course.Addcourse(self.frame2)
        
    # def dviw(self):
    #     datavw.dataview(self.frame2)
        
    # def sTudent(self):
    #     Addstudent.student(self.frame2)
        
    # def note(self):
    #     addnote.noteadd(self.frame2)
    
    # def dash():
    #     root=Tk
        
if __name__=='__main__':
    obj=td()