from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Smart Attendance System")

        img = Image.open("./Resource/Images/prjImage.jpg")
        img = img.resize((1920, 1080))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoImg)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        title_lbl = Label(bg_img, text="SMART ATTENDANCE SYSTEM", font=('times new roman', 30, "bold"), fg="white", bg="skyblue")
        title_lbl.place(x=0, y=50, width=650, height=35)


        #Buttons
        img1 = Image.open("./Resource/Images/prjimg2.jpg")
        img1 = img1.resize((200, 200))
        self.photoImg1 = ImageTk.PhotoImage(img1)
        
        b1 = Button(bg_img, command=self.student_details, image=self.photoImg1, cursor="hand2")
        b1.place(x=100, y=200, width=200, height=200)

        b1_1 = Button(bg_img, command=self.student_details, text="Student Details", cursor="hand2", fg="white", bg="skyblue", font=("times new roman", 16, "bold"))
        b1_1.place(x=100, y=400, width=200, height=25)

        img2 = Image.open("./Resource/Images/prjimg3.png")
        img2 = img2.resize((200, 200))
        self.photoImg2 = ImageTk.PhotoImage(img2)
        
        b2 = Button(bg_img, command=self.face_recog, image=self.photoImg2, cursor="hand2")
        b2.place(x=500, y=200, width=200, height=200)

        b2_1 = Button(bg_img, command=self.face_recog, text="Face Recognition", cursor="hand2", fg="white", bg="skyblue", font=("times new roman", 16, "bold"))
        b2_1.place(x=500, y=400, width=200, height=25)

        img3 = Image.open("./Resource/Images/prjimg5.jpg")
        img3 = img3.resize((200, 200))
        self.photoImg3 = ImageTk.PhotoImage(img3)
        
        b3 = Button(bg_img, command=self.train_data, image=self.photoImg3, cursor="hand2")
        b3.place(x=100, y=500, width=200, height=200)

        b3_1 = Button(bg_img, command=self.train_data, text="Train Data", cursor="hand2", fg="white", bg="skyblue", font=("times new roman", 16, "bold"))
        b3_1.place(x=100, y=700, width=200, height=25)

        img4 = Image.open("./Resource/Images/prjimg6.jpg")
        img4 = img4.resize((200, 200))
        self.photoImg4 = ImageTk.PhotoImage(img4)
        
        b4 = Button(bg_img, image=self.photoImg4, cursor="hand2")
        b4.place(x=500, y=500, width=200, height=200)

        b4_1 = Button(bg_img, text="Attendance", cursor="hand2", fg="white", bg="skyblue", font=("times new roman", 16, "bold"))
        b4_1.place(x=500, y=700, width=200, height=25)


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_data(self):
        data_dir = ("Cam_Data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset Completed!!", parent=self.root)


    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)\
            
            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
                id,predict=clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100*(1-predict/300))

                conn = mysql.connector.connect(host="localhost", username="root", password="SNStar@5", database="final_sem_project")
                cursor = conn.cursor()

                cursor.execute("select Name from studentdb where SLNo="+str(id))
                n = cursor.fetchone()
                n = '+'.join(n)

                cursor.execute("select Course from studentdb where SLNo="+str(id))
                c = cursor.fetchone()
                c = '+'.join(c)

                cursor.execute("select Roll from studentdb where SLNo="+str(id))
                r = cursor.fetchone()
                r = '+'.join(r)

                if confidence > 77:
                    cv2.putText(img, f"Name: {n}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX , 0.6, (255,255,255), 3)
                    cv2.putText(img, f"Branch: {c}", (x,y-50), cv2.FONT_HERSHEY_COMPLEX , 0.6, (255,255,255), 3)
                    cv2.putText(img, f"Roll: {r}", (x,y-0), cv2.FONT_HERSHEY_COMPLEX , 0.6, (255,255,255), 3)
                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (242,247,74), 3)
                    cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX , 0.6, (255,255,255), 3)

                coord = [x,y,w,h]
            
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()  
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        while True:
            ret,img=video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
