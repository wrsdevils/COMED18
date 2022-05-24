#==================imports===================
import os
import sqlite3
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
import random
import time
import datetime
#============================================



root = Tk()

root.geometry("1280x720")
root.title("STUDENT ENROLLMENT SYSTEM")
root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))

######----------------------- VARIABLE -----------------------------------######

user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
new_user = StringVar()
new_passwd = StringVar()

#------------------------------
nametitle = StringVar()
name = StringVar()
surname = StringVar()
blood = StringVar()
regional = StringVar()
nationality = StringVar()
religion = StringVar()
phonenum = StringVar()
mail = StringVar()
#--------------------
ddd = StringVar()
mmm = StringVar()
yyy = StringVar()

oldschool = StringVar()
oldsubdis = StringVar()
oldprovince = StringVar()
edyear = StringVar()
gpa = StringVar()
#------------------------------
program = StringVar()
nttlist = StringVar()

ntt = StringVar()
#------------------------------
address = StringVar()
villnum = StringVar()
alley = StringVar()
street = StringVar()
subdistrict = StringVar()
district = StringVar()
province = StringVar()
postnum = StringVar()

dadname = StringVar()
dadoc = StringVar()
dadoffice = StringVar()
dadphone = StringVar()

momname = StringVar()
momoc = StringVar()
momoffice = StringVar()
momphone = StringVar()

parentrelate = StringVar()
parentname = StringVar()
parentoc = StringVar()
parentoffice = StringVar()
parentphone = StringVar()

#----------------------------


with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
    cur = db.cursor()


def login(Event=None):
    global username,password, IDnum_list ,IDnum_sum, digit13,num
    global enroll
    global page2
    username = user.get()
    password = passwd.get()
    
    if username == "f" or username == "admin" or username == "1478523698745" or username == "warisa" or username == "admint" :
        messagebox.showinfo("Login Page", "The login is successful")
        root.withdraw()
        enroll = Toplevel()
        page2 = HS_window(enroll)
        enroll.protocol("WM_DELETE_WINDOW", exitt)
        enroll.mainloop()
    else :
        if len(username) != 13 :
            messagebox.showerror("Error", "กรุณากรอกข้อมูลที่ถูกต้อง")
            page1.entry2.delete(0, END)
        else :
            num = 0
            IDnum_count = 13
            IDnum_list = list(username)
            IDnum_sum =0
            while (num <12) :
                IDnum_sum +=int(IDnum_list[num])*(IDnum_count-num)
                num+=1
                digit13 = IDnum_sum % 11 
            if digit13==0: 
                digit13=1
            elif digit13==1:
                digit13=0
            else :
                digit13=11-digit13
            if digit13==int(IDnum_list[12]):
                if len(password) >= 6 :
                    with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
                        cur = db.cursor()
                        find_user = "SELECT * FROM HSlogin WHERE ID_num = ?"
                        cur.execute(find_user, [username])
                        results = cur.fetchall()
                        if results:
                            root.option_add('*Dialog.msg.font', 'DB HelvethaicaMon X Blk 12')
                            messagebox.showinfo("!", "this account already exists")
                            page1.entry2.delete(0, END)
                        else :
                            connect =sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
                            data = (username,password)
                            DB_sqlite3 =""" INSERT INTO HSlogin (ID_num,Password) VALUES (?,?)"""
                            connect.execute(DB_sqlite3,data)
                            connect.commit()

                            messagebox.showinfo("Login Page", "The login is successful")
                            page1.entry1.delete(0, END)
                            page1.entry2.delete(0, END)
                            root.withdraw()
                            enroll = Toplevel()
                            page2 = HS_window(enroll)
                            enroll.protocol("WM_DELETE_WINDOW", exitt)
                            enroll.mainloop()

                else :
                    messagebox.showerror("PASSWORD ERROR", "Password should be at least 6 characters")
                    page1.entry2.delete(0, END)
            else :
                if len(password) >= 6 :
                    messagebox.showerror("Error", "Incorrect Identification Number")
                    page1.entry2.delete(0, END)
                else :
                    messagebox.showerror("Error", "Incorrect ID num and password")
                    page1.entry2.delete(0, END)
#--------------------------------------------------------------------------------------------------------------

def logout():
    sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=enroll)
    if sure == True:
        enroll.destroy()
        root.deiconify()
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)

#--------------------------------------------------------------------------------------------------------------

def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=enroll)
    if sure == True:
        enroll.destroy()
        root.destroy()
#--------------------------------------------------------------------------------------------------------------
def next():

    global enroll2
    global page3
    global var_nametitle, var_name,var_surname,var_program, var_blood, var_phonenum, var_mail, var_oldschool, var_oldsubdis,var_oldprovince, var_edyear, var_gpa
    global var_regional, var_nationality, var_religion , var_ntt , var_ddd , var_mmm , var_yyy
    var_nametitle = nametitle.get()
    var_name = name.get()
    var_surname = surname.get()
    var_program = program.get()
    var_regional =  regional.get()
    var_nationality = nationality.get()
    var_religion =  religion.get()
    var_blood =  blood.get()
    var_phonenum =  phonenum.get()
    var_mail =  mail.get()
    var_oldschool =  oldschool.get()
    var_oldsubdis =  oldsubdis.get()
    var_oldprovince =  oldprovince.get()
    var_edyear =  edyear.get()
    var_gpa =  gpa.get()
    var_ntt = ntt.get()
    var_ddd = ddd.get()
    var_mmm = mmm.get()
    var_yyy = yyy.get()


    if (var_name  == "" or  var_surname == "" or var_program == "" or  var_regional == "" or  var_nationality  == "" or  var_religion == "" or  var_blood  == "" or  var_phonenum == "" or  var_mail == "" or  var_oldschool == "" or  var_oldsubdis == "" or  var_oldprovince == "" or  var_edyear == "" or  var_gpa == "" or  var_ntt == "" or  var_ddd == "" or var_mmm == "" or  var_yyy == "" ) :
        messagebox.showerror("ERROR","All Field Are Required")
    else :
        root.withdraw()
        #enroll.withdraw()
        enroll.deiconify()
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)
        enroll2 = Toplevel()
        page3 = HS_window2(enroll2)
        enroll2.protocol("WM_DELETE_WINDOW", exitt)
        print(username,var_ntt, var_name,var_surname, var_program, var_ddd , var_mmm , var_yyy, var_regional ,var_nationality, var_religion, var_blood, var_phonenum, var_mail, var_oldschool, var_oldsubdis,var_oldprovince, var_edyear,var_gpa)
        enroll2.mainloop()
