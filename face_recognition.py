from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
from time import strftime
from datetime import datetime


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img = Image.open(r"imagesFiles\img5.jpg")
        img = img.resize((650, 700), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_botton = Image.open(r"imagesFiles\img7.jpg")
        img_botton = img_botton.resize((950, 700), Image.ANTIALIAS)
        self.photoImage_button = ImageTk.PhotoImage(img_botton)

        f_lbl_button = Label(self.root, image=self.photoImage_button)
        f_lbl_button.place(x=650, y=55, width=950, height=700)

        b1_1=Button (f_lbl_button, text="Face Recognition",command=self.face_recog, cursor="hand2",font=("time new roman",15,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=350, y=600,width=200,height=40)


    def mark_attendance (self,i,r,n,d):
        with open("attendance.csv","r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now =datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines (f"\n{i},{r}, {n},{d} ,{dtString},{d1},Present")    


        


    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)


            cord = []

            for (x,y,w, h) in features:
                cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0), 3)
                id, predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                 host="localhost", user="root", password="password", database="faceRecognizer")
                my_cursor = conn.cursor()

                # print(str(id)+">>>>>>>>>>>")

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = ( str(n))

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = (str(i))

            
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = (str(r))

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = (str(d))


                if confidence > 77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w, y+h), (0,0,255), 3)
                    cv2.putText(img,"UnKnown Face",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                cord = [x,y,w,y]    
            return cord;
    
        def recognize(img,clf,faceCascade):
            cord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("faceRecognitionSystem.xml")


        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img )


            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

        

     
                

if __name__ == "__main__":
    root = Tk()
    object = FaceRecognition(root)
    root.mainloop()        