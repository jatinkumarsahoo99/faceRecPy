from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class FaceRecognitionSystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        img = Image.open(r"E:\faceRecognitionSystem\imagesFiles\img3.webp")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root,image=self.photoImage)
        f_lbl.place(x=0,y=0,width=500,height=130)



if __name__ == "__main__":
    root = Tk()
    object = FaceRecognitionSystem(root)
    root.mainloop()