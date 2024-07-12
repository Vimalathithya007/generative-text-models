from flask import Flask,render_template,request,redirect
from datetime import datetime

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        pass
    return render_template('index.html',alltodo=alltodo)


@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method =='POST':
        pass
        return redirect("/")
    return render_template('update.html',todo=todo)



if __name__=="__main__":
    app.run(debug=True)