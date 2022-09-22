from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "This is the first machine learning projects."


if __name__=="__main__":
    app.run(debug=True)
