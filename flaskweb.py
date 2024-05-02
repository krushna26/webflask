# importing python libraries
from flask import Flask,jsonify,request
app=Flask(__name__)

# -----------------------****____________________

#How to do routing on home page here we dont need ot specify the any name or string for the routing
# It will automatically route on that page when you started app.


@app.route("/")
def fun():
    return "Krushna pawar"

# -----------------------****____________________

#How to pass the variable with route function and how to set the default value to it
# @app.route("/home",methods=['GET','POST'],defaults={'name':'ABCD'})
# @app.route("/home/<name>",methods=['GET','POST'])
# def home(name):
#
#     return "<h1>Hii {} You are on Home<h1>".format(name)

# -----------------------****____________________


#How to extract the values of the varoables from the given query string in python for that
#you need to import the request function in python before running the query.


# @app.route("/query")
# def queryfun():
#     name=request.args.get('name')
#     location=request.args.get('location')
#     return '<h3> hii {} welcome to {}<h3>'.format(name,location)


# -----------------------****____________________

#code for the jsonify the content of file which are given.

# @app.route("/json")
# def fun2():
#     return jsonify({"a":1,"a1":[1,2,3,4,5,6,7,7,92]})





# -----------------------****____________________


#How to send and retrieve data

#First we create the form sendong of the data using route as form

@app.route("/form")
def form():
    return '''
    <form action="process" method='POST'>
    <input type=Text name=name>
    <input type=Text name=location>
    <input type=submit value=submit>
    '''
#Seconly we are retriving data from the given form which processes post request on process route
@app.route('/process',methods=['POST'])
def process():
    name=request.form['name']
    location=request.form['location']
    return '<h1> hii {} Welcome to {}</h1>'.format(name,location)

@app.route("/fly")
def fun2():
    return "We are on the Json Page"
app.run(debug=True)




