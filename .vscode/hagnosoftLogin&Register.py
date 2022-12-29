import psycopg2
from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

def registerData(first_name,Last_name,password,email):
    try:
        connection = psycopg2.connect(user="postgres",password="root",host="localhost",port="5433",database="postgres")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO register (first_name,last_name,password,email) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (first_name,Last_name,password,email)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        print()
        print("Record inserted successfully into register table")

    except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into register table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def login(nameMy,passwordMy):
    try:
        flag=1
        connection = psycopg2.connect(user="postgres",password="root",host="localhost",port="5433",database="postgres")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from register where password = %s and first_name=%s"

        cursor.execute(postgreSQL_select_Query,(passwordMy,nameMy))
        login_records = cursor.fetchall()
        for row in login_records:
            first_name=row[0]
            password=row[3]
            flag=0

        if flag==1:
            print("Incorrect userName or password")
        else:
            print("Login done")

    finally:
        # closing database connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed \n")



def register():
    print("Register")
    first_name=input("Enter your first name")
    Last_name=input("Enter your last name")
    password=input("Enter your password")
    i=0
    while True:
        if len(password)<9:
            if i==5:
                print("Too many attempts please try later")
                return 0
            print("Please rewrite the password,(password must atleast contain 9 characters")
            password=(input("Please enter your password"))
            i=i+1
        else:
            break
    
    while True:
        email=input("Enter your email address")
        ans=email.find(".com")
        if ans==-1:
            print("Please make sure to use .com at end")
            # email=input("Enter your email address again")
        else:
            break
    registerData(first_name,Last_name,password,email)
    print()
    print("you had entered")
    print("first name: ",first_name)
    print("Last name: ",Last_name)
    print("password: ",password)
    print("email: ",email)
    print("Thanks for registering")
    # login(first_name,Last_name,password)
    return 1

login("alpesh","dfdf")
# register()
# ans=register()
# if ans==1:
#     print("you have successfully registered and logined")
# else:
#    print("Please try later")