from flask import Flask,request

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    return '<h1>This home page</h1>'

@app.route('/viewcart',methods=['GET','POST'])
def name():
    return '<h1>puja has a top in her cart</h1>'


if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000)