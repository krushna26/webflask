from flask import Flask,render_template,request,url_for

app=Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']='Arrey@123#'
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/abcs",methods=['GET','POST'])
def process():
    name=request.form['name']
    location=request.form['location']
    #here in this case abcs is passed as the boolean varaible and it is used for checking the conditionals
    li=[1,2,3,4,5,6,7,8]
    return render_template('home.html',name=name,location=location,abcs=True,list=li)
app.run()