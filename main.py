## main.py ##
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox

##window
main = tk.Tk()
main.geometry("1280x720")
main.title("STUDENT ENROLLMENT SYSTEM")
main.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\school_icon.png"))
main.resizable(0, 0)


def Exit(): 
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy() #close
main.protocol("WM_DELETE_WINDOW", Exit)
#------------------------------------------------------------


def enrolJHS():
    main.withdraw()
    os.system(r"python C:\Users\Admin\Desktop\project\pics\enrolJHS.py")
    #main.deiconify()

def enrolHS():
    main.withdraw()
    os.system(r"python C:\Users\Admin\Desktop\project\pics\enrolHS.py")
    main.deiconify()

def admin():
    main.withdraw()
    os.system(r"python C:\Users\Admin\Desktop\project\pics\admin.py")
    #main.deiconify()


label1 = Label(main) #window graphic
label1.place(relx=0, rely=0, width=1280, height=720)
img = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics/main.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.118, rely=0.6775, width=380, height=148)
button1.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth="0")    #option
img2 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\JHS3.png")
button1.configure(image=img2)
button1.configure(command=enrolJHS)

button2 = Button(main)                                                 
button2.place(relx=0.584, rely=0.6775, width=380, height=148)
button2.configure(relief="flat",overrelief="flat",activebackground="#ffffff",cursor="hand2",foreground="#ffffff",background="#ffffff",borderwidth="0")
img3 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\HS3.png")
button2.configure(image=img3)
button2.configure(command=enrolHS) 

button3 = Button(main)
button3.place(relx=0.95, rely=0.03, width=50, height=50)
button3.configure(cursor="hand2",borderwidth="0")
img4 = PhotoImage(file=r"C:\Users\Admin\Desktop\project\pics\admin_icon.png")
button3.configure(image=img4)
button3.configure(command=admin)

main.mainloop()