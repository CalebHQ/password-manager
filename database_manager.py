from encryption import decrypt
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="passwordmanager"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Account (username VARCHAR(50), email VARCHAR(50), password VARCHAR(100) NOT NULL, url VARCHAR(100) NOT NULL, app_name VARCHAR(50) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")


def store_password(username, email, password, url, app_name):
    try:
        mycursor.execute("INSERT INTO Account (username, email, password, url, app_name) VALUES (%s,%s,%s,%s,%s)",
                         (username, email, password, url, app_name))
        db.commit()
    except (Exception, mysql.connector.Error) as error:
        print(error)


def find_app(app_name):
    data = []
    try:
        mycursor.execute(
            "SELECT * FROM Account WHERE app_name = '""" + app_name + "'")
        for x in mycursor:
            data.append(x)
        return data
    except (Exception, mysql.connector.Error) as error:
        print(error)


def find_users(email):
    data = []
    try:
        mycursor.execute(
            "SELECT * FROM Account WHERE email = '""" + email + "'")
        for x in mycursor:
            data.append(x)
        return data
    except (Exception, mysql.connector.Error) as error:
        print(error)


def display_all_data():
    data = []
    try:
        mycursor.execute("SELECT * FROM Account")
        for x in mycursor:
            data.append(x)
        return data
    except (Exception, mysql.connector.Error) as error:
        print(error)


def change_info(id, attribute, value):
    try:
        mycursor.execute(
            f"UPDATE Account SET {attribute} = '" + value + "' WHERE id = '" + id + "'")
        db.commit()
        print(mycursor.rowcount, "record(s) affected")
    except (Exception, mysql.connector.Error) as error:
        print(error)


def delete_data(attribute, value):
    try:
        mycursor.execute(
            f"DELETE FROM Account WHERE {attribute} = '" + value + "'")
        db.commit()
        print(mycursor.rowcount, "record(s) affected")
    except (Exception, mysql.connector.Error) as error:
        print(error)

# print(display_all_data())

# mycursor.execute("SELECT * FROM Account")
# for x in mycursor:
#     print(x)
