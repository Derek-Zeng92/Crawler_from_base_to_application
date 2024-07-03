from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/")
def hehe():
    return render_template("index.html")

@app.route("/qiaofu", methods=['GET', "POST"])
def haha():
    dic = {
        "result": [11,22,33],
        "code": "10086",
        "msg": "爱死你了"
    }
    uname = request.json.get("username")
    print(uname)
    return dic

if __name__ == '__main__':
    app.run(debug=True)
