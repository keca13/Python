#https://www.sqlitetutorial.net/sqlite-python/
import sqlite3
conn = sqlite3.connect('db/test.db')
c = conn.cursor()
#t = ('2015-01-01',)
#c.execute('SELECT * FROM projects WHERE begin_date=?', t)
#print(c.fetchone())

#import csv
#csvFile = open('test2.csv', 'w', newline='')
#csvWriter = csv.writer(csvFile)
#csfFile = ['jack55', 'JAck55w13!@', 'jack55w13!+PA', 'abcabcabc', '@IPcall2015!+PA', 'IPcall2015', '12Golobek0320', '20Golobek0320', '@Golabek0320)#@)', '13Golobek0320', '2323']
#csvWriter = csv.w(csvFile)
#all_elements = list(csvWriter)


def start():
    print(conn)
    print(c,"\n")
    print("What you want to do?\n")
    print(" 0 - SELECT data db\n")
    print(" 1 - INSERT data db\n")
    print(" 2 - DELETE data db\n")
    print(" 4 - UPDATE data db\n")
    print(" 5 - CREATE table db\n")

    choice = input("your choice > ")
    choice2= input("Be sure? >y/n ")
    if "0" in choice:
        if "y" in choice2:
            print_db()
        else:
            dead()
    elif "1" in choice:
        if "y" in choice2:
            insert_db()
        else:
            dead()
    elif "2" in choice:
        if "y" in choice2:
            delete_db()
        else:
            dead()
    elif "4"in choice:
        if "y" in choice2:
            update_db()
        else:
            dead()

    elif "5" in choice:
        if "y" in choice2:
            create_table()
        else:
            dead()
    else:
        start()


def print_db():
    import data_select
    a = data_select.main()
    print('print_db',a)
    dead()

def insert_db():
    import data_insert
    a = data_insert.main()
    print('insert_db',a)
    dead()
def delete_db():
    import data_delete
    a = data_delete.main()
    print('delete_db', a)
    dead()

def update_db():
    import data_update
    a = data_update.main()
    print('update_db',a)
    dead()

def create_table():
    import table_create
    a = table_create.main()
    print('create_table',a)
    dead()


def dead():
    #all_elements = plik
    print('THE END USE PROGRAM')
    #all_elements.append(new_elements)
    #plik.write("\n")
    #plik.writelines(all_elements)
    #plik.writelines(all_elements)
    conn.close()

start()








