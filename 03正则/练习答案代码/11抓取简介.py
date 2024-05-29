import re
"""
<p class="color-gray">
                        [意] 普里莫·莱维 / [意] 莱昂纳多·德·贝内代蒂 / 中信出版社 / 2017-10
</p>
<p>
                        奥斯维辛集中营幸存者的证词合集，由身为化学家的意大利著名作家普里莫·莱维及其奥斯维辛狱友、外科医生德·贝内代蒂共同整理撰写。
                    </p>
"""
f = open('../素材/豆瓣.html','r')
data = f.read()
f.close()

pattern = re.compile('<p class="color-gray">(.*?)</p>',re.DOTALL)
# pattern = re.compile('<p>(.*?)</p>',re.DOTALL)
# print(pattern.findall(data))

# pattern = re.compile('<div class="detail-frame">(.*?)</div>',re.DOTALL)
# pattern = re.compile('(?:<p class="color-gray">.*?</p>)|(?:<p class="detail">.*?</p>)',re.DOTALL)
print(pattern.findall(data))