####---------------###########------------
###--------------##########-----------##########
def yes ():
    global enroll2
    global page3 
    global var_nametitle, var_name,var_surname, var_nationality, var_regional, var_religion, var_blood, var_phonenum, var_mail, var_oldschool, var_oldsubdis,var_oldprovince, var_edyear, var_gpa, var_address, var_villnum, var_alley, var_street, var_subdistrict, var_district,var_province, var_postnum, var_dadname, var_dadoc, var_dadoffice, var_dadphone, var_momname, var_momoc, var_momoffice, var_momphone, var_parentrelate, var_parentname, var_parentoc, var_parentoffice, var_parentphone

    var_nametitle = nametitle.get()
    var_name = name.get()
    var_surname = surname.get()
    var_program = program.get()
    var_regional =  regional.get()
    var_nationality = nationality.get()
    var_religion =  religion.get()
    var_blood =  blood.get()
    var_phonenum =  phonenum.get()
    var_mail =  mail.get()
    var_oldschool =  oldschool.get()
    var_oldsubdis =  oldsubdis.get()
    var_oldprovince =  oldprovince.get()
    var_edyear =  edyear.get()
    var_gpa =  gpa.get()
    var_ntt = ntt.get()
    var_ddd = ddd.get()
    var_mmm = mmm.get()
    var_yyy = yyy.get()

    #------------\\\\
    var_address =  address.get()
    var_villnum =  villnum.get()
    var_alley =  alley.get()
    var_street =  street.get()
    var_subdistrict =  subdistrict.get()
    var_district =  district.get()
    var_province = province.get()
    var_postnum = postnum.get()
    var_dadname = dadname.get()
    var_dadoc = dadoc.get()
    var_dadoffice = dadoffice.get()
    var_dadphone = dadphone.get()
    var_momname = momname.get()
    var_momoc = momoc.get()
    var_momoffice = momoffice.get()
    var_momphone = momphone.get()
    var_parentrelate = parentrelate.get()
    var_parentname = parentname.get()
    var_parentoc = parentoc.get()
    var_parentoffice = parentoffice.get()
    var_parentphone = parentphone.get()


    L_alpha = [var_ntt,var_name,var_surname,var_mmm,var_program,var_regional,var_nationality,var_religion,var_blood,var_oldsubdis,var_oldprovince,var_subdistrict, var_district,var_province,var_dadoc,var_momoc,var_parentrelate,var_parentoc ]
    L_number = [var_phonenum, var_dadphone, var_momphone, var_parentphone]
    L_int = [var_ddd,var_yyy,var_edyear, var_villnum, var_postnum]
    L_name = [var_dadname, var_momname, var_parentname]
    L_any = [var_oldschool,var_address,var_dadoffice, var_momoffice,var_parentoffice]

    print (L_alpha,"\n",L_number,"\n",L_int,"\n",L_name,L_any)

    L_False = []
    mess = " #-- return FALSE "
    number = [1,2,3,4,5,6,7,8,9,0]
    spc_sign =["!","@","#","$","%","^","&","*","(",")","_","+","|","~","-","=","\\","{","}","[","]",":\",\";\",\"'","<",">","?",",",".","/"]
    true = []

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


    if (var_name  == "" or  var_surname == "" or var_program == "" or  var_regional == "" or  var_nationality  == "" or  var_religion == "" or  var_blood  == "" or  var_phonenum == "" or  var_mail == "" or  var_oldschool == "" or  var_oldsubdis == "" or  var_oldprovince == "" or  var_edyear == "" or  var_gpa == "" or  var_ntt == "" or  var_ddd == "" or var_mmm == "" or  var_yyy == "" ) :
        messagebox.showerror("ERROR","All Field Are Required")
    else :
        var_gpa = float(var_gpa)
        if isinstance (var_gpa,float) :
            if var_gpa <= 4.00 :
                print (round(var_gpa,2),"\t return True")
            else :
                print (var_gpa,"\t FALSE")
        else :
            return False

        if var_ddd.isdigit() :
            if int(var_ddd) >= 32 :
                m = var_ddd +mess + "it's incorrect day"
                L_False.append(m)
        else :
            m = var_ddd +mess + "it's not Integer"
            L_False.append(m)

        if  len(var_postnum) == 5 :
            if var_postnum.isdigit():
                print (var_postnum,"\t return True")
            else :
                m = var_postnum +mess + "it's not Integer"
                L_False.append(m)
        else :
            m = var_postnum +mess + "postnum must have 5 digits"
            L_False.append(m)

        for k in L_alpha :
            if isinstance(k,str) == True :
                for a in number :
                    if str(a) in k :
                        #print ("") 
                        m = k+mess+"it's has integer " 
                        L_False.append(m)
                        true.append(k)
                        break
                for a in spc_sign :
                    if str(a) in k :
                        #print ("")
                        m = k+mess+"it's has specific character " 
                        L_False.append(m)
                        true.append(k)
                        break
        
        for i in L_number :
            if len(i) == 10 :
                for a,b in enumerate (i) :
                    if a in [0] :
                        if b != '0' :
                            m = i+mess+"it's not bigin with 0 " 
                            L_False.append(m)
                        else :
                            print (i,"\t YES")
            else :
                m = i+mess+"it's has "+ str(len(i)) + " digits"
                L_False.append(m)

        for k in L_name :
            if isinstance(k,str) == True :
                for a in number :
                    if str(a) in k :
                        #print ("") 
                        m = k+mess+"it's has integer " 
                        L_False.append(m)
                        true.append(k)
                        break
                for a in spc_sign :
                    if str(a) in k :
                        #print ("")
                        m = k+mess+"it's has specific character " 
                        L_False.append(m)
                        true.append(k)
                        break

        if(re.fullmatch(regex, var_mail)):
            print("Valid Email")
        
        for i in range (1,3) :
            print("\n")

        if len(L_False) > 0 :
            for k in L_False :
                print (k)

        else :
            
            connect =sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
            connect.execute("DELETE from JHSpage1 where id_num =?  ",(username,))
            connect.execute("DELETE from JHSlogin where ID_num =?  ",(username,))
            connect.execute("DELETE from JHSprint where ID_num =?  ",(username,))
            connect.commit()

            

            data = (username,password)
            DB_sqlite3 =""" INSERT INTO JHSlogin (ID_num,Password) VALUES (?,?)"""
            connect.execute(DB_sqlite3,data)
            connect.commit()


            connect =sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
            #innsert = "INSERT INTO JHSpage1 (id_num,nametitle,name,surname,ddd,mmm,yyy,program,regional,nationality,religion,blood,phonenum,mail,oldschool,oldsubdis,oldprovince,edyear,gpa) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}')".format(username,var_ntt, var_name, var_surname, var_ddd, var_mmm, var_yyy , var_program, var_regional, var_nationality, var_religion, var_blood, var_phonenum, var_mail, var_oldschool, var_oldsubdis, var_oldprovince, var_edyear, var_gpa)
            innsert = "INSERT INTO HSpage1 (id_num,nametitle,name,surname,ddd,mmm,yyy,program,nationality,regional,religion,blood,phonenum,mail,oldschool,oldsubdis,oldprovince,edyear,gpa,address,villnum,alley,street,subdistrict,district,province,postnum,dadname,dadoc,dadoffice,dadphone,momname,momoc,momoffice,momphone,parentrelate,parentname,parentoc,parentoffice,parentphone) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}','{30}','{31}','{32}','{33}','{34}', '{35}','{36}','{37}','{38}', '{39}')".format(username,var_ntt, var_name,var_surname, var_ddd,var_mmm,var_yyy,var_program, var_regional,var_nationality, var_religion, var_blood, var_phonenum, var_mail, var_oldschool, var_oldsubdis,var_oldprovince, var_edyear, var_gpa, var_address, var_villnum, var_alley, var_street, var_subdistrict, var_district,var_province, var_postnum, var_dadname, var_dadoc, var_dadoffice, var_dadphone, var_momname, var_momoc, var_momoffice, var_momphone, var_parentrelate, var_parentname, var_parentoc, var_parentoffice, var_parentphone)
            connect.execute(innsert)
            connect.commit()
            print(username,var_ntt, var_name,var_surname, var_program, var_ddd , var_mmm , var_yyy, var_regional ,var_nationality, var_religion, var_blood, var_phonenum, var_mail, var_oldschool, var_oldsubdis,var_oldprovince, var_edyear,var_gpa)
            print ("ok insert yet")
            print(var_address, var_villnum, var_alley, var_street, var_subdistrict, var_district,var_province, var_postnum, var_dadname, var_dadoc, var_dadoffice, var_dadphone, var_momname, var_momoc, var_momoffice, var_momphone, var_parentrelate, var_parentname, var_parentoc, var_parentoffice, var_parentphone)
            
            
            ######################################
            

            ran = []
            room = []
            z = "0"
            for k in range (100,1000) :
                a = z+str(k)
                ran.append(a)

            print(random.choice(ran))

            w = random.randint(1,2) #อาคาร
            room.append(w)
            x = random.randint(1,4) #ชั้น
            room.append(x)
            room.append(0)
            y = random.randint(1,8) #ห้อง
            room.append(y)
            print (y)
            z = random.randint(1,20) #เลขที่นั่งสอบ

            if w == 1 :
                if x ==2 :
                    y += 8
                elif x == 3 :
                    y+= 16
                elif x == 4 :
                    y+= 24

            elif w == 2 :
                if x == 1 :
                    y += 32
                elif x ==2 :
                    y += 8+32
                elif x == 3 :
                    y+= 16+32
                elif x == 4 :
                    y+= 24+32

            print ("ROOM  NO. :",y)
            print ("BUILDING ",room[0])
            print ("ROOM ",''.join(str(i) for i in room))
            print ("SIT NO.",z)
            month = ["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤษภาคม","มิถุนายน","กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤศจิกายน","ธันวาคม"]
            date =[]


            date.append(datetime.datetime.now().strftime("%d"))
            date.append((month[(int(datetime.datetime.now().strftime("%m")))-1]))
            date.append("2565")

            insert_date = ' '.join(str(i) for i in date)


            a = [1,2,3,4,5,6]
            b=[]
            for i in range (1,3) :
                for j in range (1,5) :
                    for k in range (1,9) :
                        m = str(i)+str(j)+"0"+str(k)
                        b.append(m)

            print ("\n\n\n",b)


            with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
                    cur = db.cursor()

            conn = sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
            print('Connected to database successfully.')

            cur = conn.cursor()
            cur.execute("select * from HSpage1  ")
            rows = cur.fetchall()

            address_list = []
            ntt_name = []
            birth = []

            for row in rows:
                if row[0] == username :
                    for c in range (18) :
                        if c == 4 or c == 5 or c == 6 :
                            birth.append(row[c])
                        elif c ==1 or c == 2 or c == 3:
                            ntt_name.append(row[c])
                        elif c== 14 :
                            insert_oldschool = row[c]
                        elif c== 7 :
                            insert_program = row[c]

            insert_birth = ''.join(str(i) for i in birth)
            insert_name = ' '.join(str(i) for i in ntt_name)
            insert_room = ''.join(str(i) for i in room)

            print (insert_birth,insert_name)

            for e in address_list :
                print (e,end = " ")
            ran = []
            cur = conn.cursor()
            cur.execute("select * from HSpage1  ")
            results = cur.fetchall()
            x = (len(results))

            if x<10 :
                insert_regisnum = "000"+str(x) 
            elif x < 100 :
                insert_regisnum = "00"+str(x)
            else :
                insert_regisnum = "0"+str(x)

            print (insert_regisnum)
            timee = str(datetime.datetime.now().strftime("%H:%M:%S"))
            #insert_name,insert_regisnum,insert_date,insert_oldschool,y,insert_room,z,room[0],insert_program
            innsertt = "INSERT INTO HSprint (ID_num,name,regisnum,date,oldschool,roomnum,room,seatnum,building,program,time) VALUES  ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')".format(username,insert_name,insert_regisnum,insert_date,insert_oldschool,y,insert_room,z,room[0],insert_program,timee)
            connect.execute(innsertt)
            connect.commit()
            print(username,var_ntt, var_name,var_surname, var_program, var_ddd , var_mmm , var_yyy, var_regional ,var_nationality, var_religion, var_blood, var_phonenum, var_mail, var_oldschool, var_oldsubdis,var_oldprovince, var_edyear,var_gpa)
            print ("ok insert yet")
    enroll2.mainloop()
        
