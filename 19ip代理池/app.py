'''
python的web框架
进行请求  返回一个可用的ip
'''
# pip install flask
from flask import Flask
from proxy_redis import ProxyRedis
# 实例化flask类
app = Flask(__name__)
# http://127.0.0.1:5000/
# @app.route('/get_ip/')
@app.route('/')
def index():
    pr = ProxyRedis()
    ip = pr.get_ip()  # 返回可用性比较大的ip
    if ip:
        return ip
    return '来了老弟'

# 只要调用run  就可以运行当前的flask框架
def run():
    app.run()  # 运行flask

if __name__ == '__main__':
    app.run(debug=True)  # 运行flask
