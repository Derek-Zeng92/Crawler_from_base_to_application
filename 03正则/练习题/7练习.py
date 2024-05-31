import re
myStr = """
	caoxigang@baidu.html
曹　艳	Caoyan	6895	13811661805	caoyan@baidu.html
曹　宇	Yu Cao	8366	13911404565	caoyu@baidu.html
曹　越	Shirley Cao	6519	13683604090	caoyue@baidu.html
曹　政	Cao Zheng	8290	13718160690	caozheng@baidu.html
查玲莉	Zha Lingli	6259	13552551952	zhalingli@baidu.html
查　杉	Zha Shan	8580	13811691291	zhashan@baidu.html
查　宇	Rachel	8825	13341012971	zhayu@baidu.html
柴桥子	John	6262	13141498105	chaiqiaozi@baidu.html
常丽莉	lily	6190	13661003657	changlili@baidu.html
车承轩	Che Chengxuan	6358	13810729040	chechengxuan@baidu.html
陈　洁	Che	13811696984	chenxi_cs@baidu.html
陈　超	allen	8391	13810707562	chenchao@baidu.html
陈朝辉		13714189826	chenchaohui@baidu.html
陈　辰	Chen Chen	6729	13126735289	chenchen_qa@baidu.html
陈　枫	windy	8361	13601365213	chenfeng@baidu.html
陈海腾	Chen Haiteng	8684	13911884480	chenhaiteng@baidu.html
陈　红	Hebe	8614	13581610652	chenhong@baidu.html
陈后猛	Chen Houmeng	8238	13811753474	chenhoumeng@baidu.html
陈健军	Chen Jianjun	8692	13910828583	chenjianjun@baidu.html
陈　景	Chen Jing	6227	13366069932	chenjing@baidu.html
陈竞凯	Chen Jingkai	6511	13911087971	jchen@baidu.html
陈　坤	Isa13810136756	chenlei@baidu.html
陈　林	Lin Chen	6828	13520364278	chenlin@qq.com
"""
#匹配 手机号
#匹配 邮箱

# (1) 手机号
# res = re.findall("[1][3-8]\d{9}",myStr)
#（2）邮箱
res = re.findall("\w+@.+\.\w+",myStr)
print(res)