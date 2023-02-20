from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance


class FaceRecognitionSystem:
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

        title_lbl = Label(bg_img,text="Face Recognition Attendance System Software",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

# button
        img5 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img5=img5.resize((220,720),Image.ANTIALIAS)
        self.photoImage5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoImage5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button (bg_img, text="Student Details",command=self.student_details, cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=300,width=220,height=40)

# face button
        img6 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img6=img6.resize((220,720),Image.ANTIALIAS)
        self.photoImage6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoImage6,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button (bg_img, text="Face Dector", command=self.faceRecognition,cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=300,width=220,height=40)


# Attendance button
        img7 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img7=img7.resize((220,720),Image.ANTIALIAS)
        self.photoImage7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoImage7,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button (bg_img, text="Attendance",command=self.Attendance, cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=300,width=220,height=40)

# help button
        img8 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img8=img8.resize((220,720),Image.ANTIALIAS)
        self.photoImage8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoImage8,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button (bg_img, text="Help", cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=300,width=220,height=40)


        
# Train button
        img9 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img9=img9.resize((220,720),Image.ANTIALIAS)
        self.photoImage9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoImage9,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button (bg_img, text="Train", command=self.train_data,cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=580,width=220,height=40)


# photo button
        img10 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img10=img10.resize((220,720),Image.ANTIALIAS)
        self.photoImage10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoImage10,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button (bg_img, text="Photos",command=self.openImage, cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500, y=580,width=220,height=40)


# developer button
        img11 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img11=img11.resize((220,720),Image.ANTIALIAS)
        self.photoImage11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoImage11,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button (bg_img, text="Developer", cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800, y=580,width=220,height=40)

# Exist button
        img12 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img2.jpg")
        img12=img12.resize((220,720),Image.ANTIALIAS)
        self.photoImage12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img,image=self.photoImage12,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button (bg_img, text="Exist", cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100, y=580,width=220,height=40)

    
 
    def openImage(self):
        os.startfile("data")



# =============== function butto
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)



    def train_data(self):
        self.new_window =Toplevel(self.root)
        self.app = Train(self.new_window)

    def faceRecognition(self):
        self.new_window =Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def Attendance(self):
        self.new_window =Toplevel(self.root)
        self.app = Attendance(self.new_window)    

if __name__ == "__main__":
    root = Tk()
    object = FaceRecognitionSystem(root)
    root.mainloop()