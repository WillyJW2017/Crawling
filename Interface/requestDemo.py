import requests
import json

url = 'http://127.0.0.1:8000/login/'
data = {'username':'Jacky', 'password':'999999'}

def send_post(url, data):
    res = requests.post(url=url, data=data)
    resload = json.loads(res.text)      #将字符串转换为字典
    # resload = json.dumps(res.text)         # 将字典转换为字符串
    print(str(type(resload)))
    return resload

print(send_post(url, data))

