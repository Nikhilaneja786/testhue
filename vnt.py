from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Treeview
# from tkinter import messagebox
import database
# from tkinter import ttk

class nwt():
    # constructor
    # def _init_(self):
    def __init__(self,frame2) -> None:
        self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 

        self.tr = Treeview(self.frame2, columns=('title','description','date'), show='headings')
        self.tr.column('# 1',anchor='w',stretch=NO,width=350)
        self.tr.column('# 2',anchor='w',stretch=NO,width=700)
        self.tr.column('# 3',anchor='c',stretch=NO,width=300) 
        

        
        self.tr.heading(column='title',text='Title')
        self.tr.heading(column='description',text='Description')
        self.tr.heading(column='date',text='Date')
       
        
        data = database.vnote()

        
        for i in data:
            self.tr.insert('', 'end', text = i[0], values = (i[1], i[2],i[3]))
            
        self.tr.place(x=1.5,y=1,width=1600,height=1050)
        
        
                             
                         
       

                         
                       

            


if __name__ == '__main__':
    obj =nwt()