import sqlite3 

def insert_toDB () :	
    connect =sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
    m = [' มกราคม',' กุมภาพันธ์',' มีนาคม',' เมษายน',' พฤษภาคม',' มิถุนายน',' กรกฎาคม',' สิงหาคม',' กันยายน',' ตุลาคม',' พฤศจิกายน',' ธันวาคม']
    for k in m :
        for i in range (1,32) :
                #i = day  // k=month 
            data3 = (i,k," 2549")
            data4 = (i,k," 2550")        #table      #column

            DB_sqlite3 =""" INSERT INTO birthdayHS (ddd,mmm,yyy) VALUES (?,?,?)"""
            connect.execute(DB_sqlite3,data3) #data3
            connect.commit()

            DB_sqlite3 =""" INSERT INTO birthdayHS (ddd,mmm,yyy) VALUES (?,?,?)"""
            connect.execute(DB_sqlite3,data4) #data4
            connect.commit()


insert_toDB()