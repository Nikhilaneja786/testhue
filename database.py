import mysql.connector
Info=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="recodir"
)
#login
cursor=Info.cursor()
def loginAdmin(data):
    try:
        cursor.execute('select * from `login_page` where `username` =%s and `password`=%s ',data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False
        
def loginteacher(data):
    try:
        cursor.execute('select * from `addstaff` where `username` =%s and `password`=%s ',data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False     
    
    
def loginstudent(data):
    try:
        cursor.execute('select * from `addstudent` where `username` =%s and `password`=%s ',data)
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False   
#staff
def addstaff(data):
    try:
        cursor.execute('INSERT INTO `addstaff`(`name`,`dob`,`contact`,`qualification`,`gender`,`username`,`password`) VALUES(%s,%s,%s,%s,%s,%s,%s)',data)
        # return cursor.fetchone()
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

def Tstaff():
    try:
        cursor.execute('select * from `addstaff`')
        return cursor.fetchall()
        # Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
    

#note
def Addnote(data):
    try:
        cursor.execute('INSERT INTO `addnote`(`title`,`description`) VALUES(%s,%s)',data)
        # return cursor.fetchone()
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
    
def vnote():
    try:
        cursor.execute('select * from `addnote`')
        return cursor.fetchall()
        # Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
    
#course
def Addcourse(data):
    try:
        cursor.execute('INSERT INTO `addcourse`(`name`,`duration`) VALUES(%s,%s)',data)
        # return cursor.fetchone()
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
    
def courseview():
    try:
        cursor.execute('select * from `addcourse`')
        return cursor.fetchall()
        # Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

def COMBOCOURSE():
    try:
        cursor.execute('select name from `addcourse`')
        return cursor.fetchall()
        # Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    

#addstudent
def Addstudent(data):
    try:
        cursor.execute('INSERT INTO `addstudent`(`name`,`dob`,`contact`,`gender`,`course`,`address`,`username`,`password`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',data)
        # return cursor.fetchone()
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def Studenteview():
    try:
        cursor.execute('select * from `addstudent`')
        return cursor.fetchall()
        # Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
#holiday
def Addholiday(data):
    try:
        cursor.execute('INSERT INTO `addholiday`(`holidayname`,`type`,`startdate`,`enddate`) VALUES(%s,%s,%s,%s)',data)
        # return cursor.fetchone()
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def Hview():
    try:
        cursor.execute('select * from `addholiday`')
        return cursor.fetchall()
        # Info.commit()
        return True
    except Exception as e:
        print(e)
        return False 

def pieview():
    try:
        cursor.execute('SELECT COUNT(*) FROM `addstaff`')
        staff_count = cursor.fetchone()[0]  # Get the count for "addstaff" table
        cursor.execute('SELECT COUNT(*) FROM `addstudent`')
        student_count = cursor.fetchone()[0]  # Get the count for "addstudent" table
        
        return staff_count, student_count  # Return the counts for both tables
    except Exception as e:
        print(e)
        return None  # Handle the error condition appropriately

def barview():
    try:
        cursor.execute('SELECT COUNT(*) FROM `addstaff`')
        staff_count = cursor.fetchone()[0]  # Get the count for "addstaff" table
        cursor.execute('SELECT COUNT(*) FROM `addstudent`')
        student_count = cursor.fetchone()[0]  # Get the count for "addstudent" table
        cursor.execute('SELECT COUNT(*) FROM `addcourse`')
        course_count = cursor.fetchone()[0]
        cursor.execute('SELECT COUNT(*) FROM `addnote`')
        addnote = cursor.fetchone()[0]
        return staff_count, student_count ,course_count,addnote # Return the counts for both tables
    except Exception as e:
        print(e)
        return None  # Handle the error condition appropriately

#staff edit delete    
def selectstaff(arg):
    print("arsg = ",arg)
    try:
        cursor.execute('select * from addstaff where id = %s',arg)
        return cursor.fetchall()
    except:
        return False

def updatestaff(arg):

    try:
        cursor.execute('update addstaff SET name=%s,dob=%s,contact=%s,qualification=%s,gender=%s,username=%s,password=%s where id=%s', arg)
        Info.commit()
        
        return True
    except:
        return False
    
def deletestaff(gup):
    print("arsg = ",gup)
    try:
        cursor.execute('Delete from addstaff where id = %s',gup)
        Info.commit()
        return True
    except:
        return False


#student edit delete 

def selectstudent(arg):
    print("arsg = ",arg)
    try:
        cursor.execute('select * from addstudent where id = %s',arg)
        return cursor.fetchall()
    except:
        return False

def updatestudent(arg):

    try:
        cursor.execute('update addstudent SET name=%s,dob=%s,contact=%s,gender=%s,course=%s where id=%s', arg)
        Info.commit()
        return True
    except:
        return False
    
def deletestudent(gup):
    print("arsg = ",gup)
    try:
        cursor.execute('Delete from addstudent where id = %s',gup)
        Info.commit()
        return True
    except:
        return False
    
    
#holiday edit delete 
def deleteholiday(gup):
    print("arsg = ",gup)
    try:
        cursor.execute('Delete from addholiday where id = %s',gup)
        Info.commit()
        return True
    except:
        return False
    
    
#notice edit delete 
def deletenotice(gup):
    print("arsg = ",gup)
    try:
        cursor.execute('Delete from addnote where id = %s',gup)
        Info.commit()
        return True
    except:
        return False


#coursedelete


def selectcourse(arg):
    print("arsg = ",arg)
    try:
        cursor.execute('select * from addcourse where id = %s',arg)
        return cursor.fetchall()
    except:
        return False

def updatecourse(arg):

    try:
        cursor.execute('update addcourse SET name=%s,duration =%s where id=%s', arg)
        Info.commit()
        
        return True
    except:
        return False
    
def deletecourse(gup):
    print("arsg = ",gup)
    try:
        cursor.execute('Delete from addcourse where id = %s',gup)
        Info.commit()
        return True
    except:
        return False
    



def deleteleave(gup):
    print("arsg = ",gup)
    try:
        cursor.execute('Delete from addleave where id = %s',gup)
        Info.commit()
        return True
    except:
        return False





# def piechart(year):
#     db = "recodir"
#     cursor = Info.cursor()
#     try:
#         cursor.execute("SELECT COUNTFROM expenditure WHERE YEAR = %s", (year,))
#         total_expense = cursor.fetchone()
#         return float(total_expense[0]) if total_expense else 0
#     except Exception as e:
#         print("Error retrieving total expenditure by year:", e)
#         return 0
#     finally:
#         Info.cursor()
#         db.close()
def Addl(data):
    try:
        cursor.execute('INSERT INTO `addleave`(`name`,`reason`,`startdate`,`enddate`) VALUES(%s,%s,%s,%s)',data)
        # return cursor.fetchone()
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def lw():
    try:
        cursor.execute('select * from `addleave`')
        return cursor.fetchall()
        return True
    except Exception as e:
        print(e)
        return False 
    
def als(data):
    try:
        cursor.execute('INSERT INTO `addleaves`(`name`,`reason`,`startdate`,`enddate`,`department`) VALUES(%s,%s,%s,%s,%s)',data)
        # return cursor.fetchone()
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def lvs():
    try:
        cursor.execute('select * from `addleaves`')
        return cursor.fetchall()
        return True
    except Exception as e:
        print(e)
        return False 