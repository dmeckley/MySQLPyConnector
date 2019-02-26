import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='Majorpain80')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()
            query = ("SELECT first_name, last_name FROM authors")
            cursor.execute(query)
            for (first_name, last_name) in cursor:
                print(first_name)
                print(last_name)
            cursor.close()
            conn.close()

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()
    while True:
        userInput = input("Enter q to quit: ")
        if userInput == 'q':
            break