import base64
import json
import requests
# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    code_url = 'https://so.gushiwen.cn/RandCode.ashx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    sess = requests.Session()
    res = sess.get(code_url, headers=headers)
    with open('yzm.jpg', 'wb') as f:
        f.write(res.content)
    img_path = "./yzm.jpg"
    result = base64_api(uname='luckyboyxlg', pwd='17346570232', img=img_path, typeid=3)
    print(result)
    # 上半部分是咱们刚才的代码
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

    data = {
        '__VIEWSTATE': 'gRid5bo91a/3jGuyGRrb5K/ONANSyHJgAOW160cLBWy/6dnfzslD1VMDZFCAwg6zRoZwi9lGa/pn1woHDhFvBctNo/ugDw7KM39GNrvmebKfE2cyB2BMd7e98B4=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '793390457@qq.com',
        'pwd': 'xlg17346570232',
        'code': result,
        'denglu': '登录',
    }
    res = sess.post(url, data=data, headers=headers)
    with open('gsw.html', 'wb') as f:
        f.write(res.content)
