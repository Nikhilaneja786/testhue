from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import database

class sw():
    # constructor
    # def __init__(self):
    def __init__(self,frame2) -> None:
        # self.frame2 = frame2

        self.frame2=Frame(width='1610',height='1050',bg='white')
        self.frame2.place(x='300',y='90') 
        # # self.root = Tk()
        # self.root.title('Today tasks')

        # self.root.resizable(height=False,width=False)
        
        # self.root.geometry('1200x400')
        
        # self.fr = Frame(self.root, bg="white")
        # self.fr.place(x=0, y=25, width="804", height="720")

        self.tr = Treeview(self.frame2, columns=('name','d.o.b','contact','gender','course','address','edit','delete'),show='headings')
        self.tr.column('# 1',anchor='w',stretch=NO,width=200)
        self.tr.column('# 2',anchor='c',stretch=NO,width=200)
        self.tr.column('# 3',anchor='c',stretch=NO,width=200)
        self.tr.column('# 4',anchor='w',stretch=NO,width=180)
        self.tr.column('# 5',anchor='w',stretch=NO,width=200)
        self.tr.column('# 6',anchor='w',stretch=NO,width=300)
        self.tr.column('# 7',anchor='c',stretch=NO,width=150)
        self.tr.column('# 8',anchor='c',stretch=NO,width=150)
        # self.tr.column('# 6',anchor='w',stretch=NO,width=260)
        
        # self.tr.heading(column='id',text='Id')
        self.tr.heading(column='name',text='Name')
        self.tr.heading(column='d.o.b',text='D.O.B')
        self.tr.heading(column='contact',text='Contact')
        self.tr.heading(column='gender',text='Gender')
        self.tr.heading(column='course',text='Course')
        self.tr.heading(column='address',text='Address')
        self.tr.heading(column='edit',text='Edit')
        self.tr.heading(column='delete',text='Delete')
       
        self.tr.place(x=1.5,y=1,width=1600,height=1050)
        
        
        data = database.Studenteview()

        
        for i in data:
            self.tr.insert('', 'end', text = i[0], values = (i[1], i[2],i[3],i[4],i[5],i[6] ,'Edit', 'Delete'))
        self.tr.place(x=1.5,y=1,width=1600,height=1050)
        
        # self.tr.bind('<Double-Button-1>',self.actions)
        
    # def actions(self, e):
    #             print('fgghhgf')
    #             # get the values of the selected rows\\
    #             tt = self.tr.focus()

    #             # get the column id
    #             col = self.tr.identify_column(e.x)
    #             # print(col)
    #             # print(self.tr.item(tt))

    #             gup = (
    #                 self.tr.item(tt).get('text'),
    #             )
    #             print("gu = ",gup)
    #             if col == '#8':
    #                     res = messagebox.askyesno("ALERT", "Do You Realy Want to delete this item")
    #                     if res:
    #                             rs = database.deletestaff(gup)
    #                             if rs:
    #                                     messagebox.showinfo("Success", "Suuccessfully Deleted")
    #                                     # self.frame6.destroy()
    #                                     # obj = viewCategory(self.frame6)
    #                                     # obj.firstFrame()
    #                             else:
    #                                     messagebox.showerror('Alert', 'Something went wrong.')
    #             if col == '#7':
    #                     self.frame6.destroy()
    #                     # self.obj = editstaff.Editstaff(gup)
    #                     # obj.frame2(gup)

   
if __name__ == '__main__':
    obj =sw()