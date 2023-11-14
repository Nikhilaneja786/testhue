from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import database

class hvt():
    # constructor
    # def _init_(self):
    def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 

        self.tr = Treeview(self.frame2, columns=('holiday name','type','start date', 'end date'), show='headings')
        self.tr.column('# 1',anchor='w',stretch=NO,width=320)
        self.tr.column('# 2',anchor='w',stretch=NO,width=320)
        self.tr.column('# 3',anchor='c',stretch=NO,width=320)
        self.tr.column('# 4',anchor='c',stretch=NO,width=320)
        

        
        self.tr.heading(column='holiday name',text='Holiday Name')
        self.tr.heading(column='type',text='type')
        self.tr.heading(column='start date',text='Start Date')
        self.tr.heading(column='end date',text='End Date')
        
        
        data = database.Hview()

        
        for i in data:
            self.tr.insert('', 'end', text = i[0], values = (i[1], i[2],i[3],i[4]))
        self.tr.place(x=1.5,y=1,width=1600,height=1050)
       
        
    


if __name__ == '__main__':
    obj =hvt()