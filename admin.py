###### ADMIN PAGE ######
#==================imports===================
import os
import sqlite3

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from time import strftime
from datetime import date

#============================================



root = Tk()
 
root.geometry("1280x720")
root.title("STUDENT ENROLLMENT SYSTEM")
root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))

######----------------------- VARIABLE -----------------------------------######

user = StringVar()
passwd = StringVar()
nametitle = StringVar()
name = StringVar()
surname = StringVar()


with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
    cur = db.cursor()


def login(Event=None):
    global username,password
    global admin
    global page2
    username = user.get()
    password = passwd.get()
    
    if username == "f" or username == "admin" or username == "1478523698745" or username == "warisa" or username == "admint" :
        messagebox.showinfo("Login Page", "The login is successful")
        root.withdraw()
        admin = Toplevel()
        page2 = admin_window(admin)
        admin.protocol("WM_DELETE_WINDOW", exitt)
        admin.mainloop()
    elif len(username) >= 1 :
        if len(password) >= 6 :
            with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
                cur = db.cursor()
                find_user = "SELECT * FROM ADMIN WHERE username = ?"
                cur.execute(find_user, [username])
                results = cur.fetchall()
                if results:
                    messagebox.showinfo("Login Page", "The login is successful")
                    page1.entry1.delete(0, END)
                    page1.entry2.delete(0, END)
                    root.withdraw()
                    admin = Toplevel()
                    page2 = admin_window(admin)
                    admin.protocol("WM_DELETE_WINDOW", exitt)
                    admin.mainloop()
                else :
                    messagebox.showerror("Error", "กรุณากรอกข้อมูลที่ถูกต้อง")
                    page1.entry2.delete(0, END)
        else :
            messagebox.showerror("Error", "กรุณากรอกข้อมูลที่ถูกต้อง")
            page1.entry2.delete(0, END)

    else :
        messagebox.showerror("Error", "กรุณากรอกข้อมูลที่ถูกต้อง")
        page1.entry2.delete(0, END)
#--------------------------------------------------------------------------------------------------------------
def logout():
    sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=admin)
    if sure == True:
        admin.destroy()
        root.deiconify()
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)

#--------------------------------------------------------------------------------------------------------------

def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=admin)
    if sure == True:
        admin.destroy()
        root.destroy()       
#--------------------------------------------------------------------------------------------------------------

class login_page:
    def __init__(self, top=None):
        global img1, img2
        top.geometry("1280x720")
        top.resizable(0, 0)
        top.title("ADMIN STUDENT ENROLLMENT SYSTEM")
        root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))

        self.label1 = Label(root)
        self.label1.place(relx=0.005, rely=0, width=1270, height=720)
        self.img = PhotoImage(file=r"C:\Users\Admin\Desktop\project/pics/admin_page.png")
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
        button1.place(relx=0.42, rely=0.68 , width=200, height=47)
        button1.configure(relief="flat")
        button1.configure(overrelief="flat")
        button1.configure(activebackground="#ffffff")
        button1.configure(cursor="hand2")
        button1.configure(foreground="#ffffff")
        button1.configure(background="#ffffff")
        button1.configure(borderwidth="0")
        img1 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\admin_login.png")
        button1.configure(image=img1)       
        button1.configure(command=login)

