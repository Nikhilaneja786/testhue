from tkinter import  *
# from tkinter import messagebox
from PIL import Image, ImageTk
import LoginPage
import loginpaget
class main():
    def __init__(self):
    
        self.root=Tk()
        self.root.title("main")
        # self.root.geometry('700x500')
        self.root.geometry('1900x1000')
        self.root.config(bg='black')
        self.root.resizable(False,False)
        
        
        self.home_frame = Frame(self.root, bg='#035995', width=1900, height=1000)
        self.home_frame.place(x=0, y=0)
        
        #recodir image
        self.img = Image.open('images/recodir.png').resize((520, 125))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.home_frame, image = self.imgTk,bg='#035995')
        self.imgLbl.place(x = 720, y = 350)
        
        #continuebutton
        self.lgn_button = Image.open('images\\butt2.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.home_frame, image=photo, bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=820, y=500)
        self.login = Button(self.lgn_button_label, text='Continue As Admin', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='white', cursor='hand2', activebackground='white', fg='#035995',command=self.sun)
        self.login.place(x=10, y=8)
        
        self.lgn_button = Image.open('images\\butt2.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.home_frame, image=photo, bg='#035995')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=820, y=580)
        self.login = Button(self.lgn_button_label, text='Continue As Teacher', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='white', cursor='hand2', activebackground='white', fg='#035995',command=self.mun)
        self.login.place(x=10, y=8)
        #main loop#3047ff
        self.root.mainloop()
        
    def sun (self):
        # print('button is clicked')sa
        rs=1 
        if rs==1:
                
            self.root.destroy()
            LoginPage.page()
            
    def mun (self):
        # print('button is clicked')
        rs=1 
        if rs==1:
                
            self.root.destroy()
            loginpaget.paget()
            
            
if __name__=='__main__':
    main()
    
    