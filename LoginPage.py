from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import database
import dashboard

class loginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1910x1050')
        self.window.resizable(False, False)
        # self.window.state('zoomed')
        self.window.title('Login Page')
#040405
     
        #Login Frame
        self.lgn_frame = Frame(self.window, bg='#040405', width=1910, height=1050)
        self.lgn_frame.place(x=0, y=5)

        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('times new roman', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=450, y=130, width=300, height=30)
        #left side image
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=355, y=250)

        
        #  Sign In Image 
        
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=1120, y=280)

        
        #  Sign In label 
    
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=1150, y=390)

        
        # username
         
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#7f7f7f",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=1050, y=450)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=1080, y=485, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=1050, y=509)
        #  Username icon 
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=1050, y=482)

        
        # login button
        
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=1050, y=620)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.login)
        self.login.place(x=20, y=10)
        # 
        # =Forgot password==
        # 
        # self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
        #                             font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
        #                             activebackground="#040405"
        #                             , borderwidth=0, background="#040405", cursor="hand2")
        # self.forgot_button.place(x=630, y=510)
        # # = Sign Up 
        # self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
        #                         relief=FLAT, borderwidth=0, background="#040405", fg='white')
        # self.sign_label.place(x=550, y=560)

        # self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        # self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
        #                                   borderwidth=0, background="#040405", activebackground="#040405")
        # self.signup_button_label.place(x=670, y=555, width=111, height=35)

        
        #password
        
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#7f7f7f",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=1050, y=530)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=1080, y=566, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=1050, y=590)
        
        #Password icon 
        
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=1050, y=564)
        
        #  show/hide password 
        
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=1360, y=570)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=1360, y=570)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=1360, y=570)
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