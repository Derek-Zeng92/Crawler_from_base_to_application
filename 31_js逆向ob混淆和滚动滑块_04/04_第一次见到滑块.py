import requests
from PIL import Image

def slider_distance(file1, file2) -> str:
    # 打开图片
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    # 获取图片的像素数据
    pixels1 = image1.load()
    pixels2 = image2.load()

    # 循环图片的宽度（左右距离）
    for w in range(image1.width):
        # 循环图片的高度（上下距离）
        for h in range(image1.height):
            # 比较两张图的对应像素
            color1 = pixels1[w, h]
            color2 = pixels2[w, h]
            # 如果像素有变化，说明找到缺口位置，返回横坐标（即距离）
            if color1!= color2:
                return str(w)
    return '未计算出！！！'

session = requests.session()
session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"

first_url = "https://beijing.tuitui99.com/denglu.html"
session.get(first_url)

# 访问图片的url
img_url = "https://beijing.tuitui99.com/tncode.html?t=0.42424328707715864"
img_resp = session.get(img_url)
with open("tu.png", mode="wb") as f:
    f.write(img_resp.content)

# 抠图逻辑
img = Image.open("tu.png")
new_img = img.crop((0, 0, 240, 150))  # 抠.
new_img.save("new_tu.png")
oragin_img = img.crop((0, 300, 240, 450))  # 抠.
oragin_img.save("oragin_tu.png")

# 计算缺口位置.. 第三方
result = slider_distance('oragin_tu.png', 'new_tu.png')

# 发请求看看是否能通过
slide_url = "https://beijing.tuitui99.com/checkcode.html"
print(result)
params = {
    "tn_r": result
}

resp = session.get(slide_url, params=params)
print(resp.text)  # error 错的。。滑块距离的问题。。。
