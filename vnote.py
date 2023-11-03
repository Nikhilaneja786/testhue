from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import database
from tkinter import ttk

class nw():
    # constructor
    # def __init__(self):
    def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='90') 

        self.tr = Treeview(self.frame2, columns=('title','description','date','delete'), show='headings')
        self.tr.column('# 1',anchor='w',stretch=NO,width=350)
        self.tr.column('# 2',anchor='w',stretch=NO,width=700)
        self.tr.column('# 3',anchor='c',stretch=NO,width=300)
        # self.tr.column('# 4',anchor='w',stretch=NO,width=200)
        self.tr.column('# 4',anchor='c',stretch=NO,width=300)

        
        self.tr.heading(column='title',text='Title')
        self.tr.heading(column='description',text='Description')
        self.tr.heading(column='date',text='Date')
        # self.tr.heading(column='edit',text='Edit')
        self.tr.heading(column='delete',text='Delete')
        
        data = database.vnote()

        
        for i in data:
            self.tr.insert('', 'end', text = i[0], values = (i[1], i[2],i[3], 'Delete'))
        self.tr.place(x=1.5,y=1,width=1600,height=1050)
        
        self.tr.bind('<Double-Button-1>',self.actions)
        
    
    def actions(self, e):
                # get the values of the selected rows\\
                tt = self.tr.focus()

                # get the column id
                col = self.tr.identify_column(e.x)
                # print(col)
                # print(self.tr.item(tt))

                gup = (
                    self.tr.item(tt).get('text'),
                )
                print("gu = ",gup)
                if col == '#4':
                        res = messagebox.askyesno("ALERT", "Do You Realy Want to delete this item")
                        if res:
                                rs = database.deletenotice(gup)
                                if rs:
                                        messagebox.showinfo("Success", "Suuccessfully Deleted")
                                        # self.frame2.destroy()
                                        # obj = tview(self.frame2)
                                        # obj.firstFrame()
                                else:
                                        messagebox.showerror('Alert', 'Something went wrong.')

            


if __name__ == '__main__':
    obj =nw()