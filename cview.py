from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Treeview
# from tkinter import messagebox
import database

class cw():
    # constructor
    # def __init__(self):
     def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='90') 
  

        self.tr = Treeview(self.frame2, columns=('name', 'duration', 'edit', 'delete'), show='headings')
        self.tr.column('# 1',anchor='w',stretch=NO,width=390)
        self.tr.column('# 2',anchor='c',stretch=NO,width=390)
        self.tr.column('# 3',anchor='c',stretch=NO,width=390)
        self.tr.column('# 4',anchor='c',stretch=NO,width=390)
        # self.tr.heading('id', text="ID")
        
        self.tr.heading('name', text="Name")
        
        
        self.tr.heading('duration', text="Duration")
        
        
        self.tr.heading('edit', text="Edit")

        self.tr.heading('delete', text="Delete")
        self.tr.place(x=1.5,y=0,width=1600,height=1050)
        
        
        
        data = database.courseview()

        
        for i in data:
            self.tr.insert('', 'end', text = i[0], values = (i[1], i[2],'Edit', 'Delete'))
        self.tr.place(x=1.5,y=1,width=1600,height=1050)

   
   
if __name__ == '__main__':
    obj = cw()