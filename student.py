from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")



    # 1st 
        img = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img3.webp")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoImage)
        f_lbl.place(x=0,y=0,width=500,height=130)

# 2nd
        img2 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img3.webp")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)


        f_lbl = Label(self.root,image=self.photoImage2)
        f_lbl.place(x=500,y=0,width=500,height=130)

# 3rd
        img3 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img3.webp")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoImage3 = ImageTk.PhotoImage(img3)


        f_lbl = Label(self.root,image=self.photoImage3)
        f_lbl.place(x=1000,y=0,width=500,height=130)
    

# bg img
        img4 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img7.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoImage4 = ImageTk.PhotoImage(img4)


        bg_img = Label(self.root,image=self.photoImage4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="Student Management System",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame (bg_img, bd=2,bg="white")
        main_frame.place(x=20, y=55,width=1480,height=600)

        # left Label frame


        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief = RIDGE,text="Student Details",font=("time new roman",12,"bold") )
        left_frame.place(x=10,y=10,width=730,height=580)


        img_left = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img_left=img_left.resize((720,100),Image.ANTIALIAS)
        self.photoImage_img_left = ImageTk.PhotoImage(img_left)


        f_lbl = Label(left_frame,image=self.photoImage_img_left)
        f_lbl.place(x=5,y=0,width=720,height=100)

#current course
        current_course = LabelFrame(left_frame,bd=2,bg="white",relief = RIDGE,text="Current course information",font=("time new roman",12,"bold") )
        current_course.place(x=5,y=100,width=720,height=110)

#Depart ment

        deep_label = Label(current_course,text="Department",font=("time new roman",12,"bold"),bg="white")
        deep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course,font=("time new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"] = ("Select Department", "Computer", "IT","CSE","CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
# course

        course_label = Label(current_course,text="Course",font=("time new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course,font=("time new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"] = ("Select Course", "FE", "SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

# year

        year_label = Label(current_course,text="Year",font=("time new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course,font=("time new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22","2022-23","2323-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

     # semester

        semester_label = Label(current_course,text="Semester",font=("time new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(current_course,font=("time new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"] = ("Select Semester", "Semester - 1", "Semester - 2","Semester - 3","Semester - 4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)   


# class student information

        class_student = LabelFrame(left_frame,bd=2,bg="white",relief = RIDGE,text="Class student information",font=("time new roman",12,"bold") )
        class_student.place(x=5,y=200,width=720,height=350)

#student id
        studentId_label = Label(class_student,text="StudentID:",font=("time new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        studentId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W) 


#student name
        studentName_label = Label(class_student,text="Student Name:",font=("time new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        studentName_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W) 

        #class division
        classDivision_label = Label(class_student,text="Class Division:",font=("time new roman",13,"bold"),bg="white")
        classDivision_label.grid(row=1,column=0,padx=10,sticky=W)

        classDivision_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        classDivision_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #Roll No
        rollo_label = Label(class_student,text="Roll No:",font=("time new roman",13,"bold"),bg="white")
        rollo_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        roll_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)


        #Gender
        gender_label = Label(class_student,text="Gender:",font=("time new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        gender_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        gender_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        #DOB
        dob_label = Label(class_student,text="DOB:",font=("time new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        dob_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Email
        email_label = Label(class_student,text="Email:",font=("time new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)


        #Phone no
        phone_label = Label(class_student,text="Phone No:",font=("time new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,sticky=W)

        phone_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        phone_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)


        
        #Address
        address_label = Label(class_student,text="Address:",font=("time new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,sticky=W)

        address_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        address_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)


         #Teacher Name
        teacher_label = Label(class_student,text="Teacher:",font=("time new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry = ttk.Entry(class_student,width=20,font=("time new roman",13,"bold")) 
        teacher_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)


        # radio buttons

        radionButton1 = ttk.Radiobutton(class_student,text="take a photo sample",value="Yes")
        radionButton1.grid(row=5,column=0)

        radionButton2 = ttk.Radiobutton(class_student,text="No photo sample",value="No")
        radionButton2.grid(row=5,column=1)


        # buttons frame

        btn_frame = Frame(class_student,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=710,height=35)

        save_btn = Button(btn_frame,text="Save",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",width=17,font=("time new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(class_student,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=280,width=710,height=35)

        takeaphoto_btn = Button(btn_frame1,text="Take a Photo Sample",width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        takeaphoto_btn.grid(row=0,column=0)

        updatephotosample_btn = Button(btn_frame1,text="Update photo sample",width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        updatephotosample_btn.grid(row=0,column=2)


         # Right Label frame


        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief = RIDGE,text="Student Details",font=("time new roman",12,"bold") )
        right_frame.place(x=750,y=10,width=720,height=580)


        img_right = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img4.jpeg")
        img_right=img_right.resize((720,100),Image.ANTIALIAS)
        self.photoImage_img_right = ImageTk.PhotoImage(img_right)


        f_lbl = Label(right_frame,image=self.photoImage_img_right)
        f_lbl.place(x=5,y=0,width=720,height=100)


# search system

        search_frame = LabelFrame(main_frame,bd=2,bg="white",relief = RIDGE,text="Student Details",font=("time new roman",12,"bold") )
        search_frame.place(x=750,y=10,width=720,height=580)



























if __name__ == "__main__":
    root = Tk()
    object = Student(root)
    root.mainloop()        