#--------------------------------------------------------------------------------------------------------------

class login_page:
    def __init__(self, top=None):
        global img1, img2
        top.geometry("1280x720")
        top.resizable(0, 0)
        top.title("HIGH SCHOOL STUDENT ENROLLMENT SYSTEM")
        root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))

        self.label1 = Label(root)
        self.label1.place(relx=0.005, rely=0, width=1270, height=720)
        self.img = PhotoImage(file=r"C:\Users\Admin\Desktop\project/pics/regispage2.png")
        self.label1.configure(image=self.img)


        self.entry1 = Entry(root)
        self.entry1.place(relx=0.45, rely=0.435, width=360, height=30)
        self.entry1.configure(bg = "#e6e6e6", font="-family {DB HelvethaicaMon X Med} -size 20")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.45, rely=0.535, width=360, height=30)
        self.entry2.configure(bg = "#e6e6e6" ,font="-family  {DB HelvethaicaMon X Bd} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="●")
        self.entry2.configure(textvariable=passwd)

        button1 = Button(root)                                                 
        button1.place(relx=0.345, rely=0.65, width=400, height=68)
        button1.configure(relief="flat")
        button1.configure(overrelief="flat")
        button1.configure(activebackground="#ffffff")
        button1.configure(cursor="hand2")
        button1.configure(foreground="#ffffff")
        button1.configure(background="#ffffff")
        button1.configure(borderwidth="0")
        img1 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\surebutton1.png")
        button1.configure(image=img1)       
        button1.configure(command=login)

        button2 = Button(root)
        button2.place(relx=0.2725, rely=0.83, width=580, height=60)
        button2.configure(relief="flat")
        button2.configure(overrelief="flat")
        button2.configure(activebackground="#ffffff")
        button2.configure(cursor="hand2")
        button2.configure(foreground="#ffffff")
        button2.configure(background="#ffffff")
        button2.configure(borderwidth="0")
        img2 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\loginbutton1.png")
        button2.configure(image=img2)
        button2.configure(command=edit)

####===============####=========================####========================####====================###======
def edit (Event=None) :
    global username,password
    global img5
    username = user.get()
    password = passwd.get()
    with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
        cur = db.cursor()
    find_user = "SELECT * FROM HSlogin WHERE ID_num = ? and Password = ?"
    cur.execute(find_user, [username, password])
    results = cur.fetchall()
    if results:
        #messagebox.showinfo("Login Page", "The login is successful")
        root.geometry("1280x720")
        root.title("HIGH SCHOOL STUDENT ENROLLMENT SYSTEM")
        root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))

        label1 = Label(root)
        label1.place(relx=0.005, rely=0, width=1270, height=720)
        img = PhotoImage(file=r"C:\Users\Admin\Desktop\project/pics/print.png")
        label1.configure(image= img)


        button3 = Button(root)
        button3.place(relx=0.005, rely=0.005,width=50, height=50)
        #button3.grid(row=0,column=1)
        button3.configure(relief="flat")
        button3.configure(overrelief="flat")
        button3.configure(activebackground="#d5dded")
        button3.configure(cursor="hand2")
        button3.configure(foreground="#d5dded")
        button3.configure(background="#ffffff")
        button3.configure(borderwidth="0")
        img3 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\butbk.png")
        button3.configure(image=img3)
        button3.configure(command= enrolHSS)

        
        global img5
        username = user.get()
        #text_font = ("DB Helvethaica X Med Cond", "27")
        text_font = ("TH Niramit AS", "25")

        message = Label(root)
        message.place(relx=0.61, rely=0.062, width=300, height=30)
        message.configure(font=text_font,fg="#0600ff",bg="#ffffff",text=username, anchor="w")

        with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
            cur = db.cursor()

        conn = sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
        print('Connected to database successfully.')
        
        cur = conn.cursor()
        cur.execute("select * from HSpage1  ")
        rows = cur.fetchall()

        address_list = []
        ntt_name = []
        birth = []

        for row in rows:
            if row[0] == username :
                '''for a in range (18) :
                    address_list.append(row[a])
                
                for b in address_list :
                    print (b,end = " ")'''

                for c in range (18) :
                    if c == 4 or c == 5 or c == 6 :
                        birth.append(row[c])
                    elif c ==1 or c == 2 :
                        ntt_name.append(row[c])
                
                for d in range (19,27) :
                    '''if row[d] == "-" :
                        print ("none",row[d])'''

                    if d == 19 :
                        add = " เลขที่"
                        address_list.append(add)
                        address_list.append(row[d])
                    elif d == 20 :
                        add = "   หมู่"
                        address_list.append(add)
                        address_list.append(row[d])
                    elif d == 21  :
                        if row[21] != "-" and row[22] != "-" :
                            print (row[21],row[22])
                            add = "   ซอย"
                            address_list.insert(4,add)
                            address_list.insert(5,row[21])
                            streett = "   ถนน"
                            address_list.insert(6,streett)
                            address_list.insert(7,row[22])

                        elif row[21] != "-" and row[22] == "-" :
                            print (row[21],row[22])
                            add = "   ซอย"
                            address_list.insert(4,add)
                            address_list.insert(5,row[21])

                        elif row[21] == "-" and row[22] != "-" :
                            print (row[21],row[22])
                            streett = "   ถนน"
                            address_list.insert(4,streett)
                            address_list.insert(5,row[22])




                    elif d == 21 :
                        if row[d] != "-" :
                            print (row[d])
                            add = "   ซอย"
                            address_list.insert(4,add)
                            address_list.insert(5,row[d])
                    elif d == 23 :
                        add = "   ตำบล"
                        address_list.append(add)
                        address_list.append(row[d])
                    elif d == 24 :
                        add = "   อำเภอ"
                        address_list.append(add)
                        address_list.append(row[d])
                    elif d == 25 :
                        add = "   จังหวัด"
                        address_list.append(add)
                        address_list.append(row[d])
                    elif d == 26 :
                        add = ""
                        address_list.append(add)
                        address_list.append(row[d])
                    


                for e in address_list :
                    print (e,end = " ")
                

                message = Label(root) ### nametilte+name
                message.place(relx=0.11, rely=0.215, width=200, height=35)
                message.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text= '  '.join(str(i) for i in ntt_name) ,anchor="w" )

                message1 = Label(root) ### surname
                message1.place(relx=0.435, rely=0.215, width=180, height=35)
                message1.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text= row [3] ,anchor="w" )

                message2 = Label(root) ### birthday
                message2.place(relx=0.77, rely=0.215, width=220, height=35)
                message2.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = ' '.join(map(str,birth)) ,anchor="w" )
                #message2.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = "31 พฤศจิกายน 2554" ,anchor="w" )

                message3 = Label(root) #blood
                message3.place(relx=0.17, rely=0.282, width=120, height=35)
                message3.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[11] ,anchor="w" )

                message4 = Label(root) #regional
                message4.place(relx=0.37, rely=0.282, width=120, height=35)
                message4.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[8] ,anchor="w" )

                message5 = Label(root) #nationality
                message5.place(relx=0.59, rely=0.282, width=120, height=35)
                message5.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[9] ,anchor="w" )

                message6 = Label(root) #religion
                message6.place(relx=0.78 , rely=0.282, width=120, height=35)
                message6.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[10] ,anchor="w" )

                message7 = Label(root) #phonenum
                message7.place(relx=0.22, rely=0.349, width=200, height=35)
                message7.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[12] ,anchor="w" )

                message8 = Label(root) #email
                message8.place(relx=0.5 , rely=0.349, width=400, height=35)
                message8.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[13] ,anchor="w" )

                message9= Label(root) #program
                message9.place(relx=0.28 , rely=0.416, width=500, height=35)
                message9.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[7] ,anchor="w" )

                message10= Label(root) #oldschool
                message10.place(relx=0.2 , rely=0.550, width=500, height=35)
                message10.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[14] ,anchor="w" )

                message11 = Label(root) #olddis
                message11.place(relx=0.78 , rely=0.550, width=200, height=35)
                message11.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[15] ,anchor="w" )
    
                message12 = Label(root) #oldprovince
                message12.place(relx=0.16 , rely=0.617, width=150, height=35)
                message12.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[16] ,anchor="w" )

                message13 = Label(root) #edyear
                message13.place(relx=0.55 , rely=0.617, width=120, height=35)
                message13.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[17] ,anchor="w" )

                message14 = Label(root) #gpa
                message14.place(relx=0.765 , rely=0.617, width=120, height=35)
                message14.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[18] ,anchor="w" )

                message15 = Label(root) #address
                message15.place(relx=0.125 , rely=0.745, width=1050, height=45)
                message15.configure(font = "-family {TH Niramit AS} -size 21", fg="#0600ff", bg="#cdd6ea" , text =' '.join(str(i) for i in address_list) ,anchor="w" )

                message16 = Label(root) #parent
                message16.place(relx=0.18 , rely=0.815, width=500, height=40)
                message16.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[36] ,anchor="w" )

                message16 = Label(root) #parentphone
                message16.place(relx=0.75 , rely=0.815, width=200, height=35)
                message16.configure(font = text_font, fg="#0600ff", bg="#cdd6ea" , text = row[39] ,anchor="w" )

                button5 = Button(root)                                                 
                button5.place(relx=0.385, rely=0.9219, width=294, height=50)
                button5.configure(relief="flat")
                button5.configure(overrelief="flat")
                button5.configure(activebackground="#4aa481")
                button5.configure(cursor="hand2")
                button5.configure(foreground="#4aa481")
                button5.configure(background="#4aa481")
                button5.configure(borderwidth="0")
                img5 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\print1.png")
                button5.configure(image=img5)       
                button5.configure(command=testvoucherHS)


                print("")
                print("ID_num : "+str(row[0]))
                print("Nametitle: "+row[1])
                print("Name: "+row[2])
                print("Surname : "+row[3])
                print("GPA : "+row[18])
                print ("parent : ",row[36])
                ran = []
                cur = conn.cursor()
                cur.execute("select * from JHSpage1  ")
                results = cur.fetchall()
                x = (len(results))
                if x < 100 :
                    print ("00"+str(x))
                else :
                    print ("0"+str(x))

    else:
        messagebox.showerror("Error", "Incorrect username or password.")
        page1.entry2.delete(0, END)
   
    root.mainloop()

