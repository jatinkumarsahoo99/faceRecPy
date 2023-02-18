from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        # ============== variables================

        # ============variables=================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

    # 1st
        img = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img3.webp")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=0, y=0, width=500, height=130)

# 2nd
        img2 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img3.webp")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoImage2)
        f_lbl.place(x=500, y=0, width=500, height=130)

# 3rd
        img3 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img3.webp")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoImage3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoImage3)
        f_lbl.place(x=1000, y=0, width=500, height=130)


# bg img
        img4 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img7.jpg")
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoImage4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoImage4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Student Management System", font=(
            "time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # left Label frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("time new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img_left = img_left.resize((720, 100), Image.ANTIALIAS)
        self.photoImage_img_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoImage_img_left)
        f_lbl.place(x=5, y=0, width=720, height=100)

# current course
        current_course = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                    text="Current course information", font=("time new roman", 12, "bold"))
        current_course.place(x=5, y=100, width=720, height=110)

# Depart ment

        deep_label = Label(current_course, text="Department", font=(
            "time new roman", 12, "bold"), bg="white")
        deep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course, textvariable=self.var_dep, font=(
            "time new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department",
                               "Computer", "IT", "CSE", "CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)
# course

        course_label = Label(current_course, text="Course", font=(
            "time new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course, textvariable=self.var_course, font=(
            "time new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

# year

        year_label = Label(current_course, text="Year", font=(
            "time new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course, textvariable=self.var_year, font=(
            "time new roman", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21",
                                "2021-22", "2022-23", "2323-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

     # semester

        semester_label = Label(current_course, text="Semester", font=(
            "time new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course, textvariable=self.var_semester, font=(
            "time new roman", 12, "bold"), state="readonly", width=20)
        semester_combo["values"] = (
            "Select Semester", "Semester - 1", "Semester - 2", "Semester - 3", "Semester - 4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


# class student information

        class_student = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                   text="Class student information", font=("time new roman", 12, "bold"))
        class_student.place(x=5, y=200, width=720, height=350)

# student id
        studentId_label = Label(class_student, text="StudentID:", font=(
            "time new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry = ttk.Entry(
            class_student, textvariable=self.var_std_id, width=20, font=("time new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)


# student name
        studentName_label = Label(class_student, text="Student Name:", font=(
            "time new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)

        studentName_entry = ttk.Entry(
            class_student, textvariable=self.var_std_name, width=20, font=("time new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # class division
        classDivision_label = Label(class_student, text="Class Division:", font=(
            "time new roman", 13, "bold"), bg="white")
        classDivision_label.grid(row=1, column=0, padx=10, sticky=W)

        classDivision_entry = ttk.Entry(
            class_student, textvariable=self.var_div, width=20, font=("time new roman", 13, "bold"))
        classDivision_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Roll No
        rollo_label = Label(class_student, text="Roll No:", font=(
            "time new roman", 13, "bold"), bg="white")
        rollo_label.grid(row=1, column=2, padx=10, sticky=W)

        roll_entry = ttk.Entry(class_student, textvariable=self.var_roll, width=20, font=(
            "time new roman", 13, "bold"))
        roll_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Gender
        gender_label = Label(class_student, text="Gender:", font=(
            "time new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_entry = ttk.Entry(class_student, textvariable=self.var_gender, width=20, font=(
            "time new roman", 13, "bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # DOB
        dob_label = Label(class_student, text="DOB:", font=(
            "time new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, sticky=W)

        dob_entry = ttk.Entry(class_student, textvariable=self.var_dob, width=20, font=(
            "time new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Email
        email_label = Label(class_student, text="Email:", font=(
            "time new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, sticky=W)

        email_entry = ttk.Entry(class_student, textvariable=self.var_email, width=20, font=(
            "time new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Phone no
        phone_label = Label(class_student, text="Phone No:", font=(
            "time new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, sticky=W)

        phone_entry = ttk.Entry(class_student, textvariable=self.var_phone, width=20, font=(
            "time new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        # Address
        address_label = Label(class_student, text="Address:", font=(
            "time new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, sticky=W)

        address_entry = ttk.Entry(class_student, textvariable=self.var_address, width=20, font=(
            "time new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # Teacher Name
        teacher_label = Label(class_student, text="Teacher:", font=(
            "time new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, sticky=W)

        teacher_entry = ttk.Entry(class_student, textvariable=self.var_teacher, width=20, font=(
            "time new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=10, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()

        radionButton1 = ttk.Radiobutton(
            class_student, variable=self.var_radio1, text="take a photo sample", value="Yes")
        radionButton1.grid(row=5, column=0)

        self.var_radio2 = StringVar()
        radionButton2 = ttk.Radiobutton(
            class_student, variable=self.var_radio1, text="No photo sample", value="No")
        radionButton2.grid(row=5, column=1)

        # buttons frame

        btn_frame = Frame(class_student, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=710, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.addData, width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.updateFunction, width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.deleteData, width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.resetData, width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=280, width=710, height=35)

        takeaphoto_btn = Button(btn_frame1, text="Take a Photo Sample",command=self.genearateDataSet, width=35, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        takeaphoto_btn.grid(row=0, column=0)

        updatephotosample_btn = Button(btn_frame1, text="Update photo sample", width=35, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        updatephotosample_btn.grid(row=0, column=2)

        # Right Label frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("time new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(
            r"E:\faceRecognitionSystem\imagesFiles\img4.jpeg")
        img_right = img_right.resize((720, 100), Image.ANTIALIAS)
        self.photoImage_img_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoImage_img_right)
        f_lbl.place(x=5, y=0, width=720, height=100)


# search system

        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("time new roman", 12, "bold"))
        search_frame.place(x=5, y=150, width=700, height=70)

      # search Name
        search_label = Label(search_frame, text="Search By:", font=(
            "time new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=1, padx=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "time new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=14, font=("time new roman", 13, "bold"))
        search_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        search_btn = Button(search_frame, text="Search", width=10, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=4)

        showAll_btn = Button(search_frame, text="Dhow All", width=10, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=5)

# table frame
        table_frame1 = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame1.place(x=5, y=210, width=700, height=350)

        scroll_x = ttk.Scrollbar(table_frame1, orient=HORIZONTAL)
        scroll_Y = ttk.Scrollbar(table_frame1, orient=VERTICAL)

        self.student_tble = ttk.Treeview(table_frame1, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "gender", "phone", "address", "teacher", "photo"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_Y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_Y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_tble.xview)
        scroll_Y.config(command=self.student_tble.yview)

        self.student_tble.heading("dep", text="Department")
        self.student_tble.heading("course", text="Course")
        self.student_tble.heading("year", text="Year")
        self.student_tble.heading("sem", text="Semester")
        self.student_tble.heading("id", text="StudentId")
        self.student_tble.heading("name", text="Name")
        self.student_tble.heading("div", text="Division")
        self.student_tble.heading("dob", text="DOB")
        self.student_tble.heading("email", text="Email")
        self.student_tble.heading("phone", text="Phone")
        self.student_tble.heading("address", text="Address")
        self.student_tble.heading("teacher", text="Teacher")
        self.student_tble.heading("photo", text="PhotoSampleStatus")

        self.student_tble.column("dep", width=100)
        self.student_tble.column("course", width=100)
        self.student_tble.column("year", width=100)
        self.student_tble.column("sem", width=100)
        self.student_tble.column("id", width=100)
        self.student_tble.column("name", width=100)
        self.student_tble.column("dob", width=100)
        self.student_tble.column("email", width=100)
        self.student_tble.column("phone", width=100)
        self.student_tble.column("address", width=100)
        self.student_tble.column("teacher", width=100)
        self.student_tble.column("photo", width=100)

        self.student_tble['show'] = "headings"

        self.student_tble.pack(fill=BOTH, expand=1)
        self.student_tble.bind("<ButtonRelease>", self.getCursor)
        self.fetchData()

      # ================== function declaration
    def addData(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                # messagebox.showinfo("Success","welcome to our world")
                # conn = mysql.connection()
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="password", database="faceRecognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", ( self.var_dep.get(), self.var_course .get(), self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(), self.var_roll.get(),self.var_gender.get(), self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get() ))
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("success","Student details hase been added successfully",parent=self.root)
            except Exception  as es:
                messagebox.showerror("error",f"Error while adding student details{es}",parent=self.root)


    # ===============fetch data
    def fetchData(self):
         conn = mysql.connector.connect( host="localhost", user="root", password="password", database="faceRecognizer")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from student")
         data = my_cursor.fetchall()

         if len(data) != 0:
                self.student_tble.delete(*self.student_tble.get_children())
                for i in data:
                        self.student_tble.insert('', END, values=i)
                conn.commit()
         conn.close()                
     # ==================get cursor
    def getCursor(self,event=""):
        cursor_focus=self.student_tble.focus()
        content=self.student_tble.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course. set (data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher. set (data[13]),
        self.var_radio1.set(data[14])


    def updateFunction(self): 
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                 messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                # messagebox.showinfo("Success","welcome to our world")
                # conn = mysql.connection()
                Update = messagebox.askyesno("Update","Do you want to update this",parent=self.root)

                if Update > 0:
                        conn = mysql.connector.connect(
                    host="localhost", user="root", password="password", database="faceRecognizer")
                        my_cursor = conn.cursor()
                        my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                              self.var_dep.get(), self.var_course .get(), self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(), self.var_roll.get(),self.var_gender.get(), self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get()))
                else:
                    if not Update:
                        return;

                messagebox.showinfo("success","Updated successfully")  
                conn.commit()
                self.fetchData()
                conn.close()      

            except Exception  as es:
                messagebox.showerror("error",f"Error while adding student details{es}",parent=self.root)    


    def deleteData(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete >0:
                    conn = mysql.connector.connect(
                    host="localhost", user="root", password="password", database="faceRecognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return   
                conn.commit()
                self.fetchData()
                conn.close()    
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)     



            except Exception  as es:
                 messagebox.showerror("error",f"Error while adding student details{es}",parent=self.root) 


    def resetData(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")        

    # generate a data set or take photo sample
    def genearateDataSet(self):
          if self.var_std_id.get() == "":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
          else:
              try:
                 conn = mysql.connector.connect(
                 host="localhost", user="root", password="password", database="faceRecognizer")
                 my_cursor = conn.cursor()
                 my_cursor.execute("select * from student")
                 myresult = my_cursor.fetchall()
                 id = 0
                 for x in myresult:
                     id+=1
                 my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                              self.var_dep.get(), self.var_course .get(), self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_div.get(), self.var_roll.get(),self.var_gender.get(), self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get() == id+1 ))    

                 conn.commit()
                 self.fetchData()
                 conn.close() 

                 # ================ Load predefined data on face frontals from opencv  ===========
                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                 def face_cropped(img):
                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=face_classifier.detectMultiScale(gray,1.3,5)
                     #scaling factor =1.3
                     #Minimum Neighbor =5

                     for (x,y,w,h) in faces:
                         face_cropped = img[y:y+h,x:x+w]
                         return face_cropped

                 cap=cv2.VideoCapture(0)  
                 img_id=0

                 while True:
                     ret,my_frame=cap.read()
                     if  face_cropped(my_frame) is not None:
                         img_id+=1
                         face=cv2.resize(face_cropped(my_frame),(450,450))
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)      
                         file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("Crooped Face",face)

                     if cv2.waitKey(1) == 13 or int(img_id) == 100:
                         break


                 cap.release()
                 cv2.destroyAllWindows()
                 messagebox.showinfo("Result","Generating data sets completed")      

              except Exception  as es:
                 messagebox.showerror("error",f"Error while adding student details{es}",parent=self.root)       
                  



if __name__ == "__main__":
    root = Tk()
    object = Student(root)
    root.mainloop()
