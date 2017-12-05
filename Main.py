#Main.py
#Main()
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
panorama = {'ak':'CTAp7xajfmQwdT5R9GuQ60XUhTF27z3x','width':1024,
            'height':512,'location':'114.0553871,22.58026372',
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
s = Image.open(imagecontent)
s.show()
# with open("/home/fansli/PythonSpace/POIVision/sample.jpg", 'wb') as f:
#         f.write(request.content)

