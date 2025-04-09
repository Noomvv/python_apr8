import sqlite3

connection = sqlite3.connect('cars.db')
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS my_cars (id INTEGER, model TEXT, color TEXT, year INTEGER);')

#sql.execute('INSERT INTO my_cars (id, model, color, year) VALUES (1, "Chevrolet", "White", 2024);')
#sql.execute('INSERT INTO my_cars (id, model, color, year) VALUES (2, "BMW", "White", 2025);')
#sql.execute('INSERT INTO my_cars (id, model, color, year) VALUES (3, "Mersedes", "Brutal pink", 2034);')
#sql.execute('INSERT INTO my_cars (id, model, color, year) VALUES (4, "Peppa Car", "Beautiful poop", 2054);')
#sql.execute('INSERT INTO my_cars (id, model, color, year) VALUES (5, "Ultra Tractor", "Lemon soup", 2068);')
#sql.execute('INSERT INTO my_cars (id, model, color, year) VALUES (6, "PC Fly", "Blue sky", 2001);')

#sql.execute('DELETE FROM my_cars WHERE id=2;')
#sql.execute('DELETE FROM my_cars')

sql.execute('UPDATE my_cars SET model = "Cat Car" WHERE model = "Peppa Car";')

print(sql.execute('SELECT * FROM my_cars;').fetchall())
#print(sql.execute('SELECT model FROM my_cars').fetchall())
#print(sql.execute('SELECT * FROM my_cars WHERE id=3;').fetchall())

connection.commit()                                            #подтверждение изменений в базе данных
#connection.close()




#здесь мы создали первую базу данных и таблицу в ней