#--------------------------------------------------------------------------------------------------------------
class HS_window :
    def __init__(self, top=None):
        global img2,img3
        top.geometry("1280x720")
        top.resizable(0, 0)
        top.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))
        top.title("HIGH SCHOOL ENROLLMENT SYSTEM")
    #--------------------------------------------------------------------------------------------------------#
        self.label = Label(enroll)
        self.label.place(relx=0, rely=0, width=1280, height=720)
        self.img = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics/HSregis1.png")
        self.label.configure(image=self.img)

        button2 = Button(enroll)
        button2.place(relx=0.955, rely=0.88, width=50, height=50)
        button2.configure(relief="flat")
        button2.configure(overrelief="flat")
        button2.configure(activebackground="#d5dded")
        button2.configure(cursor="hand2")
        button2.configure(foreground="#d5dded")
        button2.configure(background="#d5dded")
        button2.configure(borderwidth="0")
        img2 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\but.png")
        button2.configure(image=img2)
        button2.configure(command=next)

        button3 = Button(enroll)
        button3.place(relx=0.005, rely=0.005,width=50, height=50)
        #button3.grid(row=0,column=1)
        button3.configure(relief="flat")
        button3.configure(overrelief="flat")
        button3.configure(activebackground="#d5dded")
        button3.configure(cursor="hand2")
        button3.configure(foreground="#d5dded")
        button3.configure(background="#ffffff")
        button3.configure(borderwidth="0")
        img3 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\butbk.png")
        button3.configure(image=img3)
        button3.configure(command= mainn)



        self.message = Label(enroll)
        self.message.place(relx=0.32, rely=0.2, width=136, height=30)
        self.message.configure(font="-family {DB Helvethaica X Med Cond} -size 20")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")
        
    #---------------------------------------#CURSORRR-----------------------------------------------------------------#
        self.entry_name = Entry(enroll) 
        self.entry_name.place(relx=0.39, rely=0.325, width=250, height=24)
        self.entry_name.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_name.configure(relief="flat")
        #self.entry_name.configure(background="#000000")
        self.entry_name.configure(textvariable= name)

        self.entry_surname = Entry(enroll) 
        self.entry_surname.place(relx=0.69, rely=0.325, width=250, height=24)
        self.entry_surname.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_surname.configure(relief="flat")
        #self.entry_surname.configure(background="#000000")
        self.entry_surname.configure(textvariable= surname)

        self.entry_blood = Entry(enroll) 
        self.entry_blood.place(relx=0.625, rely=0.4125, width=70, height=24)
        self.entry_blood.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_blood.configure(relief="flat")
        #self.entry_blood.configure(background="#000000")
        self.entry_blood.configure(textvariable= blood)

        self.entry_regional = Entry(enroll) 
        self.entry_regional.place(relx=0.175, rely=0.5055, width=150, height=24)
        self.entry_regional.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_regional.configure(relief="flat")                 
        #self.entry_regional.configure(background="#000000")
        self.entry_regional.configure(textvariable= regional) 

        self.entry_nationality= Entry(enroll) 
        self.entry_nationality.place(relx=0.46, rely=0.5057, width=150, height=24)
        self.entry_nationality.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_nationality.configure(relief="flat")
        #self.entry_nationality.configure(background="#000000")
        self.entry_nationality.configure(textvariable= nationality)
        
        self.entry_religion= Entry(enroll) 
        self.entry_religion.place(relx=0.754, rely=0.5055, width=150, height=24)
        self.entry_religion.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_religion.configure(relief="flat")
        #self.entry_religion.configure(background="#000000")
        self.entry_religion.configure(textvariable= religion )

        self.entry_phonenum= Entry(enroll) 
        self.entry_phonenum.place(relx=0.228, rely=0.5825, width=200, height=24)
        self.entry_phonenum.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_phonenum.configure(relief="flat")
        #self.entry_phonenum.configure(background="#000000")
        self.entry_phonenum.configure(textvariable= phonenum )

        self.entry_mail= Entry(enroll) 
        self.entry_mail.place(relx=0.57, rely=0.583, width=350, height=24)
        self.entry_mail.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_mail.configure(relief="flat")
        #self.entry_mail.configure(background="#000000")
        self.entry_mail.configure(textvariable= mail )

        self.entry_oldschool= Entry(enroll) 
        self.entry_oldschool.place(relx=0.239, rely=0.7725, width=450, height=24)
        self.entry_oldschool.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_oldschool.configure(relief="flat")
        #self.entry_oldschool.configure(background="#000000")
        self.entry_oldschool.configure(textvariable= oldschool )

        self.entry_oldsubdis= Entry(enroll) 
        self.entry_oldsubdis.place(relx=0.719, rely=0.7725, width=200, height=24)
        self.entry_oldsubdis.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_oldsubdis.configure(relief="flat")
        #self.entry_oldsubdis.configure(background="#000000")
        self.entry_oldsubdis.configure(textvariable= oldsubdis )

        self.entry_oldprovince= Entry(enroll) 
        self.entry_oldprovince.place(relx=0.172, rely=0.848, width=200, height=24)
        self.entry_oldprovince.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_oldprovince.configure(relief="flat")
        #self.entry_oldprovince.configure(background="#000000")
        self.entry_oldprovince.configure(textvariable= oldprovince)

        self.entry_edyear= Entry(enroll) 
        self.entry_edyear.place(relx=0.545, rely=0.85, width=100, height=24)
        self.entry_edyear.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_edyear.configure(relief="flat")
        #self.entry_edyear.configure(background="#000000")
        self.entry_edyear.configure(textvariable= edyear)

        self.entry_gpa= Entry(enroll)
        self.entry_gpa.place(relx=0.765, rely=0.85, width=100, height=24)
        self.entry_gpa.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_gpa.configure(relief="flat")
        #self.entry_gpa.configure(background="#000000")
        self.entry_gpa.configure(textvariable= gpa)

        #PROGRAM
        self.coprogram = [" ห้องเรียนวิทย์ คณิต"," ห้องเรียนวิทย์ สุขภาพ"," ห้องเรียนวิทย์ คอม"," ห้องเรียนศิลป์ คณิต"," ห้องเรียนศิลป์ ภาษา"," ห้องเรียนพิเศษ GIFTED PROGRAM "," ห้องเรียนพิเศษ ENGLISH PROGRAM"]
        self.program = ttk.Combobox(top,value = self.coprogram)
        #self.program.current(0)
        self.program.place(relx=0.757, rely=0.2, width=230 , height=30)
        self.program.configure(font="-family {DB Helvethaica X Med Cond} -size 15")
        self.program.configure(foreground="#184f78")
        self.program.configure(textvariable = program)

        #nametitle
        self.nttlist = ["   นาย","   นางสาว","   เด็กชาย","   เด็กหญิง"]
        self.ntt = ttk.Combobox(top,value = self.nttlist)
        self.ntt.place(relx=0.18, rely=0.325, width=150 , height=30)
        self.ntt.configure(font="-family {DB Helvethaica X Med Cond} -size 19")
        self.ntt.configure(foreground="#184f78")
        self.ntt.configure(textvariable = ntt)

        #---------------------------------------------------------------------------------------------------
    #########--------------------------------------------------- #BIRTHDAY----------------------------#######
        text_font = ("DB Helvethaica X Med Cond", "15")

        self.ddd = ttk.Combobox(enroll)
        self.ddd.place(relx=0.245, rely=0.41, width=75, height=30)
        self.ddd.configure(foreground="#184f78")
        find_birthday = "SELECT ddd FROM birthdayHS"


        cur.execute(find_birthday)
        result1 = cur.fetchall()
        birthday = []
        for i in range(len(result1)):
            if(result1[i][0] not in birthday):
                birthday.append(result1[i][0])

        self.ddd.configure(values=birthday)
        self.ddd.configure(state="readonly")
        self.ddd.configure(font="-family {DB Helvethaica X Med Cond} -size 18")
        self.ddd.option_add("*TCombobox*Listbox.font", text_font) #------------------------------DAYY
        self.ddd.configure(foreground="#184f78")
        self.ddd.option_add("*TCombobox*Listbox.selectBackground", "#ff8cbf")
        
        self.mmm = ttk.Combobox(enroll)
        self.mmm.place(relx=0.3125, rely=0.41, width=110, height=30)
        self.mmm.configure(font="-family {DB Helvethaica X Med Cond} -size 18")
        self.mmm.option_add("*TCombobox*Listbox.font", text_font)  #-----------------------------MONTH
        self.mmm.configure(foreground="#184f78")
        self.mmm.option_add("*TCombobox*Listbox.selectBackground", "#ff8cbf")
        self.mmm.configure(state="disabled")
        self.mmm.configure(textvariable = mmm)

        self.yyy = ttk.Combobox(enroll)
        self.yyy.place(relx=0.408, rely=0.41, width=70, height=30)
        self.yyy.configure(state="disabled")
        self.yyy.configure(font="-family {DB HelvethaicaMon X Blk} -size 18")
        self.yyy.option_add("*TCombobox*Listbox.font", text_font) #------------------------------YEARS
        self.yyy.option_add("*TCombobox*Listbox.selectBackground", "#ff8cbf")
        self.yyy.configure(foreground="#184f78")
        self.ddd.bind("<<ComboboxSelected>>", self.get_mmm)
        self.yyy.configure(textvariable = yyy)
        self.ddd.configure(textvariable = ddd )

        #-------------
         
        #self.yyy.configure(textvariable = yyy)
    #########-------------------------------------------------------------------------------------------#######

    def get_mmm(self, Event):
        self.mmm.configure(state="readonly")
        self.mmm.set('')
        self.yyy.set('')
        find_mmm = "SELECT mmm FROM birthdayHS WHERE ddd = ?"
        self.yyy.configure(font="-family {DB Helvethaica X Med Cond} -size 20")
        cur.execute(find_mmm, [self.ddd.get()])
        result2 = cur.fetchall()
        mmm = []
        for j in range(len(result2)):
            if(result2[j][0] not in mmm):
                mmm.append(result2[j][0])
        
        self.mmm.configure(values=mmm)
        self.mmm.bind("<<ComboboxSelected>>", self.get_yyy)
        self.yyy.configure(state="disabled")


    def get_yyy(self, Event):
        self.yyy.configure(state="readonly")
        self.yyy.set('')
        find_yyy = "SELECT yyy FROM birthdayHS WHERE ddd = ? and mmm = ?"
        cur.execute(find_yyy, [self.ddd.get(), self.mmm.get()])
        result3 = cur.fetchall()
        yyy = []
        for k in range(len(result3)):
            yyy.append(result3[k][0])

        self.yyy.configure(values=yyy)

 #---------------------------------------------------------------------------------------------------- 
