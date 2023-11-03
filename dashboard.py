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
import dashboard
import addholiday
import database
import addnote
import time
# from tkcalendar import DateEntry
# from datetime import datetime
# from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Canvas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar

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
        
        
        
#         data={'c':20,'x':9,'i':10}
#         # course=list(data.keys())
#         courses = list(data.keys())

#         values = list(data.values())

  

#         fig = plt.figure(figsize = (5, 5))
 
# # creating the bar plot

#         plt.bar(courses, values, color ='maroon', 

#         width = 0.4)
 

#         plt.xlabel("Courses offered")

#         plt.ylabel("No. of students enrolled")

#         plt.title("Students enrolled in different courses")
#         plt.show()
        
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

        self.login = Button(self.frame1, text='Home', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w',command=self.hom)
        self.login.place(x=80, y=110)
        
        #ADD TEACHER
        
        self.lgn_button = Image.open('images\\addstaff.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=195)
 
        self.login = Button(self.frame1, text='Add Staff', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w',command=self.tech)
        self.login.place(x=80, y=200)
        
        
        
        #add COURSEself
        self.lgn_button = Image.open('images\\addcrs.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=285)
   
        self.login = Button(self.frame1, text='Add Course', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w',command=self.crs)
        self.login.place(x=80, y=290)
        
        
        
        
        #add student
        self.lgn_button = Image.open('images\\addstudent.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=375)

        self.login = Button(self.frame1, text='Add Student', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',anchor='w',command=self.sTudent)
        self.login.place(x=80, y=380)
        
        
        
        #view attendence
        self.lgn_button = Image.open('images\\holiday.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=455)

        self.login = Button(self.frame1, text='Add Holiday', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995',anchor='w', fg='white',command=self.holiday)
        self.login.place(x=80, y=460)
        
        
        
        #add note
        self.lgn_button = Image.open('images\\addnote.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=545)
        
  
        self.login = Button(self.frame1, text='Add Notice', font=("times new roman", 18, "bold"), width=13, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995',anchor='w', fg='white',command=self.note)
        self.login.place(x=80, y=550)
        
        
        
      
        # DATA 
        
        self.lgn_button = Image.open('images\\viewc.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.frame1, image=photo,width=60,height=50,bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=10, y=640)
        
 
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
        labels = [ 'Student', 'Staff']
        sizes = [9,7]
        colors = [ '#ffcd5e', 'lightcoral']
        fig, ax = plt.subplots(figsize=(5,4))
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=150)
        ax.axis('equal')
        # plt.figure(figsize=(4, 4)) 
        canvas = FigureCanvasTkAgg(fig, master=self.frame3)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=10,y=42)
  
    
    def create_bar_chart(self):
        # Data for the bar chart
        categories = ['Staff', 'Students', 'Course', 'Notice']
        values = [3,1,4,1]
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
            
            
    def tech(self):
        teacher.Addteacher(self.frame2)
        
    def hom(self):
       
        self.frame2 = Frame(self.root, bg='white', width=1600, height=1000)
        self.frame2.place(x=300, y=0)
        
        self.lbl=Label(self.frame2,text='Welcome Admin!',bg='white',fg='#035995',font=('times new roman',24,'bold'),width=85,padx=50,anchor='w')
        self.lbl.place(x=1.5,y=15)
        
        
        self.lgn_button = Image.open('images\\dashbut2.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label1 = Label(self.frame2, image=photo,width=350,height=280,bg='#ffffff')
        self.lgn_button_label1.image = photo
        self.lgn_button_label1.place(x=100, y=80)
        
        count=0
        for data in database.Tstaff():
            count+=1
            
        self.countTeacher=Label(self.lgn_button_label1,text=count,bg='#FF91A5',fg='black',font=('',15,'bold'))
        print(count)
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
        print(count)
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
        print(count)
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
        print(count)
        self.countTeacher.place(x=200,y=110)
        
        
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
      

        dashboard.main(self)
        
    
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
            
    def holiday(self):
        # print('j')
        addholiday.holidayadd(self.frame2)
                
    # def event(self):
    #     addevent.eventadd(self.frame2)
        
if __name__=='__main__':
    obj=main()
    
    
    
      # def show_pie_chart(self):
    # # Replace this example data and labels with your own data
    #     data = [3,1,3,1]
    #     labels = ['staff', 'student', 'course', 'note']

    #     plt.figure(figsize=(5, 4))
    #     plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    #     plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    
    
     # self.pie_chart_button = Button(self.frame2, text='Show Pie Chart', font=("times new roman", 18, "bold"), width=13, bd=0,
        #                        bg='white',cursor='hand2', activebackground='#ffffff', fg='#035995',
        #                        anchor='w', command=self.show_pie_chart)
        
        # self.pie_chart_button.place(x=220, y=520)
        
        
        # button = Button(self.frame2, text="Show Pie Chart", command=self.create_pie_chart)
        # button.place(x=200,y=500)
        
        
        
                
    #     self.pie_chart_button = Button(self.frame2, text='Show Pie Chart', font=('monoco', 13, 'bold'), width=25, bd=0,
    #                                    bg='white', cursor='hand2', activebackground='#035995', pady=-1, fg='white',
    #                                    command=self.show_pie_chart)
    #     self.pie_chart_button.place(x=100, y=650)

    # # def Addnote(self):
    #     # ... (your existing code)

    # def show_pie_chart(self):
    #     # Assuming you have some data for the pie chart
    #     data = [20, 30, 40, 10]  # Example data, you should replace this with your actual data
    #     labels = ['Category A', 'Category B', 'Category C', 'Category D']

    #     plt.figure(figsize=(6, 6))
    #     plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    #     plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

    #     # Display the pie chart
    #     plt.show()
    
    
    
    
    
    
    
    
  # cal=Calendar(self.frame2)
        # cal = Calendar(self.frame2, font="Arial 13", selectmode='day', locale='en_US',
        #        cursor="hand2")
        # cal.place(x=1150,y=490)