from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import database

class vwt():
    # constructor
    # def __init__(self):
     def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='90') 
        

        self.tr = Treeview(self.frame2, columns=('name', 'd.o.b','contact','qualification','gender','edit', 'delete'), show='headings')
        self.tr.column('# 1',anchor='w',stretch=NO,width=220)
        self.tr.column('# 2',anchor='c',stretch=NO,width=220)
        self.tr.column('# 3',anchor='c',stretch=NO,width=220)
        self.tr.column('# 4',anchor='w',stretch=NO,width=220)
        self.tr.column('# 5',anchor='w',stretch=NO,width=220)
        self.tr.column('# 6',anchor='c',stretch=NO,width=220)
        self.tr.column('# 7',anchor='c',stretch=NO,width=220)
        
        
        # self.tr.heading(column='id',text='Id')
        self.tr.heading(column='name',text='Name')
        self.tr.heading(column='d.o.b',text='D.O.B')
        self.tr.heading(column='contact',text='Contact')
        self.tr.heading(column='qualification',text='Qualification')
        self.tr.heading(column='gender',text='Gender')
        self.tr.heading(column='edit',text='Edit')
        self.tr.heading(column='delete',text='Delete')
        
        self.tr.place(x=1.5,y=1,width=1600,height=1050)
        

        data = database.Tstaff()

        
        for i in data:
            self.tr.insert('', 0, text = i[0], values = (i[1],i[2],i[3],i[4],i[5], 'Edit', 'Delete'))
        self.tr.place(x=1.5,y=1,width=1600,height=1050)
            
    
   
if __name__ == '__main__':
    obj = vwt()