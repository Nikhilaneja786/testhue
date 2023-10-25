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
    


def Addstudent(data):
    try:
        cursor.execute('INSERT INTO `addstudent`(`name`,`dob`,`contact`,`gender`,`course`,`address`) VALUES(%s,%s,%s,%s,%s,%s)',data)
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
    
    
    
def selectstaff(arg):
    print("arsg = ",arg)
    try:
        cursor.execute('select * from addstaff where id = %s',arg)
        return cursor.fetchall()
    except:
        return False

def updatestaff(arg):

    try:
        cursor.execute('update addstaff SET name=%s,dob=%s,contact=%s,qualification=%s,gender=%s where id=%s', arg)
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