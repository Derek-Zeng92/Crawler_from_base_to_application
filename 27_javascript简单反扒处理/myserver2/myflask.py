from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/")
def hehe():
    return render_template("index.html")

@app.route("/qiaofu")
def haha():
    dic = {
        "result": [11,22,33],
        "code": "10086",
        "msg": "爱死你了"
    }

    # 返回的数据不能直接是 数据了. 需要套在 xxxxxx(数据)
    cb = request.args.get("callback")
    if cb:
        # xxxxxxxxxxx(    数据                )
        return cb + "(" + json.dumps(dic) + ")"
    else:
        return "哈哈"

if __name__ == '__main__':
    app.run(debug=True)
