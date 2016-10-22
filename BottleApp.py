# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template, request, error

import sqlite3

@route('/')
def home():
    return template('/home/HecticHiccups/mysite/Weeb')

@route('/Jumbo')
def SignedUp():

    return template('/home/HecticHiccups/mysite/Jumbo')

#Copied the the previous route and made this the post Route
#@route('/login', method='POST')
#def form():
    #return template('/home/HecticHiccups/mysite/Form')
    #x=request.forms.get('username')
    #return x;

@route('/login')
def form():
    return template('/home/HecticHiccups/mysite/Form')

#@route('/login', method='POST')
#def form():
    #x = request.forms.get('username')
    #y = request.forms.get('password')
    #if x == 'jesusartteaga@gmail.com' and y =='111':
        #return template('/home/HecticHiccups/mysite/Redirect')
    #else:
         #print("Invalid User")

@route('/login', method='POST')
def login():
   x = request.forms.get('username')
   y = request.forms.get('password')
   connection = sqlite3.connect("/home/HecticHiccups/mysite/ctw.db")
   cursor_v = connection.cursor()
   cursor_v.execute("SELECT * FROM users WHERE email=?", (x,))
   row = cursor_v.fetchone()
   pw = row[1]
   if y != pw:
    return "Invalid"
   else:
     return template('/home/HecticHiccups/mysite/Redirect')

@route('/Dab')
def Dabby():
    return template('/home/HecticHiccups/mysite/Dab')

@route('/Register')
def SignUp():
    return template('/home/HecticHiccups/mysite/SignUp')

@route('/Register', method='POST')
def Signup():
    sign_x = request.forms.get('username')
    sign_y = request.forms.get('password')
    sign_z = request.forms.get('password1')
    if sign_y != sign_z:
        return "Passwords Don't Match"
    else:
        connection = sqlite3.connect("/home/HecticHiccups/mysite/ctw.db")
        cursor_v = connection.cursor()
        cursor_v.execute("insert into users (email, password) values (?,?)", (sign_x,sign_y))
        connection.commit()
        cursor_v.close()
        return template('/home/HecticHiccups/mysite/Jumbo')



@route('/404')
def error():
    return template('/home/HecticHiccups/mysite/404')


application = default_app()

