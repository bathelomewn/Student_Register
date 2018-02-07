#------------------------inported the libr--------------------------------------------
from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import *
import time;
import sqlite3
import datetime

# ---------------------------------the name of the component and the name of the app itself-------------------------
root = Tk()
root.title(" ITE446 Attendance Register")
root.geometry('1350x650+0+0')
root.configure(background='blue')
db_name = 'Register.db'
# -----------------------------------MyFrame (two frames: right and left)---------------------------------------------

LeftMayFrame = Frame(root, width=1000, height=650, bd=8, relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame = Frame(root, width=350, height=650, bd=8, relief="raise")
RightMayFrame.pack(side=RIGHT)

# -------------------------------------divide the frame left to up and down and frame right to up and down--------------

LeftMayFrame1 = Frame(LeftMayFrame, width=1000, height=100, bd=8, relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2 = Frame(LeftMayFrame, width=1000, height=550, bd=8, relief="raise")
LeftMayFrame2.pack(side=TOP)

RightMayFrame1 = Frame(RightMayFrame, width=350, height=215, bd=8, relief="raise")
RightMayFrame1.pack(side=TOP)
RightMayFrame2 = Frame(RightMayFrame, width=350, height=415, bd=8, relief="raise")
RightMayFrame2.pack(side=TOP)

# ------------------------------------Canvas-----------------------------


"""cont1 = Canvas(RightMayFrame2, width=350, height = 425, bg="black")
cont1.grid(row=0,column=0)
image5 = PhotoImage(file="school.png")
cont1.create_image(200,200, image =image5)

#------------------------------------Image-----------------------------

cont = Canvas(RightMayFrame1, width=350, height = 215)
cont.grid(row=0,column=0)
image1 = PhotoImage(file="image1.png")
image=cont.create_image(200,200, image =image1)

def pic1():
    image=cont.create_image(200,200, image =image1)

image2 = PhotoImage(file="image2.png")

def pic2():
    image=cont.create_image(200,200, image =image2)

image3 = PhotoImage(file="image3.png")

def pic3():
    image=cont.create_image(200,200, image =image3)

image4 = PhotoImage(file="image4.png")

def pic4():
    image=cont.create_image(200,200, image =image4)

image5 = PhotoImage(file="image5.png")


def pic5():
    image=cont.create_image(200,200, image =image5)

image6 = PhotoImage(file="image6.png")

def pic6():
    image=cont.create_image(200,200, image =image6)

image7 = PhotoImage(file="image7.png")

def pic7():
    image=cont.create_image(200,200, image =image7)

image8 = PhotoImage(file="image8.png")

def pic8():
    image=cont.create_image(200,200, image =image8)

image9 = PhotoImage(file="image9.png")

def pic9():
    image=cont.create_image(200,200, image =image9)

image10 = PhotoImage(file="image10.png")

def pic10():
    image=cont.create_image(200,200, image =image10)

image11 = PhotoImage(file="image11.png")

def pic11():
    image=cont.create_image(200,200, image =image11)

image12 = PhotoImage(file="image12.png")

def pic12():
    image=cont.create_image(200,200, image =image12)

image13 = PhotoImage(file="image13.png")"""

# --------------------------------------------------------------------variable----------------------------------------------------------------------------------------------
DateofOrder = StringVar()
value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11 = StringVar()
value12 = StringVar()


def run_query(self, query, parameters=()):
    with sqlite3.connect(self.db_name) as conn:
        cursor = conn.cursor()
        query_result = cursor.execute(query, parameters)
        conn.commit()
    return query_result


def Mark_Register():
    conn = sqlite3.connect("Register.db");
    cursor = conn.cursor();
    cursor.execute("update student set attendncestatus = ? where studentnumber = 1233", "P")
    conn.commit()

    #
    #
    #
    #
    # if value0.get() == "P":
    #     value0.set("P")
    #     value1.set("P")
    #
    #     value2.set("P")
    #     value3.set("P")
    #     value4.set("P")
    #     value5.set("P")
    #     value6.set("P")
    #     value7.set("P")
    #     value8.set("P")
    #     value9.set("p")
    #     value10.set("P")
    #     value11.set("P")
    #     value12.set("P")
    # elif(value0.get() == "0"):
    #     value1.set("0")
    #     value2.set("0")
    #     value3.set("0")
    #     value4.set("0")
    #     value5.set("0")
    #     value6.set("0")
    #     value7.set("0")
    #     value8.set("0")
    #     value9.set("0")
    #     value10.set("0")
    #     value11.set("0")
    #     value12.set("0")
    # elif (value0.get() == "E"):
    #     value1.set("E")
    #     value2.set("E")
    #     value3.set("E")
    #     value4.set("E")
    #     value5.set("E")
    #     value6.set("E")
    #     value7.set("E")
    #     value8.set("E")
    #     value9.set("E")
    #     value10.set("E")
    #     value11.set("E")
    #     value12.set("E")
    # elif (value0.get() == "A"):
    #     value1.set("A")
    #     value2.set("A")
    #     value3.set("A")
    #     value4.set("A")
    #     value5.set("A")
    #     value6.set("A")
    #     value7.set("A")
    #     value8.set("A")
    #     value9.set("A")
    #     value10.set("A")
    #     value11.set("A")
    #     value12.set("A")
    # elif (value0.get() == "L"):
    #     value1.set("L")
    #     value2.set("L")
    #     value3.set("L")
    #     value4.set("L")
    #     value5.set("L")
    #     value6.set("L")
    #     value7.set("L")
    #     value8.set("L")
    #     value9.set("L")
    #     value10.set("L")
    #     value11.set("L")
    #     value12.set("L")
    # elif (value0.get() == " "):
    #     value1.set(" ")
    #     value2.set(" ")
    #     value3.set(" ")
    #     value4.set(" ")
    #     value5.set(" ")
    #     value6.set(" ")
    #     value7.set(" ")
    #     value8.set(" ")
    #     value9.set(" ")
    #     value10.set(" ")
    #     value11.set(" ")
    #     value12.set(" ")


def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12.set("")


def qExit():
    qExit= messagebox.askyesno("Exit System", "Do You want to quit?")
    if qExit > 0:
        root.destroy()
        return


# -------------------------------------------Componets------------------------------

DateofOrder.set(time.strftime("%d/%m/%Y"))

# ----------------------------------------component for the top  LeftMayFrame1---------------------------------------

lblNo = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="NO.", bd=16)
lblNo.grid(row=0, column=0, sticky=W)

lblStudentNo = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Student No.", bd=16)
lblStudentNo.grid(row=0, column=1, sticky=W)
lblStudentName = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Student Name.", bd=16)
lblStudentName.grid(row=0, column=2, sticky=W)
lblCourseCode = Label(LeftMayFrame1, font=('arial', 10, 'bold'), text="Course code.", bd=16)
lblCourseCode.grid(row=0, column=3, sticky=W)


box = ttk.Combobox(LeftMayFrame1, textvariable=value0, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=0, column=4)
DateofOrder.set(time.strftime("%d/%m/%y"))


btnSubmit = Button(LeftMayFrame1, text='Submit', padx=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1, command=Mark_Register).grid(row=0, column=5)

btnFill = Button(LeftMayFrame1, text='Fill', padx=2, bd=2, fg="black",

                  font=('arial', 10, 'bold'), width=12, height=1, command=Mark_Register).grid(row=0, column=5)

btnReset = Button(LeftMayFrame1, text='Reset', padx=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1, command=Reset).grid(row=0, column=6)

btnExit = Button(LeftMayFrame1, text='Exit', padx=2, bd=2, fg="black",
                 font=('arial', 10, 'bold'), width=12, height=1, command=qExit).grid(row=0, column=7)

lblDateofOrder = Label(LeftMayFrame1, font=('arial', 10, 'bold'), textvariable=DateofOrder, padx=2,
                       pady=2, bd=2, fg="black", bg='white', relief='sunken')
lblDateofOrder.grid(row=0, column=8, sticky=W)

# ------------------------------------------------------ LeftMayFrame1--------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="1", bd=16)
lblNo.grid(row=0, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1232', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=0, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Bathelomew Jack', padx=2,
                        pady=2, bd=2, fg="black", width=13)
lblstudent_Name.grid(row=0, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=0, column=3, sticky=W)

# -------------------------------------------------------------Combobox-----------------------------------------------------------------------------------------
box = ttk.Combobox(LeftMayFrame2, textvariable=value1, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E') #----the attribute inside the Combobox-------
box.current(0)
box.grid(row=0, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=0, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=0, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=0, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=0, column=8)

# ------------------------------------------- LeftMayFrame2 row2-----------------------------------------------------------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="2", bd=16)
lblNo.grid(row=1, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1233', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=1, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Kingsly Mark', padx=2,
                        pady=2, bd=2, fg="black", width=13)
lblstudent_Name.grid(row=1, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=1, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value2, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=1, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=1, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=1, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=1, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=1, column=8)

# ------------------------------------------- LeftMayFrame2 row3-----------------------------------------------------------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="3", bd=16)
lblNo.grid(row=2, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1234', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=2, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Sarayut Jasmine', padx=2,
                        pady=2, bd=2, fg="black", width=13)
lblstudent_Name.grid(row=2, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=2, column=3, sticky=W)

# -----------------------------------------Combobox--------------------------------------------------------
box = ttk.Combobox(LeftMayFrame2, textvariable=value3, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=2, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=2, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=2, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=2, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=2, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="4", bd=16)
lblNo.grid(row=3, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1235', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=3, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Rose Kelly', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=3, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=3, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value4, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=3, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=3, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=3, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=3, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=3, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="5", bd=16)
lblNo.grid(row=4, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1236', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=4, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Kingsly Mark', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=4, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=4, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value5, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=4, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=4, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=4, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=4, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=4, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="6", bd=16)
lblNo.grid(row=5, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1237', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=5, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Kevin Nice', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=5, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=5, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value6, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=5, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=5, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=5, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=5, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=5, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="7", bd=16)
lblNo.grid(row=6, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1238', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=6, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Anthony Mark', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=6, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=6, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value7, state='readonly')
box['values'] = (' ', 'E', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=6, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=6, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=6, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=6, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=6, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="8", bd=16)
lblNo.grid(row=7, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1239', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=7, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Charles Obi', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=7, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=7, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value8, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=7, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=7, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=7, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=7, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=7, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="9", bd=16)
lblNo.grid(row=8, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1240', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=8, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Joy Saint', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=8, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=8, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value9, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=8, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=8, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=8, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=8, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=8, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="10", bd=16)
lblNo.grid(row=9, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1241', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=9, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Power Mark', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=9, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=9, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value10, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=9, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=9, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=9, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=9, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=9, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="11", bd=16)
lblNo.grid(row=10, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1242', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=10, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='John Kennedy', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=10, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=10, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value11, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=10, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=10, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=10, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=10, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=10, column=8)

# --------------------------------------------

lblNo = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text="12", bd=16)
lblNo.grid(row=11, column=0, sticky=W)

lblstudent_No_1 = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='1243', padx=2,
                        pady=2, bd=2, fg="black", width=18)
lblstudent_No_1.grid(row=11, column=1, sticky=W)
lblstudent_Name = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='Kingsly Mark', padx=2,
                        pady=2, bd=2, fg="black", width=12)
lblstudent_Name.grid(row=11, column=2, sticky=W)
lblCourse_Code = Label(LeftMayFrame2, font=('arial', 10, 'bold'), text='ITE446', padx=2,
                       pady=2, bd=2, fg="black", width=12)
lblCourse_Code.grid(row=11, column=3, sticky=W)

box = ttk.Combobox(LeftMayFrame2, textvariable=value12, state='readonly')
box['values'] = (' ', 'P', 'L', '0', 'A', 'E')
box.current(0)
box.grid(row=11, column=4)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=12, height=1).grid(row=11, column=5)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=11, column=6)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=11, column=7)

btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=11, column=8)

#-------------------------------------------Submit Bottun---------------------------------------------------------------------


btnSpace = Button(LeftMayFrame2, text='', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 10, 'bold'), width=11, height=1).grid(row=11, column=8)


root.mainloop()







