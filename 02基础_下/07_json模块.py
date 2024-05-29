"""
xml

<wf>
    <name>汪峰</name>
    <age>18</age>
</wf>

json

wf = {
    name: "汪峰“，
    age: 18
}

"""


# json的处理本质上就是处理字典
# json是前端对象经过字符串化处理之后的那个东西
# 7
# {name: "alex", age:18}  -> 对象
# '{"name": "alex", "age":18}' -> json
#  拿到的json是一个字符串

# 7
# s = '{"name": "alex", "age":18}'
# # 把json字符串变成python的字典。 之后拿数据就爽
# import json  # 专门用来处理json的
# dic = json.loads(s)  # 把字符串变成字典
#
# print(dic)
# print(type(dic))
# print(dic['name'])
#
# # s = '[{"rating":["9.3","50"],"rank":1,"cover_url":"https://img2.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2564556863.jpg","is_playable":true,"id":"1307914","types":["剧情","犯罪","惊悚"],"regions":["中国香港"],"title":"无间道","url":"https:\/\/movie.douban.com\/subject\/1307914\/","release_date":"2003-09-05","actor_count":23,"vote_count":1215015,"score":"9.3","actors":["刘德华","梁朝伟","黄秋生","曾志伟","郑秀文","陈慧琳","陈冠希","余文乐","林家栋","萧亚轩","姚文基","利沙华","黄燕强","苏伟南","吴廷烨","洪智杰","尹志强","何华超","李天翔","张艺","叶清","林迪安","许金峰"],"is_watched":false}]'

# 可能需要把一个字典转化成json字符串
# import json
#
# dic = {"name": "alex", "age": 18}
#
# s = json.dumps(dic)  # 字典变成json字符串
# print(s)
# print(type(s))

# dic = {"name": "alex", "age": 18, "hunfou": True}
# s = str(dic)  # 不行的
# print(type(s))
# print(s)
# # json的概念不是python的，这个概念是前端的\
# import json  # 7
# print(json.dumps(dic))

# 自己尝试
# import pprint
# pprint.pprint()

