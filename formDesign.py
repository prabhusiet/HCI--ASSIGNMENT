import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog as sd

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',  
            database='PassITDrivingSchool'
        )
        return connection
    except mysql.connector.Error as e:
        messagebox.showerror("Database Connection Error", str(e))
        return None

class DrivingSchoolApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pass IT Driving School Management System")
        self.geometry("900x600")

        # Set the theme
        self.style = ttk.Style(self)
        self.style.theme_use("clam")  # Setting theme to 'clam' which supports more color customization

        # Configure our style
        self.style.configure("TFrame", background="#f3f4f6")
        self.style.configure("TButton", font=('Arial', 12), background="#4CAF50", foreground="white", borderwidth=1)
        self.style.map("TButton", background=[('active', '#45a049')])
        self.style.configure("TLabel", background="#f3f4f6", font=('Arial', 12))
        self.style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 12))  # Modify the font of the Treeview
        self.style.configure("Treeview.Heading", font=('Arial', 14, 'bold'))  # Make the Treeview headings bold

        # Create tabs
        tab_control = ttk.Notebook(self)

        self.instructors_tab = ttk.Frame(tab_control)
        self.students_tab = ttk.Frame(tab_control)
        self.lessons_tab = ttk.Frame(tab_control)

        tab_control.add(self.instructors_tab, text='Instructors')
        tab_control.add(self.students_tab, text='Students')
        tab_control.add(self.lessons_tab, text='Lessons')

        tab_control.pack(expand=1, fill="both")

        # Initialize UIs for each tab
        self.create_instructors_ui()
        self.create_students_ui()
        self.create_lessons_ui()

        # Load initial data from database
        self.load_instructors_data()
        self.load_students_data()
        self.load_lessons_data()

        # Initialize UIs for each tab
        self.create_instructors_ui()
        self.create_students_ui()
        self.create_lessons_ui()

        # Load initial data from database
        self.load_instructors_data()
        self.load_students_data()
        self.load_lessons_data()

    def create_instructors_ui(self):
        ttk.Label(self.instructors_tab, text='Instructor Details', font=('Arial', 15, 'bold')).grid(row=0, column=0, padx=10, pady=10)
        self.instructor_tree = ttk.Treeview(self.instructors_tab, columns=('ID', 'First Name', 'Last Name', 'Contact'), show='headings', selectmode="browse")
        self.instructor_tree.heading('ID', text='ID')
        self.instructor_tree.heading('First Name', text='First Name')
        self.instructor_tree.heading('Last Name', text='Last Name')
        self.instructor_tree.heading('Contact', text='Contact Number')
        self.instructor_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        ttk.Button(self.instructors_tab, text="Add Instructor", command=self.add_instructor).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(self.instructors_tab, text="Delete Instructor", command=self.delete_instructor).grid(row=2, column=1, padx=10, pady=10)

    def create_students_ui(self):
        ttk.Label(self.students_tab, text='Student Details', font=('Arial', 15)).grid(row=0, column=0, padx=10, pady=10)
        self.student_tree = ttk.Treeview(self.students_tab, columns=('ID', 'First Name', 'Last Name', 'Contact', 'Email'), show='headings', selectmode="browse")
        self.student_tree.heading('ID', text='ID')
        self.student_tree.heading('First Name', text='First Name')
        self.student_tree.heading('Last Name', text='Last Name')
        self.student_tree.heading('Contact', text='Contact Number')
        self.student_tree.heading('Email', text='Email')
        self.student_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        ttk.Button(self.students_tab, text="Add Student", command=self.add_student).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(self.students_tab, text="Delete Student", command=self.delete_student).grid(row=2, column=1, padx=10, pady=10)

    def create_lessons_ui(self):
        ttk.Label(self.lessons_tab, text='Lesson Details', font=('Arial', 15)).grid(row=0, column=0, padx=10, pady=10)
        self.lesson_tree = ttk.Treeview(self.lessons_tab, columns=('ID', 'InstructorID', 'StudentID', 'Type', 'Date', 'Duration'), show='headings', selectmode="browse")
        self.lesson_tree.heading('ID', text='ID')
        self.lesson_tree.heading('InstructorID', text='Instructor ID')
        self.lesson_tree.heading('StudentID', text='Student ID')
        self.lesson_tree.heading('Type', text='Lesson Type')
        self.lesson_tree.heading('Date', text='Date')
        self.lesson_tree.heading('Duration', text='Duration (Hours)')
        self.lesson_tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        ttk.Button(self.lessons_tab, text="Add Lesson", command=self.add_lesson).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(self.lessons_tab, text="Delete Lesson", command=self.delete_lesson).grid(row=2, column=1, padx=10, pady=10)

    def load_instructors_data(self):
        connection = create_db_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Instructors"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.instructor_tree.delete(*self.instructor_tree.get_children())  # Clear the existing data
            for row in rows:
                self.instructor_tree.insert("", tk.END, values=row)
            connection.close()

    def load_students_data(self):
        connection = create_db_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Students"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.student_tree.delete(*self.student_tree.get_children())  # Clear the existing data
            for row in rows:
                self.student_tree.insert("", tk.END, values=row)
            connection.close()

    def load_lessons_data(self):
        connection = create_db_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM Lessons"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.lesson_tree.delete(*self.lesson_tree.get_children())  # Clear the existing data
            for row in rows:
                self.lesson_tree.insert("", tk.END, values=row)
            connection.close()

    # Implement the add_instructor, add_student, add_lesson functions here using similar patterns as delete_instructor

    def delete_instructor(self):
        selected_item = self.instructor_tree.selection()
        if selected_item:
            item_values = self.instructor_tree.item(selected_item, "values")
            instructor_id = item_values[0]
            response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this instructor?")
            if response:
                connection = create_db_connection()
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Instructors WHERE InstructorID = %s", (instructor_id,))
                connection.commit()
                connection.close()
                self.instructor_tree.delete(selected_item)
                messagebox.showinfo("Success", "Instructor deleted successfully!")

    def delete_student(self):
        selected_item = self.student_tree.selection()
        if selected_item:
            item_values = self.student_tree.item(selected_item, "values")
            student_id = item_values[0]
            response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")
            if response:
                connection = create_db_connection()
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Students WHERE StudentID = %s", (student_id,))
                connection.commit()
                connection.close()
                self.student_tree.delete(selected_item)
                messagebox.showinfo("Success", "Student deleted successfully!")

    def delete_lesson(self):
        selected_item = self.lesson_tree.selection()
        if selected_item:
            item_values = self.lesson_tree.item(selected_item, "values")
            lesson_id = item_values[0]
            response = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this lesson?")
            if response:
                connection = create_db_connection()
                cursor = connection.cursor()
                cursor.execute("DELETE FROM Lessons WHERE LessonID = %s", (lesson_id,))
                connection.commit()
                connection.close()
                self.lesson_tree.delete(selected_item)
                messagebox.showinfo("Success", "Lesson deleted successfully!")
    
    def add_instructor(self):
        def save_data():
            try:
                connection = create_db_connection()
                cursor = connection.cursor()
                sql = "INSERT INTO Instructors (FirstName, LastName, ContactNumber) VALUES (%s, %s, %s)"
                cursor.execute(sql, (first_name.get(), last_name.get(), contact_number.get()))
                connection.commit()
                connection.close()
                new_window.destroy()
                messagebox.showinfo("Success", "Instructor added successfully!")
                self.load_instructors_data()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", str(e))
        
        new_window = tk.Toplevel(self)
        new_window.title("Add New Instructor")
        tk.Label(new_window, text="First Name:").grid(row=0, column=0)
        first_name = tk.Entry(new_window)
        first_name.grid(row=0, column=1)
        tk.Label(new_window, text="Last Name:").grid(row=1, column=0)
        last_name = tk.Entry(new_window)
        last_name.grid(row=1, column=1)
        tk.Label(new_window, text="Contact Number:").grid(row=2, column=0)
        contact_number = tk.Entry(new_window)
        contact_number.grid(row=2, column=1)
        tk.Button(new_window, text="Save", command=save_data).grid(row=3, column=1, pady=10)

    def add_student(self):
        def save_data():
            try:
                connection = create_db_connection()
                cursor = connection.cursor()
                sql = "INSERT INTO Students (FirstName, LastName, ContactNumber, Email) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (first_name.get(), last_name.get(), contact_number.get(), email.get()))
                connection.commit()
                connection.close()
                new_window.destroy()
                messagebox.showinfo("Success", "Student added successfully!")
                self.load_students_data()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", str(e))
        
        new_window = tk.Toplevel(self)
        new_window.title("Add New Student")
        tk.Label(new_window, text="First Name:").grid(row=0, column=0)
        first_name = tk.Entry(new_window)
        first_name.grid(row=0, column=1)
        tk.Label(new_window, text="Last Name:").grid(row=1, column=0)
        last_name = tk.Entry(new_window)
        last_name.grid(row=1, column=1)
        tk.Label(new_window, text="Contact Number:").grid(row=2, column=0)
        contact_number = tk.Entry(new_window)
        contact_number.grid(row=2, column=1)
        tk.Label(new_window, text="Email:").grid(row=3, column=0)
        email = tk.Entry(new_window)
        email.grid(row=3, column=1)
        tk.Button(new_window, text="Save", command=save_data).grid(row=4, column=1, pady=10)

    def add_lesson(self):
        def save_data():
            try:
                connection = create_db_connection()
                cursor = connection.cursor()
                sql = "INSERT INTO Lessons (InstructorID, StudentID, LessonType, LessonDate, DurationHours) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (instructor_id.get(), student_id.get(), lesson_type.get(), lesson_date.get(), duration_hours.get()))
                connection.commit()
                connection.close()
                new_window.destroy()
                messagebox.showinfo("Success", "Lesson added successfully!")
                self.load_lessons_data()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", str(e))
        
        new_window = tk.Toplevel(self)
        new_window.title("Add New Lesson")
        tk.Label(new_window, text="Instructor ID:").grid(row=0, column=0)
        instructor_id = tk.Entry(new_window)
        instructor_id.grid(row=0, column=1)
        tk.Label(new_window, text="Student ID:").grid(row=1, column=0)
        student_id = tk.Entry(new_window)
        student_id.grid(row=1, column=1)
        tk.Label(new_window, text="Lesson Type:").grid(row=2, column=0)
        lesson_type = tk.Entry(new_window)
        lesson_type.grid(row=2, column=1)
        tk.Label(new_window, text="Lesson Date (YYYY-MM-DD HH:MM:SS):").grid(row=3, column=0)
        lesson_date = tk.Entry(new_window)
        lesson_date.grid(row=3, column=1)
        tk.Label(new_window, text="Duration (Hours):").grid(row=4, column=0)
        duration_hours = tk.Entry(new_window)
        duration_hours.grid(row=4, column=1)
        tk.Button(new_window, text="Save", command=save_data).grid(row=5, column=1, pady=10)


if __name__ == "__main__":
    app = DrivingSchoolApp()
    app.mainloop()
