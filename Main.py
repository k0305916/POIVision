#Main.py

import requests
from PIL import Image
import io

#---
# #用户输入相关信息
# # 类别
# URLqueryclass = ['美食','酒店','购物','生活服务','丽人']
# URLquery = input('(类型共有：{})请输入想查找的类型，以\‘，\’间隔:'.format(URLqueryclass));
# URLquery = URLquery.replace('，', ',')
# URLqueryValue = URLquery.split(',') 
# 
# #location
# URLqueryLoc = input('请输入经纬度（经度,纬度，以','来分隔）：')
# URLqueryLoc = URLqueryLoc.replace('，', ',')
# 
# #radius
# URLqueryRadius = input('请输入搜索半径：')
# 
# #Count
# URLqueryCount = input('请输入预查找的条数')
# URLquerySize = 20
# URLqueryPage = int(int(URLqueryCount) / URLquerySize)
#---

# payload = {'query':'酒店','location':"39.915,116.404","radius":"2000",
#            'page_size':20,'page_num':1,
#            "output":"json","ak":"CTAp7xajfmQwdT5R9GuQ60XUhTF27z3x"}
# URL = "https://api.map.baidu.com/place/v2/search?"
# request = requests.get(URL,payload)
# #print(request.raise_for_status())#检查服务器返回状态
# #print(request.status_code)#服务端返回200,就意味着成功了。
# print(request.text)
# # results = request.json()['results']
# # for result in results:
# #     uid = result['uid']
# #     loc = result['location']
# # #     for loc in result['location']:
# # #         lat = loc['lat']
# # #         lng = loc['lng']
# # #         print(lat)
# # #         print(lng)
# #     print(loc['lat'])
# #     print(loc['lng'])
# #     address = result['address']
# #     name = result['name']
# #     detail = result['detail']
# #     print(name)

#https://api.map.baidu.com/panorama/v2?ak=CTAp7xajfmQwdT5R9GuQ60XUhTF27z3x&width=512&
#height=256&location=116.313393,40.04778&fov=180
#fov:全景图的角度(0-360)
#width:(0-1024]
#height:(0-512]

loc = ['114.11104196900,22.54552469500',
'114.11087532800,22.54549902500',
'114.11070868700,22.54547335600',
'114.11054204600,22.54544768600',
'114.11037540500,22.54542201600',
'114.11020876500,22.54539634600',
'114.11004212400,22.54537067600',
'114.10987548300,22.54534500700',
'114.10970884200,22.54531933700',
'114.10954220100,22.54529366700',
'114.11120861000,22.54555036500',
'114.10954220100,22.54529366700',
'114.11244718400,22.54572194400',
'114.11230956400,22.54570287900',
'114.11217194500,22.54568381500',
'114.11203432600,22.54566475100',
'114.11189670700,22.54564568700',
'114.11175908700,22.54562662200',
'114.11162146800,22.54560755800',
'114.11148384900,22.54558849400',
'114.11134622900,22.54556942900',
'114.11120861000,22.54555036500',
'114.11258480300,22.54574100800',
'114.11120861000,22.54555036500',
'114.11103899000,22.54556362700',
'114.11087053800,22.54558652700',
'114.11071940900,22.54566071500',
'114.11063775000,22.54580639700',
'114.11059908300,22.54597204800',
'114.11056911500,22.54613951700',
'114.11054435000,22.54630783900',
'114.11052275300,22.54647660000',
'114.11050425100,22.54664571700',
'114.11048924900,22.54681519600',
'114.11120861000,22.54555036500',
'114.11048924900,22.54681519600']
 
for myloc in loc:
    panorama = {'ak':'CTAp7xajfmQwdT5R9GuQ60XUhTF27z3x','width':1024,
                'height':512,'location':myloc,
                'fov':360}
    URLpano = "https://api.map.baidu.com/panorama/v2?"
    #返回的是一张图的时候，
    #首先：将图片保存至本地
    #然后：读取image读取图片
    request = requests.get(URLpano,panorama)
    # print(request.text)
    imagecontent = io.BytesIO(request.content)
    # imagecontent.seek(0)
    # byteImg = imagecontent.read()
    pic = Image.open(imagecontent)
    pic.save(myloc+'.png','PNG')
