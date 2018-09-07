# This imports the Flask class from the flask package
from flask import Flask
# now we instantiate and instance of the flask class by setting the variable
# app equal to the class flask.
# __name__ is a special variable in python that is the name of the module
# It is so flask knows where to look for templates and static files
app = Flask(__name__)

# This part creates the routes for the website. routes are a way of binding a
# URL to a page or function
# the @app.route is known as a decorator. We don't need to know how they work
# to use basic flask. They allow us to add functionality.
@app.route("/")
# by adding a second decorator we can access the home page through a different
# URL
@app.route("/home")
def home():
# by wrapping Hello World in <h1> </h1> we appy html code to indicate this is
# a heading. This isnt necessary to make it run but will increase the font size
    return "<h1>Hello World!</h1>"
# now we can add an about page:
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# This is the entire "Hello World!" flask app. in order to run the app in the
# console enter:
# set FLASK_APP=flaskblog.py
# flask run
# Now if you go the the browser and either copy the IP address in the prompt or
# enter "localhost:5000" into the browser it should run.

# in order to show changes made to the application without having to stop and
# restart the application we can run the app in debug mode:
# set FLASK_DEBUG=1
# then flask run

# The __name__ variable is == __main__ if we run the script with python
# directly.This means that when we run the script with python, it will
# automatically run in debug mode. If we import the module to somewhere else
# and run the script then __name__ will equal the name of the module and it
# wont run in debug mode.
if __name__ == '__main__':
    app.run(debug=True)
# now we can run this scirpt directly with python by typing in the console:
# python flaskblog.py
# this will run it in debug mode automatically.