#--------------------------------------------------------------------------------------------------------------
class admin_window :
    def __init__(self, top=None):
        global img2,img3
        top.geometry("1280x720")
        top.resizable(0, 0)
        top.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))
        top.title("ADMIN ENROLLMENT SYSTEM")
    #--------------------------------------------------------------------------------------------------------#
        self.label = Label(admin)
        self.label.place(relx=0, rely=0, width=1280, height=720)
        self.img = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics/choose.png")
        self.label.configure(image=self.img)


        button2 = Button(admin)                                                 
        button2.place(relx=0.148, rely=0.25 , width=324, height=357)
        button2.configure(relief="flat")
        button2.configure(overrelief="flat")
        button2.configure(activebackground="#ffffff")
        button2.configure(cursor="hand2")
        button2.configure(foreground="#ffffff")
        button2.configure(background="#ffffff")
        button2.configure(borderwidth="0")
        img2= PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\m1.png")
        button2.configure(image=img2)       
        button2.configure(command=showm1)

    

        button3 = Button(admin)                                                 
        button3.place(relx=0.6 , rely=0.25 , width=324, height=357)
        button3.configure(relief="flat")
        button3.configure(overrelief="flat")
        button3.configure(activebackground="#ffffff")
        button3.configure(cursor="hand2")
        button3.configure(foreground="#ffffff")
        button3.configure(background="#ffffff")
        button3.configure(borderwidth="0")
        img3= PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\m4.png")
        button3.configure(image=img3)       
        button3.configure(command=showm4)
        
####---------------------------######---------------------------------#############-----------------------
def showm1 (Event=None) :
    root.geometry("1280x720")
    root.title("ADMIN STUDENT ENROLLMENT SYSTEM")
    root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))
    global img

    label1 = Label(admin)
    label1.place(relx=0.005, rely=0, width=1280, height=720)
    img = PhotoImage(file=r"C:\Users\Admin\Desktop\project/pics/showm1.png")
    label1.configure(image= img)

    button3 = Button(admin)
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
    
    #text_font = ("DB Helvethaica X Med Cond", "27")
    text_font = ("TH Niramit AS", "17")

    with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
        cur = db.cursor()

    connect = sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
    print('Connected to database successfully.')
    
    cur = connect.cursor()
    cur.execute("select * from JHSprint  ")
    rows = cur.fetchall()
    k = 0
    for row in rows :
        print (row[2],row[1],row[4],row[7],row[6],row[5],row[8],row[9],end= "  ")
        showup = Label(admin) ### regisnum
        showup.place(relx=0.07, rely = 0.25+k , width=70, height=35)
        showup.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[2] ,anchor="w" )

        showup1 = Label(admin) ### name
        showup1.place(relx=0.132, rely = 0.25+k , width=200, height=35)
        showup1.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[1] ,anchor="w" )

        if len(row[4]) >= 25 :
            showup2 = Label(admin) #school
            showup2.place(relx=0.297, rely=0.25+k, width=215, height=35)
            showup2.configure(font="-family {TH Niramit AS} -size 17", fg="#474747", bg="#ffffff" ,  text = row[4] ,anchor="w" )
        
        else :
            showup2 = Label(admin) #school
            showup2.place(relx=0.295, rely=0.25+k, width=215, height=35)
            showup2.configure(font="-family {TH Niramit AS} -size 15", fg="#474747", bg="#ffffff" ,  text = row[4] ,anchor="w" )

        showup3 = Label(admin) ### seat
        showup3.place(relx=0.477, rely = 0.25+k , width=50, height=35)
        showup3.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[7] ,anchor="center" )

        showup4 = Label(admin) ### room
        showup4.place(relx=0.55, rely = 0.25+k , width = 70, height=35)
        showup4.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[6] ,anchor="center" )

        showup5 = Label(admin) ### roomnum
        showup5.place(relx=0.643, rely = 0.25+k , width = 50, height=35)
        showup5.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[5] ,anchor="center" )

        showup6 = Label(admin) ### building
        showup6.place(relx=0.719, rely = 0.25+k , width = 50, height=35)
        showup6.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[8] ,anchor="center" )

        if len(row[9]) >= 12 :    
            showup7 = Label(admin) ### program
            showup7.place(relx=0.787, rely = 0.25+k , width = 200, height=35)
            showup7.configure(font="-family {TH Niramit AS} -size 15", fg="#474747", bg="#ffffff" , text= row[9] ,anchor="center" )
        else :
            showup7 = Label(admin) ### program
            showup7.place(relx=0.719, rely = 0.25+k , width = 50, height=35)
            showup7.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[9] ,anchor="center" )

        k += 0.05 #line break
        
    admin.mainloop()

