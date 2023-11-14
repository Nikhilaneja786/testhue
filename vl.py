from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import database

class LV():
    # constructor
    # def _init_(self):
    def __init__(self,frame2) -> None:
        self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='0') 

        self.tr = Treeview(self.frame2, columns=('name','reason','startdate', 'enddate','delete'), show='headings')
        self.tr.column('# 1',anchor='w',stretch=NO,width=320)
        self.tr.column('# 2',anchor='w',stretch=NO,width=320)
        self.tr.column('# 3',anchor='c',stretch=NO,width=320)
        self.tr.column('# 4',anchor='c',stretch=NO,width=320)
        self.tr.column('# 5',anchor='c',stretch=NO,width=320)

        
        self.tr.heading(column='name',text='Name')
        self.tr.heading(column='reason',text='Reason')
        self.tr.heading(column='startdate',text='Start Date')
        self.tr.heading(column='enddate',text='End Date')
        self.tr.heading(column='delete',text='Delete')
        
        data = database.lw()

        
        for i in data:
            self.tr.insert('', 'end', text = i[0], values = (i[1], i[2],i[3],i[4],'delete'))
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
                if col == '#5':
                        res = messagebox.askyesno("ALERT", "Do You Realy Want to delete this item")
                        if res:
                                rs = database.deleteholiday(gup)
                                if rs:
                                        messagebox.showinfo("Success", "Suuccessfully Deleted")
                                        # self.frame2.destroy()
                                        obj = LV(self.frame2)
                                        # obj.firstFrame()
                                else:
                                        messagebox.showerror('Alert', 'Something went wrong.')
        


if __name__ == '__main__':
    obj =LV()