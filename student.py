from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Smart Attendance System")

        self.var_slno=IntVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_name=StringVar()
        self.var_sic=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()


        img = Image.open("./Resource/Images/prjImage.jpg")
        img = img.resize((1920, 1080))
        self.photoImg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoImg)
        bg_img.place(x=0, y=0, width=1920, height=1080)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT", font=('times new roman', 30, "bold"), fg="white", bg="skyblue")
        title_lbl.place(x=0, y=50, width=650, height=35)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=50, y=100, width=1420, height=700)


        #Left Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=('times new romman', 12, 'bold'), fg="skyblue")
        left_frame.place(x=30, y=50, width=660, height=580)

        course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Major", font=('times new romman', 12, 'bold'), fg="skyblue")
        course_frame.place(x=8, y=20, width=640, height=125)

        search_label = Label(course_frame, text="Department: ", font=('times new romman', 12, 'bold'), fg="skyblue")
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(course_frame, textvariable=self.var_dep, font=('times new romman', 10), width=17, state="read only")
        dep_combo['values'] = ('Select Department','M.Tech', 'MCA', 'B.Tech')
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        course_label = Label(course_frame, text="Course: ", font=('times new romman', 12, 'bold'), fg="skyblue")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(course_frame, textvariable=self.var_course, font=('times new romman', 10), width=17, state="read only")
        course_combo['values'] = ('Select Course','CSE', 'CST', 'CEN', 'ECE', 'EEE', 'EIE')
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        year_label = Label(course_frame, text="Year: ", font=('times new romman', 12, 'bold'), fg="skyblue")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(course_frame, textvariable=self.var_year,  font=('times new romman', 10), width=17, state="read only")
        year_combo['values'] = ('Select Year', '2020-21', '2021-22', '2022-23', '2023-24')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        semester_label = Label(course_frame, text="Semester: ", font=('times new romman', 12, 'bold'), fg="skyblue")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(course_frame, textvariable=self.var_semester, font=('times new romman', 10), width=17, state="read only")
        semester_combo['values'] = ('Select Semester',1, 2, 3, 4, 5, 6, 7, 8)
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Student Info", font=('times new romman', 12, 'bold'), fg="skyblue")
        student_frame.place(x=8, y=175, width=640, height=380)

        name_label = Label(student_frame, text="Name: ", font=('times new romman', 12, 'bold'), fg="skyblue")
        name_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        name_entry = ttk.Entry(student_frame, textvariable=self.var_name, font=('times new romman', 10), width=20)
        name_entry.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        sic_no_label = Label(student_frame, text="SIC: ", font=('times new romman', 12, 'bold'), fg="skyblue")
        sic_no_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        sic_no_entry = ttk.Entry(student_frame, textvariable=self.var_sic, font=('times new romman', 10), width=20)
        sic_no_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        roll_no_label = Label(student_frame, text="Roll/Reg No:  ", font=('times new romman', 12, 'bold'), fg="skyblue")
        roll_no_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        roll_no_entry = ttk.Entry(student_frame, textvariable=self.var_roll, font=('times new romman', 10), width=20)
        roll_no_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        dob_label = Label(student_frame, text="DOB: ", font=('times new romman', 12, 'bold'), fg="skyblue")
        dob_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        dob_entry = ttk.Entry(student_frame, textvariable=self.var_dob, font=('times new romman', 10), width=20)
        dob_entry.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        email_label = Label(student_frame, text="Email: ", font=('times new romman', 12, 'bold'), fg="skyblue")
        email_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        email_entry = ttk.Entry(student_frame, textvariable=self.var_email, font=('times new romman', 10), width=20)
        email_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)

        phone_no_label = Label(student_frame, text="Phone No:  ", font=('times new romman', 12, 'bold'), fg="skyblue")
        phone_no_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        phone_no_entry = ttk.Entry(student_frame, textvariable=self.var_phone, font=('times new romman', 10), width=20)
        phone_no_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=7, column=1, padx=10, pady=10, sticky=W)

        radiobtn2 = ttk.Radiobutton(student_frame, variable=self.var_radio1, text="Without Photo Sample", value="No")
        radiobtn2.grid(row=7, column=2, padx=10, pady=10, sticky=W)

        save_btn = Button(student_frame, command=self.add_data, text="SAVE", width=14, font=('times new romman', 12, 'bold'), fg="purple", bg="lightyellow")
        save_btn.grid(row=9, column=0, padx=4, pady=20)

        update_btn = Button(student_frame, command=self.updata_data, text="UPDATE", width=14, font=('times new romman', 12, 'bold'), fg="purple", bg="lightyellow")
        update_btn.grid(row=9, column=1, pady=20)

        delete_btn = Button(student_frame, command=self.delete_data, text="DELETE", width=14, font=('times new romman', 12, 'bold'), fg="purple", bg="lightyellow")
        delete_btn.grid(row=9, column=2, pady=20)

        reset_btn = Button(student_frame, command=self.reset_data, text="RESET", width=14, font=('times new romman', 12, 'bold'), fg="purple", bg="lightyellow")
        reset_btn.grid(row=9, column=3, pady=20)

        photo_btn = Button(student_frame, command=self.generate_dataset, text="Take Photo Sample", width=30, font=('times new romman', 12, 'bold'), fg="purple", bg="lightyellow")
        photo_btn.grid(row=10, column=0, columnspan=2, padx=4, pady=4)

        uphoto_btn = Button(student_frame, text="Update Photo Sample", width=30, font=('times new romman', 12, 'bold'), fg="purple", bg="lightyellow")
        uphoto_btn.grid(row=10, column=2, columnspan=2, pady=4)        


        #Right Frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=('times new romman', 12, 'bold'), fg="skyblue")
        right_frame.place(x=720, y=50, width=660, height=580)

        img1 = Image.open("./Resource/Images/prjimg4.jpg")
        img1 = img1.resize((650,150))
        self.photoImg1 = ImageTk.PhotoImage(img1)

        img_lb = Label(right_frame, image=self.photoImg1)
        img_lb.place(x=3, y=0, width=650, height=150)

        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System", font=('times new romman', 12, 'bold'), fg="skyblue")
        search_frame.place(x=3, y=150, width=650, height=75)

        search_label = Label(search_frame, text="Search by: ", font=('times new romman', 14, 'bold'), fg="purple", bg="red")
        search_label.grid(row=0, column=0, padx=4, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=('times new romman', 13), width=10, state="read only")
        search_combo['values'] = ('Select', 'SIC_No', 'Name', 'Roll_No')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, font=('times new romman', 10), width=20)
        search_entry.grid(row=0, column=2,pady=10, sticky=W)
        
        search_btn = Button(search_frame, text="SEARCH", width=12, font=('times new romman', 12, 'bold'), fg="purple", bg="lightyellow")
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn = Button(search_frame, text="SHOW ALL", width=12, font=('times new romman', 12, 'bold'), fg="purple", bg="lightyellow")
        showAll_btn.grid(row=0, column=4, padx=2)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=3, y=225, width=650, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("slno", "Dep", "Course", "Year", "Sem", "Name", "SIC", "Roll", "DOB", "Email", "PhoneNo", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("slno", text="SLNo")
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("SIC", text="SIC")
        self.student_table.heading("Roll", text="Roll")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("PhoneNo", text="PhoneNo")
        self.student_table.heading("Photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("slno", width=80)
        self.student_table.column("Dep", width=120)
        self.student_table.column("Course", width=120)
        self.student_table.column("Year", width=120)
        self.student_table.column("Sem", width=120)
        self.student_table.column("Name", width=120)
        self.student_table.column("SIC", width=120)
        self.student_table.column("Roll", width=120)
        self.student_table.column("DOB", width=120)
        self.student_table.column("Email", width=120)
        self.student_table.column("PhoneNo", width=120)
        self.student_table.column("Photo", width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    
    #======Functions=====
    def add_data(self):
        try:
            if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_name.get() == "" or self.var_sic.get() == "" or self.var_roll.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "":
                messagebox.showerror("Error, All feilds are required", parent=self.root)
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="SNStar@5", database="final_sem_project")
                cursor = conn.cursor()
                cursor.execute("insert into studentdb (Department, Course, Year, Semester, Name, SIC, Roll, DOB, Email, PhoneNo, PhotoSample) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                self.var_sic.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_radio1.get()
                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="SNStar@5", database="final_sem_project")
        cursor = conn.cursor()
        cursor.execute("select * from studentdb")
        data = cursor.fetchall()
        print(data)


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""): 
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[1]),
        self.var_course.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_name.set(data[5]),
        self.var_sic.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_radio1.set(data[11])


    def updata_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_name.get() == "" or self.var_sic.get() == "" or self.var_roll.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "":
                messagebox.showerror("Error, All feilds are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="SNStar@5", database="final_sem_project")
                    cursor = conn.cursor()
                    cursor.execute("update studentdb set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Roll=%s, DOB=%s, Email=%s, PhoneNo=%s, PhotoSample=%s where SIC=%s",(
                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_sic.get()
                                                                                                                                                                                    ))
                else:
                    if not update:
                        return

                messagebox.showinfo("Success","Student details have been update successfully", parent=self.root)                
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)


    def delete_data(self):
        if self.var_sic.get() == "":
            messagebox.showerror("Error", "Student SIC is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete box", "Do you want ro delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="SNStar@5", database="final_sem_project")
                    cursor = conn.cursor()
                    cursor.execute("delete from studentdb where sic=%s", (self.var_sic.get(),))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else: 
                    if not delete:
                        return
                messagebox.showinfo("Success", "Registered student deleted successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)
    

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_name.set(""),
        self.var_sic.set(""),
        self.var_roll.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_radio1.set("")

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_name.get() == "" or self.var_sic.get() == "" or self.var_roll.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "":
                messagebox.showerror("Error, All feilds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="SNStar@5", database="final_sem_project")
                cursor = conn.cursor()
                cursor.execute("select * from studentdb")
                res = cursor.fetchall()
                id = 0
                self.var_slno.set(id+1)
                for x in res:
                    id += 1
                cursor.execute("update studentdb set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, SIC=%s, Roll=%s, DOB=%s, Email=%s, PhoneNo=%s, PhotoSample=%s where SLNo=%s",(
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_sic.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_slno.get()==id+1
                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,cam_frame=cap.read()
                    if face_cropped(cam_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(cam_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "Cam_Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face,str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Tesult", "Generating Data set Completed")
            except Exception as e:
                messagebox.showerror("Error", f"Due To: {str(e)}", parent=self.root)

    




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()