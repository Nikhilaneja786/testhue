from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from datetime import *
import time
import database
import matplotlib.pyplot as plt

class main():
    def __init__(self):
    
        self.root=Tk()
        self.root.title("main")
        # self.root.geometry('700x500')
        self.root.geometry('1900x1000')
        self.root.config(bg='black')
        self.root.resizable(False,False)
        # ... (your existing code)

        # Add a button to trigger the pie chart creation
        self.pie_chart_button = Button(self.root, text='Show Pie Chart', font=('monoco', 13, 'bold'), width=25, bd=0,
                                       bg='black', cursor='hand2', activebackground='#035995', pady=-1, fg='white',
                                       command=self.show_pie_chart)
        self.pie_chart_button.place(x=200, y=650)

    # def Addnote(self):
        # ... (your existing code)

    def show_pie_chart(self):
        # Assuming you have some data for the pie chart
        data = [20, 30, 40, 10]  # Example data, you should replace this with your actual data
        labels = ['Category A', 'Category B', 'Category C', 'Category D']

        plt.figure(figsize=(6, 6))
        plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

        # Display the pie chart
        plt.show()

if __name__ == '__main__':
    root = Tk()
    app = main()
    root.mainloop()
