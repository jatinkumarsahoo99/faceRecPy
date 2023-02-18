from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        title_lbl = Label(self.root, text="Train Data Set", font=(
            "time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)


            # 1st
        img = Image.open(r"imagesFiles\img3.webp")
        img = img.resize((1530, 325), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=0, y=55, width=1530, height=325)

# 2nd
        img2 = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img3.webp")
        img2 = img2.resize((1530, 325), Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoImage2)
        f_lbl.place(x=0, y=440, width=1530, height=325)

        b1_1=Button (self.root, text="Train Data",command=self.train_classifier, cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0, y=380,width=1530,height=40)

    def train_classifier (self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image). convert('L') #Gray scale image
            imageNp=np.array(img, 'uint8')
            id=int (os.path.split(image) [1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids=np.array(ids)
        # ============ Train the classifier And save===============

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, np.array(ids))
        clf.save("faceRecognitionSystem.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")
        


if __name__ == "__main__":
    root = Tk()
    object = Train(root)
    root.mainloop()        