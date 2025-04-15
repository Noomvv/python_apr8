import sqlite3

connection = sqlite3.connect('exam.db')
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, age INTEGER, python_grade TEXT)')

sql.execute('INSERT INTO students (id, name, age, python_grade) VALUES (1, "vladimir", 23, "B");')
sql.execute('INSERT INTO students (id, name, age, python_grade) VALUES (2, "sofa", 19, "A");')
sql.execute('INSERT INTO students (id, name, age, python_grade) VALUES (3, "maks", 19, "B");')
sql.execute('INSERT INTO students (id, name, age, python_grade) VALUES (4, "stas", 19, "C");')
sql.execute('INSERT INTO students (id, name, age, python_grade) VALUES (5, "danya", 19, "A");')
sql.execute('INSERT INTO students (id, name, age, python_grade) VALUES (6, "didi", 19, "B");')

connection.commit()                                            #подтверждение изменений в базе данных

def get_student_by_name(name):
    student = sql.execute(f'SELECT * FROM students WHERE name="{name}";').fetchone()
    print(student)

def update_student_grade(name, new_grade):
    sql.execute(f'UPDATE students SET python_grade="{new_grade}" WHERE name="{name}";')
    connection.commit()
    
def delete_student(name):
    sql.execute(f'DELETE FROM students WHERE name="{name}";')
    connection.commit()

while True:
    choice = input('=========================\n1. Get info\n2. Update info\n3. Delete student\n> ')
    if choice == '1':
        name = input('Enter student name> ')
        get_student_by_name(name)
    elif choice == '2':
        name = input('Enter student name> ')
        new_grade = input('Enter new grade> ')
        update_student_grade(name, new_grade)
    elif choice == '3':
        name = input('Enter student name> ')
        delete_student(name)
    else:
        print('Error')