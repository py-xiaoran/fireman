import MySQLdb
from os import walk
def getImgField(path):
    w = walk(path)
    d = {'local':None, 'name':None,'type':None,'weight':None,'height':None}
    img_list = list()
    for res in w:
        for index,f in enumerate(res[2]):
            d['local']=res[0]+r"/"+f
            d['name']=f[:-4]
            if res[0].endswith('homeImg'):
                d['type']=1
            elif res[0].endswith('person'):
                d['type']=2
            else:
                d['type']=3
            d['weight']=0
            d['height']=0
            img_list.append(d.copy())
    return img_list

def saveDb(img_list):
    conn = MySQLdb.connect(host='',user='root',passwd='xiaoran',db='xiaoran',port=3306) 
    cur = conn.cursor()
    for img in img_list:
        sql = r'insert into getImg_imagesrc(img_name,img_local,img_type_id,img_weight,img_height) values("%(name)s","%(local)s",1,%(weight)d,%(height)d)'%img
        print sql
        try:
            cur.execute(sql)
        except Exception as e:
            print e
            conn.rollback()
            raise e
    cur.close()
    conn.commit()        

if __name__=="__main__":
    path = "/home/xiaoran/to_git/fireman/fireman/home/static"#raw_input('enter abspath of img:')
    img_list =getImgField(path)
    print img_list
    saveDb(img_list)
