import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  
    database="student_db"
)

cursor = conn.cursor()

def add_student():
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    query = "INSERT INTO students (name, roll_no, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, roll_no, course))
    conn.commit()
    print("Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def update_student():
    student_id = input("Enter student ID to update: ")
    name = input("Enter new name: ")
    roll_no = input("Enter new roll number: ")
    course = input("Enter new course: ")
    query = "UPDATE students SET name=%s, roll_no=%s, course=%s WHERE id=%s"
    cursor.execute(query, (name, roll_no, course, student_id))
    conn.commit()
    print("Student updated successfully!")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print("Student deleted successfully!")

def main():
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

main()
cursor.close()
conn.close()