class HS_window2 :
    def __init__(self, top=None):
        global img2 , img3,img4,img5
        top.geometry("1280x720")
        top.resizable(0, 0)
        top.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))
        top.title("HIGH SCHOOL ENROLLMENT SYSTEM")
    #--------------------------------------------------------------------------------------------------------#
        self.label2 = Label(enroll2)
        self.label2.place(relx=0, rely=0, width=1280, height=720)
        self.img = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics/JHSregis2.png")
        self.label2.configure(image=self.img)


        button3 = Button(enroll2)
        button3.place(relx=0.005, rely=0.005,width=50, height=50)
        #button3.grid(row=0,column=1)
        button3.configure(relief="flat")
        button3.configure(overrelief="flat")
        button3.configure(activebackground="#d5dded")
        button3.configure(cursor="hand2")
        button3.configure(foreground="#d5dded")
        button3.configure(background="#ffffff")
        button3.configure(borderwidth="0")
        img3 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\butbk.png")
        button3.configure(image=img3)
        button3.configure(command= moreopen)

        button4 = Button(enroll2)
        button4.place(relx=0.905, rely=0.863, width=50, height=50)
        button4.configure(relief="flat")
        button4.configure(overrelief="flat")
        button4.configure(activebackground="#ced5ea")
        button4.configure(cursor="hand2")
        button4.configure(foreground="#ced5ea")
        button4.configure(background="#ced5ea")
        button4.configure(borderwidth="0")
        img4 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\confirm.png")
        button4.configure(image=img4)
        button4.configure(command=yes)

        button5 = Button(enroll2)
        button5.place(relx=0.95, rely=0.9, width=50, height=50)
        button5.configure(relief="flat")
        button5.configure(overrelief="flat")
        button5.configure(activebackground="#ced5ea")
        button5.configure(cursor="hand2")
        button5.configure(foreground="#ced5ea")
        button5.configure(background="#ced5ea")
        button5.configure(borderwidth="0")
        img5 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\but.png")
        button5.configure(image=img5)
        button5.configure(command=lastpage)

        #bt=tk.Button(enroll2,text='page1',command= moreopen )
        #bt.grid(column=0,row=0)
    #---------------------------------------#CURSORRR page 3-----------------------------------------------------------------#
    
        self.entry_address = Entry(enroll2) 
        self.entry_address.place(relx=0.177, rely=0.154, width=220, height=24)
        self.entry_address.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_address.configure(relief="flat")
        #self.entry_address.configure(background="#000000")
        self.entry_address.configure(textvariable=address) 

        self.entry_villnum = Entry(enroll2) 
        self.entry_villnum.place(relx=0.47, rely=0.154, width=220, height=24)
        self.entry_villnum.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_villnum.configure(relief="flat")
        #self.entry_villnum.configure(background="#000000")
        self.entry_villnum.configure(textvariable= villnum)

        self.entry_alley = Entry(enroll2) 
        self.entry_alley.place(relx=0.73, rely=0.154, width=200, height=24)
        self.entry_alley.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_alley.configure(relief="flat")
        #self.entry_alley.configure(background="#000000")
        self.entry_alley.configure(textvariable= alley)
        #---------------

        self.entry_street = Entry(enroll2) 
        self.entry_street.place(relx=0.14, rely=0.23, width=250, height=24)
        self.entry_street.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_street.configure(relief="flat")
        #self.entry_street.configure(background="#000000")
        self.entry_street.configure(textvariable=street) 

        self.entry_subdistrict = Entry(enroll2) 
        self.entry_subdistrict.place(relx=0.455, rely=0.23, width=220, height=24)
        self.entry_subdistrict.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_subdistrict.configure(relief="flat")
        #self.entry_subdistrict.configure(background="#000000")
        self.entry_subdistrict.configure(textvariable= subdistrict)

        self.entry_district = Entry(enroll2) 
        self.entry_district.place(relx=0.738, rely=0.23, width=180, height=24)
        self.entry_district.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_district.configure(relief="flat")
        #self.entry_district.configure(background="#000000")
        self.entry_district.configure(textvariable= district)
        #---------------
        
        self.entry_province = Entry(enroll2) 
        self.entry_province.place(relx=0.16, rely=0.3065, width=250, height=24)
        self.entry_province.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_province.configure(relief="flat")
        #self.entry_province.configure(background="#000000")
        self.entry_province.configure(textvariable=province) 

        self.entry_postnum = Entry(enroll2) 
        self.entry_postnum.place(relx=0.52, rely=0.306, width=220, height=24)
        self.entry_postnum.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_postnum.configure(relief="flat")
        #self.entry_postnum.configure(background="#000000")
        self.entry_postnum.configure(textvariable= postnum)
        #---------------

        self.entry_dadname = Entry(enroll2) 
        self.entry_dadname.place(relx=0.23, rely=0.493, width=400, height=24)
        self.entry_dadname.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_dadname.configure(relief="flat")
        #self.entry_dadname.configure(background="#000000")
        self.entry_dadname.configure(textvariable=dadname) 

        self.entry_dadoc = Entry(enroll2) 
        self.entry_dadoc.place(relx=0.69, rely=0.493, width=220, height=24)
        self.entry_dadoc.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_dadoc.configure(relief="flat")
        #self.entry_dadoc.configure(background="#000000")
        self.entry_dadoc.configure(textvariable= dadoc)
        #---------------

        self.entry_dadoffice = Entry(enroll2) 
        self.entry_dadoffice.place(relx=0.23, rely=0.555, width=400, height=24)
        self.entry_dadoffice.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_dadoffice.configure(relief="flat")
        #self.entry_dadoffice.configure(background="#000000")
        self.entry_dadoffice.configure(textvariable=dadoffice) 

        self.entry_dadphone = Entry(enroll2) 
        self.entry_dadphone.place(relx=0.728, rely=0.555, width=170, height=24)
        self.entry_dadphone.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_dadphone.configure(relief="flat")
        #self.entry_dadphone.configure(background="#000000")
        self.entry_dadphone.configure(textvariable= dadphone)
        #---------------
        #----------------
        #---------------
        self.entry_momname = Entry(enroll2) 
        self.entry_momname.place(relx=0.255, rely=0.628, width=400, height=24)
        self.entry_momname.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_momname.configure(relief="flat")
        #self.entry_momname.configure(background="#000000")
        self.entry_momname.configure(textvariable=momname) 

        self.entry_momoc = Entry(enroll2) 
        self.entry_momoc.place(relx=0.69, rely=0.628, width=220, height=24)
        self.entry_momoc.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_momoc.configure(relief="flat")
        #self.entry_momoc.configure(background="#000000")
        self.entry_momoc.configure(textvariable= momoc)
        #---------------

        self.entry_momoffice = Entry(enroll2) 
        self.entry_momoffice.place(relx=0.23, rely=0.690, width=400, height=24)
        self.entry_momoffice.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_momoffice.configure(relief="flat")
        #self.entry_momoffice.configure(background="#000000")
        self.entry_momoffice.configure(textvariable=momoffice) 

        self.entry_momphone = Entry(enroll2) 
        self.entry_momphone.place(relx=0.728, rely=0.690, width=170, height=24)
        self.entry_momphone.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_momphone.configure(relief="flat")
        #self.entry_momphone.configure(background="#000000")
        self.entry_momphone.configure(textvariable= momphone)
        #---------------


        self.entry_parentrelate = Entry(enroll2) 
        self.entry_parentrelate .place(relx=0.35, rely=0.763, width=200, height=24)
        self.entry_parentrelate .configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_parentrelate .configure(relief="flat")
        #self.entry_parentrelate .configure(background="#000000")
        self.entry_parentrelate .configure(textvariable= parentrelate)
        #---------------

        self.entry_parentname = Entry(enroll2) 
        self.entry_parentname.place(relx=0.195, rely=0.828, width=450, height=24)
        self.entry_parentname.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_parentname.configure(relief="flat")
        #self.entry_parentname.configure(background="#000000")
        self.entry_parentname.configure(textvariable=parentname) 

        self.entry_parentoc = Entry(enroll2) 
        self.entry_parentoc.place(relx=0.695, rely=0.828, width=220, height=24)
        self.entry_parentoc.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_parentoc.configure(relief="flat")
        #self.entry_parentoc.configure(background="#000000")
        self.entry_parentoc.configure(textvariable= parentoc)
        #---------------

        self.entry_parentoffice = Entry(enroll2) 
        self.entry_parentoffice.place(relx=0.23, rely=0.89, width=400, height=24)
        self.entry_parentoffice.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_parentoffice.configure(relief="flat")
        #self.entry_parentoffice.configure(background="#000000")
        self.entry_parentoffice.configure(textvariable=parentoffice) 

        self.entry_parentphone = Entry(enroll2) 
        self.entry_parentphone.place(relx=0.728, rely=0.89, width=170, height=24)
        self.entry_parentphone.configure(font="-family {DB Helvethaica X Med Cond} -size 20", fg="#184f78")
        self.entry_parentphone.configure(relief="flat")
        #self.entry_parentphone.configure(background="#000000")
        self.entry_parentphone.configure(textvariable= parentphone)

