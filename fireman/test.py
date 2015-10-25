from algorithm.search import algor_search_img
name='xiaoran'
li=['ddd','xia','xiaoran','bbbxia','xiadls','bkxiaoran','ccxi','xiaccc','xccd']
res = algor_search_img(name,li)
print res
class test(object):
    name=''
    def __init__(self,name):
        self.name=name
li2=list()
for l in  li:
    t = test(l)
    print t
    li2.append(t)
print li2
res2 = algor_search_img(name,li2,attr='name')
print "---------"
for level,t in res2:
    print level,t.name