def showm4 (Event=None) :
    root.geometry("1280x720")
    root.title("ADMIN STUDENT ENROLLMENT SYSTEM")
    root.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))
    global img

    label1 = Label(admin)
    label1.place(relx=0.005, rely=0, width=1280, height=720)
    img = PhotoImage(file=r"C:\Users\Admin\Desktop\project/pics/showm4.png")
    label1.configure(image= img)

    button3 = Button(admin)
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
    
    #text_font = ("DB Helvethaica X Med Cond", "27")
    text_font = ("TH Niramit AS", "17")

    with sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db") as db:
        cur = db.cursor()

    connect = sqlite3.connect(r"C:\Users\Admin\Desktop\project\pics\enrollment.db")
    print('Connected to database successfully.')
    
    cur = connect.cursor()
    cur.execute("select * from HSprint  ")
    rows = cur.fetchall()
    k = 0
    for row in rows :
        print (row[2],row[1],row[4],row[7],row[6],row[5],row[8],row[9],end= "  ")
        showup = Label(admin) ### regisnum
        showup.place(relx=0.07, rely = 0.25+k , width=70, height=35)
        showup.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[2] ,anchor="w" )

        showup1 = Label(admin) ### name
        showup1.place(relx=0.130, rely = 0.25+k , width=200, height=35)
        showup1.configure(font="-family {TH Niramit AS} -size 15", fg="#474747", bg="#ffffff" , text= row[1] ,anchor="w" )

        if len(row[4]) >= 25 :
            showup2 = Label(admin) #school
            showup2.place(relx=0.297, rely=0.25+k, width=215, height=35)
            showup2.configure(font="-family {TH Niramit AS} -size 14", fg="#474747", bg="#ffffff" ,  text = row[4] ,anchor="w" )
        
        else :
            showup2 = Label(admin) #school
            showup2.place(relx=0.295, rely=0.25+k, width=215, height=35)
            showup2.configure(font="-family {TH Niramit AS} -size 17", fg="#474747", bg="#ffffff" ,  text = row[4] ,anchor="w" )

        showup3 = Label(admin) ### seat
        showup3.place(relx=0.477, rely = 0.25+k , width=50, height=35)
        showup3.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[7] ,anchor="center" )

        showup4 = Label(admin) ### room
        showup4.place(relx=0.55, rely = 0.25+k , width = 70, height=35)
        showup4.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[6] ,anchor="center" )

        showup5 = Label(admin) ### roomnum
        showup5.place(relx=0.643, rely = 0.25+k , width = 50, height=35)
        showup5.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[5] ,anchor="center" )

        showup6 = Label(admin) ### building
        showup6.place(relx=0.719, rely = 0.25+k , width = 50, height=35)
        showup6.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[8] ,anchor="center" )

        if len(row[9]) >= 12 :    
            showup7 = Label(admin) ### program
            showup7.place(relx=0.787, rely = 0.25+k , width = 200, height=35)
            showup7.configure(font="-family {TH Niramit AS} -size 15", fg="#474747", bg="#ffffff" , text= row[9] ,anchor="center" )
        else :
            showup7 = Label(admin) ### program
            showup7.place(relx=0.719, rely = 0.25+k , width = 50, height=35)
            showup7.configure(font = text_font, fg="#474747", bg="#ffffff" , text= row[9] ,anchor="center" )


        k += 0.05 #line break
        
    admin.mainloop()

def moreopen () : #back to page 1
    global page2
    page1.entry1.delete(0, END)
    page1.entry2.delete(0, END)
    logout()
    admin.mainloop()



##########################################
page1 = login_page(root)              ####
root.bind("<Return>", login)          ####
root.mainloop()                       ####
##########################################