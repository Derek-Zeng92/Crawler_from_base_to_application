# pip install flask
from flask import Flask, render_template, request

app = Flask(__name__)


# 请求过来了. 但是没人接受....没有人给人家一个正确的结果
# http://127.0.0.1:5000  机器上的某个应用程序
# "/"  path
@app.route("/")
def qiaofu():
    # print("有人来了")
    # f = open("index.html", mode="r", encoding="utf-8")
    # content = f.read()
    name = "樵夫"
    # 在服务器端已经把数据渲染在html中了.
    # 在前端看到的html的源代码中是有数据的。
    # content = content.replace("{{}}", name)

    #  渲染模板
    #  渲染模板需要把模板的html移动到templates文件夹内
    return render_template("index.html", name1="樵夫", name2="杨老师")


@app.route("/yang", methods=['GET', "POST"])
def yangzhenzhong():
    # 接收参数
    # request.args 接收到的是url屁股后面? 后的参数
    # uname = request.args.get("username")
    # pwd = request.args.get("pwd")
    # print(uname)
    # print(pwd)
    # if uname != '123456':
    #     return "没数据"

    # 如果没有 UA. 返回错误数据
    ua = request.headers.get("User-Agent")
    if not ua:
        return "shit"
    if "python" in ua:
        return "封你一年..."

    referer = request.headers.get("Referer")
    if not referer:
        return "shitttttttttt"

    cookie = request.cookies.get("wuming")
    if cookie != 'red_cards':
        return "摆了个白。 没有cookie的请求是没有发展的。。。。"

    # post请求时。所有的Form Data的东西自动进入到form里面
    # uname = request.form.get("username")
    # print(uname)

    uname = request.json.get("username")
    print(uname)

    print("超级帅 ")
    lst = [{"name": "alex", "age": 118},
           {"name": "wusir", "age": 108},
           {"name": "qiaofu", "age": 18}]
    return {
        "code": 0,
        "data": lst,
        "msg": "success"
    }


if __name__ == '__main__':
    # 启动web服务,
    # debug=True, 在修改代码的时候自动帮我们完成重启服务器的动作
    # port, 端口
    app.run(debug=True, port=5000)
