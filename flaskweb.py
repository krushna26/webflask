# importing python libraries
from flask import Flask, jsonify, request, redirect, url_for,session

app=Flask(__name__)


app.config['DEBUG']=True
app.config["SECRET_KEY"]='Arrey@123#'

# -----------------------****____________________

#How to do routing on home page here we dont need ot specify the any name or string for the routing
# It will automatically route on that page when you started app.


@app.route("/")
def fun():
    #Id we want to remove the value Stored in the session can be automatically removed from the session when it
    # Goes into the fun page in this case but you can consider the any function name in that case you can write the
    # Below lines of code Which will be helpful for Removing the session variable from sesssion.
    session.pop('name',None)
    return "Krushna pawar"

# -----------------------****____________________

#How to pass the variable with route function and how to set the default value to it
@app.route("/home",methods=['GET','POST'],defaults={'name':'ABCD','location':'pune'})
@app.route("/home/<name>/<location>",methods=['GET','POST'])
def home(name,location):

    #Syntax for the adding the values in the Session
    session['name']=name

    return "<h1>Hii {} You are in {}<h1>".format(name,location)

# -----------------------****____________________


#How to extract the values of the varoables from the given query string in python for that
#you need to import the request function in python before running the query.


@app.route("/query")
def queryfun():

    #Syntax for the fetching values which are stored in the Session
    if 'name' in session:
        name=session['name']
    else:
        name="Krushna"
    location=request.args.get('location')
    return '<h3> hii {} welcome to {}<h3>'.format(name,location)



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


# Ccode for the fetchong data from the JSON
@app.route("/processjson")
def fun2():
    data=request.get_json()
    name=data['name']
    location=data['location']
    randomlis=data['randomlis']
    return jsonify({'result':'sucess','name':name,'location':location,'randomlis':randomlis})


#combining the get and post request under the Single route function in Flask

@app.route("/formdata",methods=["GET","POST"])
def formdata():
    # Here in this case we have added the one form which will send data to the same action and method is post
    # As we know default method is GET So that will be called automatically and process the form data as it have form method as POST

    if request.method=="GET":
        return '''
            <form action="/formdata" method='POST'>
            <input type=Text name=name>
            <input type=Text name=location>
            <input type=submit value=submit>
            '''
    else:
        name=request.form['name']
        location=request.form['location']
        # return '<h1> Hii {} you are on {} stay Happy</h1>'.format(name,location)


        ##If We want to redict data processed into another URL Then This can be possible using redirect(url_for(nameof the function and the parameter you need to pass))
        return redirect(url_for('home',name=name,location=location))


app.run()
