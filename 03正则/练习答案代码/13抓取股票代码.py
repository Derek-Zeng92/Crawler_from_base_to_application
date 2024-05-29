import re
f = open('../素材/股票.html', 'r')
data = f.read()
#第一次 抓取 包含 股票代码信息的数据
pattern = re.compile("<tbody class=\"tbody_right\" id=\"datalist\">(.*?)</tbody>",re.DOTALL)
tbodyData = pattern.findall(data)
# print(tbodyData[0])
#将抓取到的股票信息代码的数据 进行再次过滤  将html标签过滤掉
dataPatt = re.compile(">(.*?)<")
newData = dataPatt.findall(tbodyData[0])

#将 数据里面的空白字符 去掉
newData1 = newData.copy()
for i in newData1:
    # print(i)
    if i == '':
        newData.remove(i)

# print(newData)
#进行数据的展示
print(len(newData))
#外侧走一次
for l in range(0,len(newData),12):
    # print(l) l 0   12    24
    #            j 0-11  0-11  0-11
    #走12次 将每列数据进行 显示
    for j in range(12):
        print(newData[j+l],end=" ")
    print("")