def moreopen () : #back to page 1
        global enroll
        global page2
        enroll2.destroy()
        page2 = HS_window(enroll)
        enroll.mainloop()

def testvoucherHS (Event=None) :
    root.geometry("1120x700")
    root.title("HIGH SCHOOL STUDENT ENROLLMENT SYSTEM")
    root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))

    label1 = Label(root)
    label1.place(relx=0.005, rely=0, width=1120, height=700)
    img = PhotoImage(file=r"C:\Users\Admin\Desktop\project/pics/testvoucherHS.png")
    label1.configure(image= img)
    
    global img5
    username = user.get()
    #text_font = ("DB Helvethaica X Med Cond", "27")
    text_font = ("TH Niramit AS", "25")

    with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
        cur = db.cursor()

    conn = sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
    print('Connected to database successfully.')
    
    cur = conn.cursor()
    cur.execute("select * from HSprint  ")
    rows = cur.fetchall()
    for row in rows:
        print (row[0])
        if row[0] == username :
            showup = Label(root) ### regisnum
            showup.place(relx=0.4, rely=0.176, width=100, height=35)
            showup.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[2] ,anchor="w" )

            showup1 = Label(root) ### date
            showup1.place(relx=0.64, rely=0.176, width=220, height=35)
            showup1.configure(font = text_font,fg="#474747", bg="#ffffff"  , text= row[3] ,anchor="w" )

            showup2 = Label(root) ### name
            showup2.place(relx=0.207, rely=0.61, width=300, height=35)
            showup2.configure(font = text_font, fg="#474747", bg="#ffffff" ,  text= row[1] ,anchor="w" )

            if len(row[4]) >= 25 :
                showup3 = Label(root) #school
                showup3.place(relx=0.68, rely=0.62, width=450, height=35)
                showup3.configure(font="-family {TH Niramit AS} -size 20", fg="#474747", bg="#ffffff" ,  text = row[4] ,anchor="w" )
            
            else :
                showup3 = Label(root) #school
                showup3.place(relx=0.68, rely=0.62, width=450, height=35)
                showup3.configure(font="-family {TH Niramit AS} -size 25", fg="#474747", bg="#ffffff" ,  text = row[4] ,anchor="w" )

            showup4 = Label(root) #roomnum
            showup4.place(relx=0.228, rely=0.697, width=50, height=35)
            showup4.configure(font = text_font, fg="#474747", bg="#ffffff" , text = row[5] ,anchor="w" )

            showup5 = Label(root) #room
            showup5.place(relx=0.65, rely=0.705, width=100, height=35)
            showup5.configure(font = text_font,fg="#474747", bg="#ffffff" ,  text =  row[6],anchor="w" )

            showup6 = Label(root) #no.
            showup6.place(relx=0.228 , rely=0.78, width=50, height=35)
            showup6.configure(font = text_font,fg="#474747", bg="#ffffff" ,text = row[7] ,anchor="w" )

            showup7 = Label(root) #building
            showup7.place(relx=0.68, rely=0.78, width=50, height=35)
            showup7.configure(font = text_font, fg="#474747", bg="#ffffff" ,  text =row[8],anchor="w" )

            showup8 = Label(root) #program
            showup8.place(relx=0.25, rely=0.855, width=360, height=35)
            showup8.configure(font = text_font, fg="#474747", bg="#ffffff" ,  text = row[9] ,anchor="w" )


    root.mainloop()

