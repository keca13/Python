import sqlite3
from sqlite3 import Error
import datetime


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects2(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    #In this function, we used the  lastrowid attribute of the Cursor object to get back the generated id.
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks2(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def main():
    database = r"E:\python\pycharm\lnp\db\test.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project_name = input("Write project name: >")
        now = datetime.datetime.now()
        end = now + datetime.timedelta(days=+14)

        project = (project_name, now.strftime("%x"), end.strftime("%x"))
        project_id = create_project(conn, project)

        # tasks
        task_name = input("Podaj nazwe tasku: >")
        date_start = datetime.datetime.now()
        date_end = date_start + datetime.timedelta(days=+14)
        task_1 = (task_name, 1, 1, project_id, date_start.strftime("%x"), date_end.strftime("%x"))
        #task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2020-01-03', '2020-01-05')

        # create tasks
        create_task(conn, task_1)
        #create_task(conn, task_2)


if __name__ == '__main__':
    main()