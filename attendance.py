from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

            # 1st
        img = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img7.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=0, y=0, width=800, height=200)

# 2nd
        img2 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img7.jpg")
        img2 = img2.resize((800, 200), Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoImage2)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # bg img
        img4 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img6.png")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoImage4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoImage4)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="Attendance Management System", font=(
            "time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # left Label frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Attendance Details", font=("time new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img5.jpg")
        img_left = img_left.resize((720, 100), Image.ANTIALIAS)
        self.photoImage_img_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoImage_img_left)
        f_lbl.place(x=5, y=0, width=720, height=100)

        insideleftframe = Frame(left_frame, bd=2, relief=RIDGE,bg="white")
        insideleftframe.place(x=0, y=135, width=710, height=350)

        #Label entry
        # Attendance id
        attendanceId = Label(insideleftframe, text="Attendance Id:", font=(
            "time new roman", 13, "bold"), bg="white")
        attendanceId.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(
            insideleftframe,  width=20, font=("time new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        # student roll
        rollLabel = Label(insideleftframe, text="Roll:", font=(
            "time new roman", 13, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=4,pady=8, sticky=W)

        roll_entry = ttk.Entry(
            insideleftframe, width=20, font=("time new roman", 13, "bold"))
        roll_entry.grid(row=0, column=3, pady=8, sticky=W)

        # name
        name_label = Label(insideleftframe, text="Name:", font=(
            "time new roman", 13, "bold"), bg="white")
        name_label.grid(row=1, column=0)

        name_entry = ttk.Entry(
            insideleftframe, width=20, font=("time new roman", 13, "bold"))
        name_entry.grid(row=1, column=1, pady=8, sticky=W)

        # department
        departMent_label = Label(insideleftframe, text="DepartMent:", font=(
            "time new roman", 13, "bold"), bg="white")
        departMent_label.grid(row=1, column=2, sticky=W)

        department_entry = ttk.Entry(insideleftframe, width=20, font=(
            "time new roman", 13, "bold"))
        department_entry.grid(row=1, column=3, pady=8,sticky=W)

        # time
        time_label = Label(insideleftframe, text="Time:", font=(
            "time new roman", 13, "bold"), bg="white")
        time_label.grid(row=2, column=0, pady=8)

        time_entry = ttk.Entry(insideleftframe, width=20, font=(
            "time new roman", 13, "bold"))
        time_entry.grid(row=2, column=1)

        # date2
        date_label2 = Label(insideleftframe, text="Date:", font=(
            "time new roman", 13, "bold"), bg="white")
        date_label2.grid(row=2, column=2, pady=8)

        date_entry2 = ttk.Entry(insideleftframe,  width=20, font=(
            "time new roman", 13, "bold"))
        date_entry2.grid(row=2, column=3)

        # Attendance
        attendance_label = Label(insideleftframe, text="Attendance:", font=(
            "time new roman", 13, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, pady=8, sticky=W)


        self.atten_status=ttk.Combobox(insideleftframe, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)



        btn_frame = Frame(insideleftframe, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=710, height=35)

        save_btn = Button(btn_frame, text="Import CSV", width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV", width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)





                # Right Label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance Details", font=("time new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=580)


        
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=5, width=700, height=455)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable = ttk.Treeview(table_frame,columns=("Id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("Id",text="Attendance Id")
        self.attendanceReportTable.heading("roll",text="Roll")
        self.attendanceReportTable.heading("name",text="Name")
        self.attendanceReportTable.heading("department",text="Department")
        self.attendanceReportTable.heading("time",text="Time")
        self.attendanceReportTable.heading("date",text="Date")
        self.attendanceReportTable.heading("attendance",text="Attendance")

        self.attendanceReportTable['show'] = "headings"

        self.attendanceReportTable.column("Id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)


        self.attendanceReportTable.pack(fill=BOTH,expand=1)















        




if __name__ == "__main__":
    root = Tk()
    object = Attendance(root)
    root.mainloop()        