#----------------------------------------------------------------------
def lastpage () :
    
    root.geometry("1280x720")
    root.title("HIGH SCHOOL STUDENT ENROLLMENT SYSTEM")
    root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))
    
    global img,img1,img2,img3
    global enroll,enroll2
    global page2
    enroll.withdraw()

    page2 = HS_window(enroll)

    label1 = Label(enroll2)
    label1.place(relx=0.005, rely=0, width=1280, height=720)
    img = PhotoImage(file=r"C:\Users\Admin\Desktop\project/pics/lastpageHS.png")
    label1.configure(image= img)
    
    button2 = Button(enroll2)
    button2.place(relx=0.632, rely=0.75, width=250, height=42)
    button2.configure(relief="flat")
    button2.configure(overrelief="flat")
    button2.configure(activebackground="#63a3e4")
    button2.configure(cursor="hand2")
    button2.configure(foreground="#63a3e4")
    button2.configure(background="#63a3e4")
    button2.configure(borderwidth="0")
    img2 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\butt2.png")
    button2.configure(image=img2)
    button2.configure(command=main)

    button3 = Button(enroll2)
    button3.place(relx=0.18, rely=0.75, width=250, height=42)
    button3.configure(relief="flat")
    button3.configure(overrelief="flat")
    button3.configure(activebackground="#4aa481")
    button3.configure(cursor="hand2")
    button3.configure(foreground="#4aa481")
    button3.configure(background="#4aa481")
    button3.configure(borderwidth="0")
    img3 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\butt3.png")
    button3.configure(image=img3)
    button3.configure(command=enrolHS)

    enroll2.mainloop()
##---###----###
def main():
    enroll2.withdraw()
    os.system(r"python C:\Users\Admin\Desktop\project\pics\main.py")
    root.deiconify()

def mainn():
    enroll.withdraw()
    os.system(r"python C:\Users\Admin\Desktop\project\pics\main.py")
    root.deiconify()

def enrolHS():
    enroll2.withdraw()
    os.system(r"python C:\Users\Admin\Desktop\project\pics\enrolHS.py")
    #main.deiconify()


def enrolHSS():
    root.withdraw()
    os.system(r"python C:\Users\Admin\Desktop\project\pics\enrolHS.py")
    #main.deiconify()
####---------------------------######---------------------------------#############-----------------------


page1 = login_page(root)
root.bind("<Return>", login)
root.mainloop()