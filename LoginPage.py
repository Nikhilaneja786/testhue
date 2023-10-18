from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import database
import dashboard

class loginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1910x1050')
        self.window.config(bg='white')
        self.window.resizable(False, False)
        # self.window.state('zoomed')
        self.window.title('Login Page')
# white
     
        #Login Frame
        self.lgn_frame = Frame(self.window, bg='#035995', width=800, height=1050)
        self.lgn_frame.place(x=0, y=5)

        self.txt = "WELCOME TO RECODIR"
        self.heading = Label(self.window, text=self.txt, font=('times new roman', 25, "bold"), bg="white",
                             fg='#035995',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=1150, y=60, width=430, height=30)
        
        
        #left side image
        # self.side_image = Image.open('images\\vector.png')
        # photo = ImageTk.PhotoImage(self.side_image)
        # self.side_image_label = Label(self.lgn_frame, image=photo, bg='#035995')
        # self.side_image_label.image = photo
        # self.side_image_label.place(x=255, y=250)
  
 
        
        #  Sign In Image 
        
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.window, image=photo, bg='white')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=1270, y=280)

        
        #  Sign In label 
    
        self.sign_in_label = Label(self.window, text="Sign In", bg="white", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=1300, y=390)

        
        # username
         
        self.username_label = Label(self.window, text="Username", bg="white", fg="black",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=1200, y=450)

        # self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="black",
        #                             font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        # self.username_entry.place(x=1230, y=485, width=270)

        # self.username_line = Canvas(self.window, width=300, height=2.0, bg="black", highlightthickness=0)
        # self.username_line.place(x=1200, y=509)
        
        
        
        
        
        
        
        
        
        
        self.username_icon = Image.open('images\\outline.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.window, image=photo, bg='white')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=1200, y=480) 
        self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="black",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=1240, y=492, width=260)
        
        
        #  Username icon 
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.window, image=photo, bg='white')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=1210, y=490)

        
        
        
        #password
        self.password_label = Label(self.window, text="Password", bg="white", fg="black",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=1200, y=550)

        # self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="black",
        #                             font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        # self.password_entry.place(x=1230, y=566, width=244)
        # self.password_line = Canvas(self.window, width=300, height=2.0, bg="black", highlightthickness=0)
        # self.password_line.place(x=1200, y=590)
        
        self.password_entry = Image.open('images\\outline.png')
        photo = ImageTk.PhotoImage(self.password_entry)
        self.password_entry = Label(self.window, image=photo, bg='white')
        self.password_entry.image = photo
        self.password_entry.place(x=1200, y=580) 
        self.password_entry= Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="black",
                                    font=("yu gothic ui ", 12, "bold"), show='*',insertbackground = '#6b6a69')
        self.password_entry.place(x=1240, y=592, width=260)
        
        
        
        #Password icon 
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.window, image=photo, bg='white')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=1210, y=590)
        
        
        # login button
        self.lgn_button = Image.open('images\\but.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.window, image=photo, bg='white')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=1210, y=665)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#035995', cursor='hand2', activebackground='#035995', fg='white',command=self.login)
        self.login.place(x=18, y=8)
        
        
        #  show/hide password 
         
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=1510, y=590)

    def show(self):
        self.hide_button = Button(self.window, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=1510, y=590)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=1510, y=590)
        self.password_entry.config(show='*')
        
        
    def login(self):
        if self.username_entry.get() and self.password_entry.get():
            res=database.loginAdmin((self.username_entry.get(),self.password_entry.get()))
            if res:
                self.window.destroy()
                dashboard.main()
            else:
                messagebox.showerror('Alert','Invalid username/password')
        else:
            messagebox.showwarning('Alert','Please enter your details')
            

def page():
    window = Tk()
    loginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()