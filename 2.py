import sqlite3

connection = sqlite3.connect('bank.db')
sql = connection.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS my_bank (id INTEGER, name TEXT, balance INTEGER);')

sql.execute('INSERT INTO my_bank (id, name, balance) VALUES (1, "Vladimir", 8000);')
sql.execute('INSERT INTO my_bank (id, name, balance) VALUES (2, "Sofa", 9000);')
sql.execute('INSERT INTO my_bank (id, name, balance) VALUES (3, "Maksim", 5000);')
sql.execute('INSERT INTO my_bank (id, name, balance) VALUES (4, "Danil", 3000);')
sql.execute('INSERT INTO my_bank (id, name, balance) VALUES (5, "Diyora", 6000);')
sql.execute('INSERT INTO my_bank (id, name, balance) VALUES (6, "Latifa", 5000);')

#connection.commit()                                            #подтверждение изменений в базе данных

class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self):
        deposit = int(input('enter deposit amount> '))
        balance = sql.execute(f'SELECT balance FROM my_bank WHERE name="{client}";').fetchone()
        print(type(balance))
        balance_int = int(balance[0])
        print(type(balance_int))
        result = balance_int + deposit
        sql.execute(f'UPDATE my_bank SET balance = {result} WHERE name="{client}";')
        
    def cash(self):
        cash = int(input('enter cash amount> '))
        balance = sql.execute(f'SELECT balance FROM my_bank WHERE name="{client}";').fetchone()
        balance_int = int(balance[0])
        result = balance_int - cash
        sql.execute(f'UPDATE my_bank SET balance = {result} WHERE name="{client}";')
        
    def my_balance(self):
        balance = sql.execute(f'SELECT balance FROM my_bank WHERE name="{client}";').fetchone()
        print(balance)

client = input('name> ')

while True:    
    choice = input('=========================\n1. Deposit\n2. Cash\n3. My balance\n4. Exit\n>')

    if choice == '3':
        BankAccount.my_balance(client)
        #connection.commit()
    elif choice == '1':
        BankAccount.deposit(client)
        #connection.commit()
    elif choice == '2':
        BankAccount.cash(client)
    elif choice == '4':
        print('Thank you!')
        break
    else:
        print('Error')
    





